from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Groq(id="qwen/qwen3-32b"),
        markdown=True,
        add_history_to_context=True,
        enable_user_memories=True
    )

agent = build_agent()

user_id = "rahul@gmail.com"
agent.print_response("I am Rahul & I am a Data Analyst.", user_id=user_id)
agent.print_response("who am I?", user_id=user_id)

memories = agent.get_user_memories(
    user_id=user_id
)

print("MEMORIES: ")
pprint(memories)