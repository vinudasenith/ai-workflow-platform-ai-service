from crewai import Task
from src.services.email_service import send_superadmin_notification

# Function to create a super admin notification task
def create_super_admin_notification_task(org_data):
    return Task(
        description=(f"Notify SuperAdmin that the following organization requires review:\n"
            f"Name: {org_data['name']}\n"
            f"Industry: {org_data['industry']}\n"
            f"Phone Number: {org_data['phoneNumber']}\n"
            f"Owner: {org_data['ownerName']}"
    ),
    expected_output="A confirmation message that email was triggered.",
        callback=lambda result: send_superadmin_notification(
            " SuperAdmin Review Required",
            f"A registration requires attention:\n\n{org_data}"
        )
)
