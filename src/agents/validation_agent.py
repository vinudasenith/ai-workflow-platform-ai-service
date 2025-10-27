from crewai import Agent
from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
)

# Define the validation agent
validation_agent = Agent(
    role="Registration Validation Specialist",
    goal="Validate organization registration details for correctness and safety",
    backstory="Expert in business verification and fraud detection.",
    llm=llm,
    verbose=True
)
