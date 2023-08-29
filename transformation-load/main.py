import os
import sys
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Job

# ----------
import sys
from dotenv import load_dotenv
from infrastructure.database_storage_service import DatabaseStorageService
from application.adapters.console_app import ConsoleApp

load_dotenv()

if sys.argv[1] == "--console":
    database_storage_service = DatabaseStorageService()
    console_app = ConsoleApp(database_storage_service)  # Dependency injection
    console_app.create_app()

