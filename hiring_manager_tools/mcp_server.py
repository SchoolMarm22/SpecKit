"""MCP server for Hiring Manager Tools — exposes spec resources and tools."""

import json
import os

from mcp.server import Server
from mcp.types import Resource, Tool, TextContent


def create_mcp_server(specs_dir: str = "specs") -> Server:
    """Create and configure the MCP server."""
    server = Server("hiring_manager_tools")

    @server.list_resources()
    async def list_resources():
        """List all available spec resources."""
        from hiring_manager_tools.spec import list_specs
        resources = []
        all_specs = list_specs(specs_dir)
        for spec in all_specs:
            name = os.path.splitext(os.path.basename(spec.source_path))[0]
            uri = f"spec://{spec.kind}/{name}"
            resources.append(Resource(
                uri=uri,
                name=f"{spec.metadata.get('role', name)} ({spec.kind})",
                description=f"{spec.kind} spec: {spec.metadata.get('role', name)}",
                mimeType="text/markdown",
            ))
        return resources

    @server.read_resource()
    async def read_resource(uri: str):
        """Read a spec resource by URI."""
        # Parse uri: spec://kind/name
        parts = uri.replace("spec://", "").split("/", 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid spec URI: {uri}")
        kind, name = parts
        spec_path = os.path.join(specs_dir, kind, f"{name}.md")
        if not os.path.exists(spec_path):
            raise FileNotFoundError(f"Spec not found: {spec_path}")
        with open(spec_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content

    @server.list_tools()
    async def list_tools():
        """List available tools."""
        return [
            Tool(
                name="prepare_interview",
                description="Generate an interview preparation package from a hiring spec and resume",
                inputSchema={
                    "type": "object",
                    "required": ["spec_ref", "resume_text"],
                    "properties": {
                        "spec_ref": {
                            "type": "string",
                            "description": "Spec path like 'hiring/senior-frontend-platform'"
                        },
                        "resume_text": {
                            "type": "string",
                            "description": "The candidate's resume as plain text"
                        }
                    }
                }
            ),
            Tool(
                name="lint_spec",
                description="Analyze a spec file for bias, vagueness, and quality issues",
                inputSchema={
                    "type": "object",
                    "required": ["spec_ref"],
                    "properties": {
                        "spec_ref": {
                            "type": "string",
                            "description": "Spec path like 'hiring/senior-frontend-platform'"
                        }
                    }
                }
            ),
            Tool(
                name="list_specs",
                description="List available spec files",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "kind": {
                            "type": "string",
                            "description": "Optional filter by spec kind (e.g., 'hiring')"
                        }
                    }
                }
            ),
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        """Handle tool calls."""
        if name == "prepare_interview":
            return await _prepare_interview(arguments, specs_dir)
        elif name == "lint_spec":
            return await _lint_spec(arguments, specs_dir)
        elif name == "list_specs":
            return await _list_specs(arguments, specs_dir)
        else:
            raise ValueError(f"Unknown tool: {name}")

    return server


async def _prepare_interview(arguments: dict, specs_dir: str):
    from hiring_manager_tools.spec import load_spec
    from hiring_manager_tools.claude_client import ClaudeClient
    from hiring_manager_tools.engine import Engine
    from hiring_manager_tools.registry import create_default_registry

    spec_ref = arguments["spec_ref"]
    resume_text = arguments["resume_text"]

    spec_path = os.path.join(specs_dir, f"{spec_ref}.md")
    spec = load_spec(spec_path)

    registry = create_default_registry()
    module = registry.resolve("interview_prep", spec.kind)
    plan = module.plan(spec, {"resume_text": resume_text})

    client = ClaudeClient()
    engine = Engine(client)
    result = engine.execute(plan, spec, module.name)

    return [TextContent(
        type="text",
        text=json.dumps({"output": result.output, "meta": result.meta}, indent=2),
    )]


async def _lint_spec(arguments: dict, specs_dir: str):
    from hiring_manager_tools.spec import load_spec
    from hiring_manager_tools.validation import validate_spec_structure
    from hiring_manager_tools.claude_client import ClaudeClient
    from hiring_manager_tools.engine import Engine
    from hiring_manager_tools.registry import create_default_registry

    spec_ref = arguments["spec_ref"]
    spec_path = os.path.join(specs_dir, f"{spec_ref}.md")
    spec = load_spec(spec_path)

    structural_issues = validate_spec_structure(spec)
    structural_json = [
        {"level": i.level, "field": i.field, "message": i.message}
        for i in structural_issues
    ]

    registry = create_default_registry()
    module = registry.resolve("spec_lint", spec.kind)
    plan = module.plan(spec, {})

    client = ClaudeClient()
    engine = Engine(client)
    result = engine.execute(plan, spec, module.name)

    return [TextContent(
        type="text",
        text=json.dumps({
            "structural_issues": structural_json,
            "ai_lint": result.output,
            "meta": result.meta,
        }, indent=2),
    )]


async def _list_specs(arguments: dict, specs_dir: str):
    from hiring_manager_tools.spec import list_specs as ls

    kind = arguments.get("kind")
    specs = ls(specs_dir, kind=kind)
    output = []
    for s in specs:
        name = os.path.splitext(os.path.basename(s.source_path))[0]
        output.append({
            "path": s.source_path,
            "kind": s.kind,
            "role": s.metadata.get("role"),
            "team": s.metadata.get("team"),
            "version": s.version,
        })

    return [TextContent(type="text", text=json.dumps(output, indent=2))]
