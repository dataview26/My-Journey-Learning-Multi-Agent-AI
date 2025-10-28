import json
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

LOG_FILE = Path("artifacts/critic_scores.jsonl")
OUT_FILE = Path("artifacts/critic_scores.png")

def load_jsonl(fp: Path):
    """Read all JSON objects from a .jsonl file."""
    records = []
    if not fp.exists():
        print(f"[!] No log file found at {fp}")
        return records
    with fp.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records

def plot_scores(records):
    if not records:
        print("[!] No data to plot.")
        return

    # Sort by timestamp
    records.sort(key=lambda r: r["ts"])

    times = [datetime.fromisoformat(r["ts"].replace("Z", "+00:00")) for r in records]
    scores = [r["score"] for r in records]

    plt.figure(figsize=(8, 4))
    plt.plot(times, scores, marker="o", color="#007acc", linewidth=2)
    plt.title("Critic Scores Over Time", fontsize=14, pad=10)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Score (0–3)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.ylim(-0.1, 3.1)
    plt.tight_layout()

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUT_FILE)
    print(f"[+] Saved chart to {OUT_FILE}")

def summarize(records):
    if not records:
        print("[!] No records to summarize.")
        return
    scores = [r["score"] for r in records]
    avg = sum(scores) / len(scores)
    print(f"📊 Total runs: {len(scores)} | Avg score: {avg:.2f}/3")
    print(f"🆙 Best score: {max(scores)} | 🔽 Lowest: {min(scores)}")

def main():
    records = load_jsonl(LOG_FILE)
    summarize(records)
    plot_scores(records)

if __name__ == "__main__":
    main()
