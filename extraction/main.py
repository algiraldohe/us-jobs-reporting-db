from dotenv import load_dotenv

load_dotenv()

import sys

from application.adapters.console_app import ConsoleApp
from infrastructure.local_storage_service import LocalStorageService
print(sys.argv)
if sys.argv[1] == "--console":
    local_storage = LocalStorageService()
    console_app = ConsoleApp(local_storage)  # Dependency injection
    console_app.create_app()


elif sys.argv[1] == "--flask":
    print("Flask app not implemented")

else:
    print("Mode not found")
