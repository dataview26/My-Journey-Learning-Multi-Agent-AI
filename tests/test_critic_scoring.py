from journey_agents.agents import run_scored_experiment

def test_critic_outputs_score():
    msgs = run_scored_experiment(seed=42)
    critic_msgs = [m.content.lower() for m in msgs if "critic" in m.sender.lower()]
    assert any("score=" in c for c in critic_msgs)
