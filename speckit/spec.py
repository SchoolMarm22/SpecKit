"""SpecFile dataclass, loader, parser, and listing."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field

import yaml


@dataclass
class SpecFile:
    """A parsed spec file."""

    kind: str
    metadata: dict = field(default_factory=dict)
    body: str = ""
    sections: dict[str, str] = field(default_factory=dict)
    source_path: str | None = None
    version: int = 1

    def __post_init__(self):
        if "version" in self.metadata:
            self.version = int(self.metadata["version"])


def _split_frontmatter(raw_text: str) -> tuple[dict, str]:
    """Split YAML frontmatter from markdown body.

    Returns (metadata_dict, body_string).
    """
    raw_text = raw_text.strip()
    if not raw_text.startswith("---"):
        return {}, raw_text

    # Find the closing ---
    end = raw_text.find("---", 3)
    if end == -1:
        return {}, raw_text

    frontmatter_str = raw_text[3:end].strip()
    body = raw_text[end + 3:].strip()

    metadata = yaml.safe_load(frontmatter_str)
    if metadata is None:
        metadata = {}

    return metadata, body


def _normalize_section_key(heading: str) -> str:
    """Normalize a heading to a section key.

    '## Must-Haves' -> 'must_haves'
    '## Anti-Patterns' -> 'anti_patterns'
    """
    # Remove leading # and strip
    key = heading.lstrip("#").strip()
    # Lowercase
    key = key.lower()
    # Replace non-alphanumeric with underscore
    key = re.sub(r"[^a-z0-9]+", "_", key)
    # Strip leading/trailing underscores
    key = key.strip("_")
    return key


def _split_sections(body: str) -> dict[str, str]:
    """Split markdown body into sections by H2 headings.

    Content before the first H2 is stored under 'preamble'.
    """
    sections: dict[str, str] = {}

    # Split on lines that start with ## (but not ### or more)
    parts = re.split(r"\n(?=## (?!#))", body)

    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue

        if part.startswith("## ") and not part.startswith("### "):
            # Extract heading from first line
            lines = part.split("\n", 1)
            heading = lines[0]
            content = lines[1].strip() if len(lines) > 1 else ""
            key = _normalize_section_key(heading)
            sections[key] = content
        elif i == 0:
            # Content before first H2
            sections["preamble"] = part
        else:
            # Shouldn't happen, but store as preamble continuation
            sections["preamble"] = sections.get("preamble", "") + "\n" + part

    return sections


def load_spec(path: str) -> "SpecFile":
    """Load a spec from a file path. Parses frontmatter, splits sections."""
    with open(path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    spec = parse_spec(raw_text)
    spec.source_path = path
    return spec


def parse_spec(raw_text: str) -> "SpecFile":
    """Parse a spec from raw text (for the web demo paste-in flow).

    source_path will be None.
    """
    metadata, body = _split_frontmatter(raw_text)
    sections = _split_sections(body)

    kind = metadata.get("kind", "")
    version = int(metadata.get("version", 1))

    return SpecFile(
        kind=kind,
        metadata=metadata,
        body=body,
        sections=sections,
        source_path=None,
        version=version,
    )


def list_specs(specs_dir: str, kind: str | None = None) -> list["SpecFile"]:
    """List all specs, optionally filtered by kind."""
    specs = []

    if kind:
        kind_dir = os.path.join(specs_dir, kind)
        if os.path.isdir(kind_dir):
            for fname in sorted(os.listdir(kind_dir)):
                if fname.endswith(".md") and fname != "README.md":
                    path = os.path.join(kind_dir, fname)
                    specs.append(load_spec(path))
    else:
        for kind_name in sorted(os.listdir(specs_dir)):
            kind_dir = os.path.join(specs_dir, kind_name)
            if os.path.isdir(kind_dir):
                for fname in sorted(os.listdir(kind_dir)):
                    if fname.endswith(".md") and fname != "README.md":
                        path = os.path.join(kind_dir, fname)
                        specs.append(load_spec(path))

    return specs
