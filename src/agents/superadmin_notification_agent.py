from crewai import Agent
from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
)

super_admin_notification_agent = Agent(
    role="Superadmin Notification Agent",
    goal="Send email notification to superadmin whenever a registration require review",
    backstory="Responsible for notifying superadmins about registrations that need their attention",
    llm=llm,
    verbose=True
)