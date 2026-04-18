from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"), # llama-3.3-70b-versatile
        markdown=True,
        tools = [DuckDuckGoTools()],
        instructions = "You are a helpful and an expert Travel agent.",
        add_datetime_to_context = True
    )

grok_agent = build_agent()

grok_agent.print_response("Is it safe to fly UAE, today?")
