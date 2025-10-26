# Critic Agent Evaluation

**Date:** 2025-10-27  
**Seed:** 42  

## Question
Can a Critic agent evaluate the Planner and Worker’s output and provide constructive feedback?

## Setup
Agents: Planner, Worker, Critic  
Goal: assess if the Critic improves overall reasoning.

## Run
$env:PYTHONPATH="src"; python -m journey_agents.run_experiment --name "hello-multi-agent"

## Results
(Write what happened)

## Reflection
What worked? What didn’t? How did the Critic’s input help?

## Next
Add a simple score (e.g., 0–2) and checklist for the Critic to judge quality.
