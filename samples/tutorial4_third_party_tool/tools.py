from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.tools import TavilySearchResults

tavily_tool_instance = TavilySearchResults(
    max_results=5,
    search_depth="basic",  # basic or advanced
    include_answer=True,
    include_raw_content=True,
    include_images=True,
)

adk_tavily_tool = LangchainTool(tool=tavily_tool_instance)
