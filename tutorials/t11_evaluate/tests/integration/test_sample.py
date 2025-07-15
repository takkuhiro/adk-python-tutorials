from google.adk.evaluation.agent_evaluator import AgentEvaluator
import pytest

@pytest.mark.asyncio
async def test_with_single_test_file():
    """evalsetファイルを使ってエージェントを評価する"""
    await AgentEvaluator.evaluate(
        # NOTE: より階層の深いエージェントを評価対象に指定する場合
        # (e.g. main_agent.sub_agents.analytics_agent)は、
        # モジュールとして認識するために全ての階層に__init__.pyを作成する必要がある
        agent_module="my_weather_agent",
        eval_dataset_file_path_or_dir="tests/integration/fixture/weather_agent/test_files/weather_agent_evalset.test.json",
    )