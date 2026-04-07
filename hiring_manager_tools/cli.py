"""CLI entry point for Hiring Manager Tools."""

import json
import os
import sys

import click


@click.group()
def main():
    """Hiring Manager Tools -- AI-native people management, configured by spec files."""
    pass


@main.command()
@click.option("--spec", required=True, help="Spec path relative to specs/ directory (e.g., hiring/senior-frontend-platform)")
@click.option("--resume", required=True, help="Path to resume text file")
@click.option("--specs-dir", default="specs", help="Base directory for spec files")
@click.option("--output", default=None, help="Output file path (default: stdout)")
@click.option("--pretty", is_flag=True, help="Pretty-print JSON output")
def prep(spec, resume, specs_dir, output, pretty):
    """Generate an interview prep package from a spec and resume."""
    from hiring_manager_tools.spec import load_spec
    from hiring_manager_tools.claude_client import ClaudeClient
    from hiring_manager_tools.engine import Engine
    from hiring_manager_tools.registry import create_default_registry

    # Load spec
    spec_path = os.path.join(specs_dir, f"{spec}.md")
    if not os.path.exists(spec_path):
        click.echo(f"Error: Spec file not found: {spec_path}", err=True)
        sys.exit(1)

    spec_file = load_spec(spec_path)

    # Read resume
    if not os.path.exists(resume):
        click.echo(f"Error: Resume file not found: {resume}", err=True)
        sys.exit(1)

    with open(resume, "r", encoding="utf-8") as f:
        resume_text = f.read()

    # Resolve module
    registry = create_default_registry()
    module = registry.resolve("interview_prep", spec_file.kind)

    # Build plan and execute
    plan = module.plan(spec_file, {"resume_text": resume_text})

    client = ClaudeClient()
    engine = Engine(client)
    result = engine.execute(plan, spec_file, module.name)

    # Output
    combined = {"output": result.output, "meta": result.meta}
    indent = 2 if pretty else None
    json_str = json.dumps(combined, indent=indent)

    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(json_str)
        click.echo(f"Output written to {output}")
    else:
        click.echo(json_str)


@main.command()
@click.option("--spec", required=True, help="Spec path relative to specs/ directory")
@click.option("--specs-dir", default="specs", help="Base directory for spec files")
@click.option("--pretty", is_flag=True, help="Pretty-print JSON output")
def lint(spec, specs_dir, pretty):
    """Lint a spec file for quality, bias, and completeness."""
    from hiring_manager_tools.spec import load_spec
    from hiring_manager_tools.validation import validate_spec_structure
    from hiring_manager_tools.claude_client import ClaudeClient
    from hiring_manager_tools.engine import Engine
    from hiring_manager_tools.registry import create_default_registry

    # Load spec
    spec_path = os.path.join(specs_dir, f"{spec}.md")
    if not os.path.exists(spec_path):
        click.echo(f"Error: Spec file not found: {spec_path}", err=True)
        sys.exit(1)

    spec_file = load_spec(spec_path)

    # Structural validation (no API call)
    structural_issues = validate_spec_structure(spec_file)
    structural_json = [
        {"level": issue.level, "field": issue.field, "message": issue.message}
        for issue in structural_issues
    ]

    # AI-powered lint
    registry = create_default_registry()
    module = registry.resolve("spec_lint", spec_file.kind)
    plan = module.plan(spec_file, {})

    client = ClaudeClient()
    engine = Engine(client)
    result = engine.execute(plan, spec_file, module.name)

    # Combined output
    combined = {
        "structural_issues": structural_json,
        "ai_lint": result.output,
        "meta": result.meta,
    }
    indent = 2 if pretty else None
    click.echo(json.dumps(combined, indent=indent))


@main.command("list")
@click.option("--kind", default=None, help="Filter by spec kind")
@click.option("--specs-dir", default="specs", help="Base directory for spec files")
@click.option("--pretty", is_flag=True, help="Pretty-print JSON output")
def list_cmd(kind, specs_dir, pretty):
    """List available spec files."""
    from hiring_manager_tools.spec import list_specs

    specs = list_specs(specs_dir, kind=kind)
    output = []
    for s in specs:
        output.append({
            "path": s.source_path,
            "kind": s.kind,
            "role": s.metadata.get("role"),
            "team": s.metadata.get("team"),
            "version": s.version,
        })

    indent = 2 if pretty else None
    click.echo(json.dumps(output, indent=indent))


@main.command()
@click.option("--specs-dir", default="specs", help="Base directory for spec files")
@click.option("--host", default="localhost")
@click.option("--port", default=8321, type=int)
def serve(specs_dir, host, port):
    """Start the MCP server."""
    from hiring_manager_tools.mcp_server import create_mcp_server
    create_mcp_server(specs_dir).run(host=host, port=port)


@main.command()
@click.option("--host", default="localhost")
@click.option("--port", default=8000, type=int)
@click.option("--specs-dir", default="specs", help="Base directory for spec files")
def web(host, port, specs_dir):
    """Start the web demo."""
    import uvicorn

    # Set specs_dir as env var so the app can read it
    os.environ["HMT_SPECS_DIR"] = specs_dir
    uvicorn.run("hiring_manager_tools.web.app:app", host=host, port=port, reload=False)


if __name__ == "__main__":
    main()
