import os


from sqlalchemy.ext.asyncio import async_session,create_async_engine
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG=os.getenv('DB_CONFIG')
