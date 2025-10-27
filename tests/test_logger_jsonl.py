from pathlib import Path
from journey_agents.utils.logger import append_jsonl

def test_append_jsonl_writes_file(tmp_path: Path):
    fp = tmp_path / "try.jsonl"
    rec = {"ts": "2025-10-30T00:00:00Z", "score": 2, "reasons": ["contains 'plan'"]}
    out = append_jsonl(rec, file=fp)
    assert out.exists()
    data = out.read_text(encoding="utf-8").strip().splitlines()
    assert data and '"score": 2' in data[-1]
