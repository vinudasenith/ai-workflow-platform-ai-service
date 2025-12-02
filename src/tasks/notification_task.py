from crewai import Task
from src.agents.notification_agent import notification_agent

notification_task = Task(
    description=(
        "You are an Email Notification Agent. Your job is to generate the email content "
        "based ONLY on the provided organization approval result.\n\n"
        "IF approvalStatus = 'approved': send message → 'Your organization has been approved!'\n"
        "IF approvalStatus = 'needs_superadmin_review': send message → "
        "'Your submission is under super admin review.'\n"
        "IF approvalStatus = 'rejected': send message → 'Your submission has been rejected.'\n\n"
        "STRICT JSON OUTPUT ONLY:\n"
        "{ 'emailSubject': '', 'emailBody': '' }"
    ),
    agent=notification_agent,
    expected_output="Strict JSON only with emailSubject & emailBody fields."
)
