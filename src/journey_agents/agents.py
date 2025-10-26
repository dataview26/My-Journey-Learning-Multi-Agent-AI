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

def run_hello_experiment(seed: int = 42) -> List[Message]:
    pad: List[Message] = []
    planner = Planner(name="Planner")
    worker = Worker(name="Worker")
    ctx = {"seed": seed}
    for turn in range(3):
        if turn % 2 == 0:
            pad.append(planner.act(pad, ctx))
        else:
            pad.append(worker.act(pad, ctx))
    return pad
