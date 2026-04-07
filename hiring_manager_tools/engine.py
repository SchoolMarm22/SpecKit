"""Engine executor — runs invocation plans against Claude."""

from hiring_manager_tools.modules.base import InvocationPlan, ModuleResult
from hiring_manager_tools.run_record import RunRecord, persist_run


class Engine:
    """Executes invocation plans against Claude.

    Does not know about specific modules — only about plans and results.
    """

    def __init__(self, client, runs_dir: str = ".hiring_manager_tools/runs"):
        self.client = client
        self.runs_dir = runs_dir

    def execute(
        self, plan: InvocationPlan, spec, module_name: str
    ) -> ModuleResult:
        """Execute a plan. Returns structured, validated output with meta block."""
        run = RunRecord.start(
            module_name=module_name,
            spec_path=spec.source_path,
            spec_version=spec.version,
            prompt_version=plan.prompt_version,
            model=self.client.model,
        )

        try:
            raw_output = self.client.invoke(
                system_prompt=plan.system_prompt,
                messages=plan.messages,
                tool_schema=plan.tool_schema,
            )

            meta = {
                "spec_version": spec.version,
                "spec_path": spec.source_path,
                "spec_kind": spec.kind,
                "prompt_version": plan.prompt_version,
                "model": self.client.model,
                "module": module_name,
                "run_id": run.run_id,
                "timestamp": run.started_at.isoformat(),
            }

            run.complete()
            self._persist_run(run)

            return ModuleResult(output=raw_output, meta=meta)

        except Exception as e:
            run.fail(str(e))
            self._persist_run(run)
            raise

    def _persist_run(self, run: RunRecord):
        """Append run record to JSONL file."""
        persist_run(run, self.runs_dir)
