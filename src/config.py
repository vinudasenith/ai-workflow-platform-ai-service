import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SUPER_ADMIN_EMAIL = os.getenv("SUPER_ADMIN_EMAIL")
