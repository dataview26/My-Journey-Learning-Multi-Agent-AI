\# 🧠 Critic Scoring

\*\*Date:\*\* 2025-10-27  

\*\*Seed:\*\* 42  



\## Question

Can a Critic agent assign a simple 0–3 score to the Worker's output and explain its reasoning?



\## Setup

Agents: Planner → Worker → Critic  

Checklist:  

+1 if text contains “plan”  

+1 if ≥3 bullet items  

+1 if reflection mentioned  



\## Run

```bash

$env:PYTHONPATH="src"

python -m journey\_agents.run\_experiment --name "critic-scoring" --seed 42



