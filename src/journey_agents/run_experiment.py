import argparse
from datetime import datetime, timezone
from typing import List, Dict, Any

from .agents import run_hello_experiment, run_scored_experiment, score_plan, Message
from .utils.logger import append_jsonl

def _to_dicts(messages: List[Message]) -> List[Dict[str, Any]]:
    return [{"sender": m.sender, "content": m.content} for m in messages]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="hello-multi-agent")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--log", action="store_true", help="append run record to artifacts/critic_scores.jsonl")
    args = parser.parse_args()

    if args.name == "hello-multi-agent":
        messages = run_hello_experiment(seed=args.seed)
    elif args.name == "critic-scoring":
        messages = run_scored_experiment(seed=args.seed)
    else:
        raise SystemExit(f"Unknown experiment: {args.name}")

    print("=== SCRATCHPAD TRANSCRIPT ===")
    for m in messages:
        print(f"[{m.sender}] {m.content}")

    if args.log:
        worker_text = next((m.content for m in messages if m.sender.lower() == "worker"), "")
        score, reasons = score_plan(worker_text)
        record = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "seed": args.seed,
            "experiment": args.name,
            "score": score,
            "reasons": reasons,
            "messages": _to_dicts(messages),
        }
        fp = append_jsonl(record)
        print(f"\n[logger] appended record to {fp}")

if __name__ == "__main__":
    main()
