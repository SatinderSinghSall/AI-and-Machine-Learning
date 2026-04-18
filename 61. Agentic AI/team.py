from agno.agent import Agent
from agno.team import Team
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

eng_agent = Agent(name="English Agent", role="You answer questions in English")
chi_agent = Agent(name="Chinese Agent", role="You answer questions in Chinese")
hin_agent = Agent(name="Hindi Agent", role="You answer questions in Hindi")

team_leader = Team(
    name = "Answer & Translation Team",
    members = [eng_agent, chi_agent, hin_agent],
    model = Groq(id="qwen/qwen3-32b"), # llama-3.3-70b-versatile
    markdown=True,
    show_members_responses = True,
    instructions = "All member Agents must respond to answer the query in their specific language. Do NOT just call / route just a single Agent, all of them must respond to the query provided. Output the response of all Agents."
)

team_leader.print_response("What is the capital of India?", markdown=True)
