# Hello Multi-Agent

**Date:** 2025-10-26  
**Seed:** 42  

## Question
Can two basic agents coordinate via message-passing to create a weekly learning plan?

## Setup
Planner + Worker, shared scratchpad, 3 turns.

## Run
\$env:PYTHONPATH="src"; python -m journey_agents.run_experiment --name "hello-multi-agent"\

## Results
Planner proposed steps  Worker produced plan  Planner approved.

## Reflection
 Coordination works.  
Next: add a Critic agent to review results.
