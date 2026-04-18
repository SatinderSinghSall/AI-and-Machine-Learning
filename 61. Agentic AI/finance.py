from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"), # llama-3.3-70b-versatile
        markdown=True,
        tools=[DuckDuckGoTools(), YFinanceTools()],
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Format your response using markdown and use tables to display data where possible."],
        add_datetime_to_context = True,
        debug_mode = True
    )

grok_agent = build_agent()

grok_agent.print_response("Share the NVDA stock price and analyst recommendations.", markdown=True)
