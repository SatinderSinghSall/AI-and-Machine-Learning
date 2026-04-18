from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
from rich.pretty import pprint

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"), # llama-3.3-70b-versatile
        markdown=True,
        instructions = "You are a helpful and an expert Travel agent.",
        add_datetime_to_context = True,
        db=db,
        update_memory_on_run=True,
        add_history_to_context = True,
        enable_user_memories = True
    )

grok_agent = build_agent()

user_id = "satinder@gmail.com"

grok_agent.print_response("I am Satinder Singh Sall a MCA student at KiiT University & China is one of my favorite countries. What is the capital of China?", user_id = user_id)
grok_agent.print_response("What is the best time to visit it?", user_id = user_id)
grok_agent.print_response("Who am I?", user_id = user_id)

memories = grok_agent.get_user_memories(
    user_id = user_id
)

print("Memories Database:")
pprint(memories)
