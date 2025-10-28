from journey_agents.agents import run_scored_experiment

def test_critic_outputs_score():
    msgs = run_scored_experiment(seed=42)
    critic_lines = [m.content for m in msgs if "critic" in m.sender.lower()]
    assert critic_lines, "No critic output found"
    text = critic_lines[-1].lower()
    assert "score=" in text, "No score mentioned"
    assert any(x in text for x in ["0", "1", "2", "3"]), "Score value missing"
