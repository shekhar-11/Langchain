from langchain.agents import create_agent
from langchain.tools import tool
from tavily import TavilyClient

tavily_client = TavilyClient()

@tool(description="Get weather for a given city.")
def get_weather(city: str) -> dict:
    """Get weather for a given city."""
    return {
        "text": f"It's always sunny in {city}!",
        "temperature": "60°F"
    }

@tool(description="Convert Fahrenheit temperature to Celsius.")
def tool2(temp:str) -> str:
    x = int(temp.replace("°F", ""))
    celsius = (x - 32) * 5.0/9.0
    return f"The temperature in Celsius is {celsius:.2f}°C"




@tool(description="Get the city name from the user query.")
def tool3(query: str) -> str:
    # This is a placeholder implementation. In a real scenario, you would use NLP techniques to extract the city name.
    if "San Francisco" in query:
        return "San Francisco"
    return "Unknown City"





agent = create_agent(
    model="google_genai:gemini-3-flash-preview",
    tools=[get_weather,tool2,tool3],  # Pass the function, not the result
system_prompt = """
You MUST use tools to answer.

Steps:
1. Call get_weather with the city
2. Extract the temperature
3. Call tool2 with the temperature
4. Return final answer

Do NOT answer directly.
""",

)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco? Also, give me the temperature in Celsius."}]}
)
print(result["messages"][-1].content_blocks)