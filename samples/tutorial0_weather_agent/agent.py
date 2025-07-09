from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """都市名から天気を取得する

    Args:
        city (str): 天気を取得する都市名 (例: "new york")

    Returns:
        dict: ステータスと結果、またはエラーメッセージ
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "New Yorkの天気は晴れて、気温は25度です。"
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


root_agent = Agent(
    name="weather_agent",
    model="gemini-2.0-flash",
    description="都市の時刻と天気に関する質問に答えるエージェントです。",
    instruction="あなたは、都市の時刻と天気に関する質問に答えるエージェントです。",
    tools=[get_weather],
)