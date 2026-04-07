"""FastAPI web demo for Hiring Manager Tools."""

import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Hiring Manager Tools Demo")


def _check_api_key():
    """Raise a clear error if ANTHROPIC_API_KEY is not set."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise HTTPException(
            status_code=503,
            detail={
                "message": "ANTHROPIC_API_KEY not set. Export it in your environment before starting the server.",
            },
        )


class PrepRequest(BaseModel):
    spec_text: str
    resume_text: str


class LintRequest(BaseModel):
    spec_text: str


@app.get("/")
async def index():
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    return FileResponse(os.path.join(static_dir, "index.html"))


@app.post("/api/prep")
async def prep(request: PrepRequest):
    """Generate interview prep from pasted spec + resume text."""
    from hiring_manager_tools.spec import parse_spec
    from hiring_manager_tools.validation import validate_spec_structure
    from hiring_manager_tools.claude_client import ClaudeClient
    from hiring_manager_tools.engine import Engine
    from hiring_manager_tools.registry import create_default_registry

    _check_api_key()

    spec = parse_spec(request.spec_text)

    # Validate
    issues = validate_spec_structure(spec)
    errors = [i for i in issues if i.level == "error"]
    if errors:
        raise HTTPException(
            status_code=422,
            detail={
                "message": "Spec validation failed",
                "issues": [
                    {"level": e.level, "field": e.field, "message": e.message}
                    for e in errors
                ],
            },
        )

    registry = create_default_registry()
    module = registry.resolve("interview_prep", spec.kind)
    plan = module.plan(spec, {"resume_text": request.resume_text})

    client = ClaudeClient()
    engine = Engine(client)
    result = engine.execute(plan, spec, module.name)

    return {"output": result.output, "meta": result.meta}


@app.post("/api/lint")
async def lint(request: LintRequest):
    """Lint a pasted spec."""
    from hiring_manager_tools.spec import parse_spec
    from hiring_manager_tools.validation import validate_spec_structure
    from hiring_manager_tools.claude_client import ClaudeClient
    from hiring_manager_tools.engine import Engine
    from hiring_manager_tools.registry import create_default_registry

    _check_api_key()

    spec = parse_spec(request.spec_text)

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

    return {
        "structural_issues": structural_json,
        "ai_lint": result.output,
        "meta": result.meta,
    }
