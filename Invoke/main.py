from langchain.agents import create_agent
from dataclasses import dataclass
class WeatherTool:
    text:str
    temperature:str

@dataclass
class WeatherTool:
    text: str
    temperature: str

def get_weather(city: str) -> WeatherTool:
    """Get weather for a given city."""
    return WeatherTool(
        text=f"It's always sunny in {city}!",
        temperature="75°F"
    )

agent = create_agent(
    model="google_genai:gemini-3-flash-preview",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)