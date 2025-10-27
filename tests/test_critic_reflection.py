from journey_agents.agents import run_scored_experiment

def test_critic_outputs_reflection_and_score():
    msgs = run_scored_experiment(seed=42)
    critic_lines = [m.content for m in msgs if "critic" in m.sender.lower()]
    assert critic_lines, "No critic message found"
    line = critic_lines[-1].lower()
    assert "score=" in line and "/3" in line
    assert "suggestion:" in line
