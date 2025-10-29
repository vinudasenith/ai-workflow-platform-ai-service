import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

AGENT_EMAIL = os.getenv("AGENT_EMAIL")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SUPERADMIN_EMAIL = os.getenv("SUPERADMIN_EMAIL")

# Function to send email notification to superadmin
def send_superadmin_notification(subject: str, message: str):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = AGENT_EMAIL
        msg["To"] = SUPERADMIN_EMAIL

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(AGENT_EMAIL, EMAIL_PASS)
            server.sendmail(AGENT_EMAIL, SUPERADMIN_EMAIL, msg.as_string())

        return True, "Email sent successfully"
    except Exception as e:
        return False, str(e)