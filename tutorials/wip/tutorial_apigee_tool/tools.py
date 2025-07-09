from google.adk.tools.apihub_tool.apihub_toolset import APIHubToolset
from google.adk.tools.openapi_tool.auth.auth_helpers import token_to_scheme_credential

apikey_credential_str = "YOUR_API_KEY"

auth_scheme, auth_credential = token_to_scheme_credential("apikey", "query", "apikey", apikey_credential_str)

sample_toolset_with_auth = APIHubToolset(
    name="apihub-sample-tool",
    description="Sample Tool",
    access_token="...",
    apihub_resource_name="...",
    auth_scheme=auth_scheme,
    auth_credential=auth_credential,
)
