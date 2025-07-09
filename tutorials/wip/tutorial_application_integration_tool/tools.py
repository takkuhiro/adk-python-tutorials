import os

from dotenv import load_dotenv
from google.adk.tools.application_integration_tool.application_integration_toolset import (
    ApplicationIntegrationToolset,
)

load_dotenv()

APPLICATION_INTEGRATION_SA = os.getenv("APPLICATION_INTEGRATION_SA")
with open(APPLICATION_INTEGRATION_SA) as f:
    service_account_credentials = f.read()

# connector_tool = ApplicationIntegrationToolset(
#     project="test-project", # TODO: replace with GCP project of the connection
#     location="us-central1", #TODO: replace with location of the connection
#     connection="test-connection", #TODO: replace with connection name
#     entity_operations={"Entity_One": ["LIST","CREATE"], "Entity_Two": []},#empty list for actions means all operations on the entity are supported.
#     actions=["action1"], #TODO: replace with actions
#     service_account_credentials='{...}', # optional. Stringified json for service account key
#     tool_name_prefix="tool_prefix2",
#     tool_instructions="..."
# )

connector_tool = ApplicationIntegrationToolset(
    project="aitech-aim-ai",
    location="us-central1",
    connection="ExecuteConnection",
    entity_operations={"Entity_One": ["LIST", "CREATE"], "Entity_Two": []},
    actions=["action1"],
    service_account_json=service_account_credentials,  # json
    # tool_name_prefix="tool_prefix",
    tool_instructions="Application Integration に接続して問題を解決します",
)
