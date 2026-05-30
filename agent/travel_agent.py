from dotenv import load_dotenv
import os

load_dotenv()

from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain_community.chat_models import ChatOpenAI

# ==================================================
# IMPORT CUSTOM TOOLS
# ==================================================

from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotels
from tools.places_tool import recommend_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget

# ==================================================
# TOOLS
# ==================================================

flight_tool = Tool(
    name="Flight Search Tool",
    func=search_flights,
    description="""
Search flights between source and destination cities.

Example:
Mumbai to Goa
Delhi to Jaipur
"""
)

hotel_tool = Tool(
    name="Hotel Recommendation Tool",
    func=recommend_hotels,
    description="""
Recommend hotels in a city.

Input example:
Goa
Mumbai
Delhi
"""
)

places_tool = Tool(
    name="Places Discovery Tool",
    func=recommend_places,
    description="""
Find tourist attractions in a city.

Input example:
Goa
Mumbai
Jaipur
"""
)

weather_tool = Tool(
    name="Weather Tool",
    func=get_weather,
    description="""
Get live weather information for a city.

Input example:
Goa
Mumbai
Delhi
"""
)

budget_tool = Tool(
    name="Budget Tool",
    func=estimate_budget,
    description="""
Estimate trip budget.

Input example:
Mumbai to Goa for 3 days
Delhi trip for 5 days
"""
)

tools = [
    flight_tool,
    hotel_tool,
    places_tool,
    weather_tool,
    budget_tool
]

# ==================================================
# MEMORY
# ==================================================

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# ==================================================
# LLM
# ==================================================

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="openai/gpt-4o-mini",
    temperature=0.7
)

# ==================================================
# AGENT
# ==================================================

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    return_intermediate_steps=True,
    memory=memory,
    agent_kwargs={
        "prefix": """
You are an Expert AI Travel Planner.

You MUST use the available tools before answering.

Trip Planning Process:

1. Search Flights
2. Recommend Hotels
3. Discover Attractions
4. Check Weather
5. Calculate Budget

IMPORTANT:

The final answer MUST contain:

✈ Flights

🏨 Hotels

🌴 Attractions

🌦 Weather

💰 Budget

Never return only a budget summary.

Always provide detailed travel recommendations based on tool outputs.

Always include information from every tool that was used.
"""
    }
)