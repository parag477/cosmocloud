from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
database_name = "student_management"
student_collection = "students"

# MongoDB Connection
client = AsyncIOMotorClient(MONGODB_URL)
database = client[database_name]
student_collection = database[student_collection]
