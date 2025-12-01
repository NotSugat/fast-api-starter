import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SECRET_KEY = os.getenv(
    "SECRET_KEY", "09027e5d4c40783326cef1ee95c179c7dcaa4c92e90844c1c1958b027546d240"
)
REFRESH_SECRET_KEY = os.getenv(
    "REFRESH_SECRET_KEY",
    "b92bb176d0c75d87efce31a3f4c472b3648d6e63d4b6a349802f712ba4422489",
)
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "10080")
)  # 7 days
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))


# Set up basic logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
