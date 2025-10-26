import argparse
from .agents import run_hello_experiment, run_scored_experiment

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="hello-multi-agent")
    parser.add_argument("--seed", type=int, default=42)
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

if __name__ == "__main__":
    main()
