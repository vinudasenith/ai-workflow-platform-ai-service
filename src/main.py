from src.agents.validation_agent import validation_agent
from src.tasks.validate_task import validate_task

test_data = {
    "name": "TechNova",
    "industry": "IT",
    "organizationSize": "11-50",
    "ownerName": "Vinuda",
    "ownerEmail": "wrong-email",
    "ownerPassword": "12",
    "phoneNumber": "1234567890"
}

result = validation_agent.execute_task(validate_task, test_data)
print(result)
