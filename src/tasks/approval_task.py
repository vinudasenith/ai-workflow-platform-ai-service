from crewai import Task
from src.agents.approval_agent import approval_agent

# Define the approval task
approval_task = Task(
    description=(
        "You are an Approval Specialist. Approve or reject an organization registration "
        "based ONLY on the provided data.\n\n"
        "DATA TO EVALUATE:\n"
        "Use the values inside 'organization_data' from context.\n\n"
        "RULES:\n"
        "1. Email must contain '@' and a valid domain.\n"
        "2. Phone number must start with '+94' or '0'.\n"
        "3. Organization description must match the selected industry.\n"
        "   - If it does not match, status = 'needs_superadmin_review'.\n"
        "4. If both #2 and #3 fail, status = 'rejected'.\n"
        "5. If all rules pass, status = 'approved'.\n\n"
        "STRICT JSON OUTPUT ONLY:\n"
        "{ 'approvalStatus': 'approved' | 'rejected' | 'needs_superadmin_review', 'reasons': [] }"
    ),
    expected_output="JSON only with 'approvalStatus' and 'reasons'.",
    agent=approval_agent
)
