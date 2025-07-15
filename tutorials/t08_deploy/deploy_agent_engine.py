import os

import vertexai
from dotenv import load_dotenv
from myagent.agent import root_agent
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp

load_dotenv()

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    staging_bucket=os.getenv("GOOGLE_CLOUD_STAGING_BUCKET"),
)


def deploy_agent_engine() -> None:
    adk_app = AdkApp(agent=root_agent, enable_tracing=True)
    remote_app = agent_engines.create(
        adk_app,
        display_name=root_agent.name,
        # TODO: 以下のrequirementsにAgentが使うパッケージが全て入っているか確認する
        requirements=[
            "google-cloud-aiplatform[adk,agent_engines]",
        ],
        extra_packages=["./myagent"],
    )
    print(f"Created remote agent: {remote_app.resource_name}")


if __name__ == "__main__":
    deploy_agent_engine()
