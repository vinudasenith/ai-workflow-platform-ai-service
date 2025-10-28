from crewai import Agent
from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
)

# Define the approval agent
approval_agent= Agent(
    role="Approval Specialist",
    goal="Approve or reject organization registrations based on validation results",
    backstory="Expert in business rules, compliance, and fraud detection",
    llm=llm,
    verbose=True
)