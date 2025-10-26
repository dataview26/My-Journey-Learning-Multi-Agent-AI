from journey_agents.agents import run_hello_experiment

def test_import_and_run():
    msgs = run_hello_experiment(seed=42)
    assert len(msgs) == 3
    assert msgs[0].sender == "Planner"
