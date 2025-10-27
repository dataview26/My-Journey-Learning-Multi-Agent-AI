from dataclasses import dataclass, field
from typing import List, Dict, Any
import random

@dataclass
class Message:
    sender: str
    content: str

@dataclass
class Agent:
    name: str
    def act(self, scratchpad: List[Message], context: Dict[str, Any]) -> Message:
        raise NotImplementedError

@dataclass
class Planner(Agent):
    def act(self, scratchpad: List[Message], context: Dict[str, Any]) -> Message:
        if not scratchpad:
            return Message(self.name, "Plan week-1 learning: 1) Set up env 2) Read basics 3) Run toy agent.")
        else:
            return Message(self.name, "Looks good. Save as experiment log and set NEXT steps.")

@dataclass
class Worker(Agent):
    rng: random.Random = field(default_factory=random.Random)
    def act(self, scratchpad: List[Message], context: Dict[str, Any]) -> Message:
        bullets = [
            "Create repo & scaffold",
            "Read intro on multi-agent systems",
            "Implement Planner→Worker toy",
            "Log results + reflection",
        ]
        self.rng.seed(context.get("seed", 0))
        pick = "\n- ".join(bullets)
        return Message(self.name, f"Week 1 plan:\n- {pick}")

# ---- Scoring helpers ----
def score_plan(text: str) -> tuple[int, list[str]]:
    """
    Return (score 0–3, reasons).
    +1 if 'plan' appears
    +1 if ≥3 bullet items
    +1 if the word 'reflection' appears
    """
    score = 0
    reasons: list[str] = []
    t = text.lower()

    if "plan" in t:
        score += 1
        reasons.append("contains 'plan'")

    lines = [ln.strip() for ln in text.splitlines()]
    bullets = [ln for ln in lines if ln.startswith("-")]
    if len(bullets) >= 3:
        score += 1
        reasons.append(f"{len(bullets)} bullet items")

    if "reflection" in t:
        score += 1
        reasons.append("mentions 'reflection'")

    return score, reasons

def make_suggestion(text: str) -> str:
    """Return a short improvement suggestion based on missing criteria."""
    t = text.lower()
    suggestions = []
    if "plan" not in t:
        suggestions.append("state the plan explicitly")
    lines = [ln.strip() for ln in text.splitlines()]
    if sum(ln.startswith("-") for ln in lines) < 3:
        suggestions.append("add at least 3 bullet steps")
    if "reflection" not in t:
        suggestions.append("include a reflection line")
    return "; ".join(suggestions) if suggestions else "looks good — keep iterating"

@dataclass
class Critic(Agent):
    def act(self, scratchpad: List[Message], context: Dict[str, Any]) -> Message:
        target_text = scratchpad[-1].content if scratchpad else ""
        score, reasons = score_plan(target_text)
        suggestion = make_suggestion(target_text)
        reason_str = "; ".join(reasons) if reasons else "no checklist items met"
        return Message(self.name, f"Critic review: score={score}/3; reasons: {reason_str}; suggestion: {suggestion}")

# ---- Runners ----
def run_hello_experiment(seed: int = 42) -> List[Message]:
    pad: List[Message] = []
    planner = Planner(name="Planner")
    worker = Worker(name="Worker")
    critic = Critic(name="Critic")
    ctx = {"seed": seed}
    pad.append(planner.act(pad, ctx))
    pad.append(worker.act(pad, ctx))
    pad.append(critic.act(pad, ctx))
    return pad

def run_scored_experiment(seed: int = 42) -> List[Message]:
    """Alias for the hello experiment that includes scoring."""
    return run_hello_experiment(seed=seed)
