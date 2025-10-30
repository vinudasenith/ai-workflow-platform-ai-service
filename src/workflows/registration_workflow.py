from crewai import Crew
from src.agents.validation_agent import validation_agent
from src.agents.approval_agent import approval_agent
from src.agents.notification_agent import notification_agent
from src.agents.superadmin_notification_agent import super_admin_notification_agent

from src.tasks.validate_task import validate_task
from src.tasks.approval_task import approval_task
from src.tasks.notification_task import notification_task
from src.tasks.super_admin_notification_task import create_super_admin_notification_task


def run_registration_workflow(org_data):
    """
    Execute the complete workflow: validation → approval → notifications.
    """

    # Validation Phase
    validation_crew = Crew(
        agents=[validation_agent],
        tasks=[validate_task],
        process="sequential",
        verbose=True
    )

    validation_result = validation_crew.kickoff(inputs={"organization_data": org_data})
    print("✅ Validation Result:", validation_result)

    # Approval Phase
    approval_crew = Crew(
        agents=[approval_agent],
        tasks=[approval_task],
        process="sequential",
        verbose=True
    )

    approval_result = approval_crew.kickoff(inputs={"organization_data": org_data})
    print("✅ Approval Result:", approval_result)

    # Extract approval status safely
    approval_status = approval_result.get("approvalStatus", "unknown")

    # Notification to Organization Owner
    notification_crew = Crew(
        agents=[notification_agent],
        tasks=[notification_task],
        process="sequential",
        verbose=True
    )

    notification_result = notification_crew.kickoff(inputs={"approvalStatus": approval_status})
    print("✅ Notification Result:", notification_result)

    # Super Admin Notification (if needed)
    if approval_status == "needs_superadmin_review":
        super_admin_task = create_super_admin_notification_task(org_data)
        superadmin_crew = Crew(
            agents=[super_admin_notification_agent],
            tasks=[super_admin_task],
            process="sequential",
            verbose=True
        )
        superadmin_result = superadmin_crew.kickoff()
        print("Super Admin Notification Result:", superadmin_result)

    print("\nWorkflow Complete!")

    return {
        "validation": validation_result,
        "approval": approval_result,
        "notification": notification_result,
        "superadmin": superadmin_result
    }
