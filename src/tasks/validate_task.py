from crewai import Task

# Define the validation task
validate_task= Task(
    description=(
        "Validate the organization regsitratition data. Ensure field like name , industry, organization size ,ownerName , ownerPassword, and  phoneNumber meet the required criteria." 
        "Return ONLY Valid or Invalid status with reasons."

    ),
    expected_output="Strict JSON only.",
)

