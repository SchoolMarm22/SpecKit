"""RunRecord dataclass and JSONL persistence."""

import json
import os
import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone


@dataclass
class RunRecord:
    """Tracks a single engine execution."""

    run_id: str
    module_name: str
    spec_path: str | None
    spec_version: int
    prompt_version: str
    model: str
    started_at: datetime
    completed_at: datetime | None = None
    status: str = "running"  # "running" | "success" | "failed"
    error: str | None = None

    @classmethod
    def start(cls, **kwargs) -> "RunRecord":
        return cls(
            run_id=str(uuid.uuid4()),
            started_at=datetime.now(timezone.utc),
            **kwargs,
        )

    def complete(self):
        self.completed_at = datetime.now(timezone.utc)
        self.status = "success"

    def fail(self, error: str):
        self.completed_at = datetime.now(timezone.utc)
        self.status = "failed"
        self.error = error

    def to_json(self) -> str:
        """Serialize to JSON string for JSONL persistence."""
        data = asdict(self)
        # Convert datetime objects to ISO format strings
        for key in ("started_at", "completed_at"):
            if data[key] is not None:
                data[key] = data[key].isoformat()
        return json.dumps(data)


def persist_run(run: RunRecord, runs_dir: str = ".speckit/runs"):
    """Append run record to JSONL file organized by date."""
    os.makedirs(runs_dir, exist_ok=True)
    date_str = run.started_at.strftime("%Y-%m-%d")
    filepath = os.path.join(runs_dir, f"{date_str}.jsonl")
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(run.to_json() + "\n")
