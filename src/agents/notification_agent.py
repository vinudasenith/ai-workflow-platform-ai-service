from crewai import Agent
from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
)

# Define  notification agent
notification_agent=Agent(
    role="Notification specialist",
    goal="Generate clear and correct email notifications for organization owners.",
    backstory=("Responsible for creating email notifications to inform organization owners about important updates and actions required.",
    ),

    llm=llm,
    verbose=True,
    allow_delegation=True
)