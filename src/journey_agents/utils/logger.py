# src/journey_agents/utils/logger.py
from __future__ import annotations
from pathlib import Path
import json
from typing import Any, Dict

ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(parents=True, exist_ok=True)

def append_jsonl(record: Dict[str, Any], file: Path | None = None) -> Path:
    """
    Append one JSON object per line to a .jsonl file.
    Returns the file path (default: artifacts/critic_scores.jsonl).
    """
    fp = file or ARTIFACTS / "critic_scores.jsonl"
    fp.parent.mkdir(parents=True, exist_ok=True)
    with fp.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return fp
