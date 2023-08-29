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

# # Create the database connection
# username = os.environ.get("POSTGRES_USER")
# password = os.environ.get("POSTGRES_PASSWORD")
# localhost = os.environ.get("POSTGRES_HOST")
# dbname = os.environ.get("POSTGRES_DB")
# engine = create_engine(f'postgresql://{username}:{password}@{localhost}/{dbname}')
# Session = sessionmaker(bind=engine)
# session = Session()

# data = {"PositionLocation" : [[
#                         {
#                             "LocationName": "Wallops Island, Virginia",
#                             "CountryCode": "United States",
#                             "CountrySubDivisionCode": "Virginia",
#                             "CityName": "Wallops Island, Virginia",
#                             "Longitude": -75.47912,
#                             "Latitude": 37.844044
#                         },
#                         {
#                             "LocationName": "Boise, Idaho",
#                             "CountryCode": "United States",
#                             "CountrySubDivisionCode": "Idaho",
#                             "CityName": "Boise, Idaho",
#                             "Longitude": -116.19341,
#                             "Latitude": 43.60698
#                         }
#                     ],
#                     [{
#                             "LocationName": "Aurora, Colorado",
#                             "CountryCode": "United States",
#                             "CountrySubDivisionCode": "Colorado",
#                             "CityName": "Aurora, Colorado",
#                             "Longitude": -104.813,
#                             "Latitude": 39.7087
#                         },
#                         {
#                             "LocationName": "Watkins, Colorado",
#                             "CountryCode": "United States",
#                             "CountrySubDivisionCode": "Colorado",
#                             "CityName": "Watkins, Colorado",
#                             "Longitude": -104.6031,
#                             "Latitude": 39.738983
#                         }
#                     ]
# ]
# }
# import pandas as pd
# import json


# df = pd.DataFrame(data)
# df = df.applymap(lambda x: json.dumps(x))

# df['jobname'] = pd.Series(['Data Scientist', "Data Engineer"])
# df = df[['jobname','PositionLocation']]
# df.rename(columns={"PositionLocation":"location"}, inplace=True)

# # Create a context manager for SQLAlchemy session
# from contextlib import contextmanager


# @contextmanager
# def session_scope():
#     session = Session()
#     try:
#         yield session
#         session.commit()
#     except Exception as e:
#         session.rollback()
#         raise e
#     finally:
#         session.close()

# # Query the data using SQLAlchemy with session handling
# query = "SELECT * FROM jobs"

# with session_scope() as session:
#     df.to_sql(name="jobs", con=engine, index=False, if_exists="append")
#     queried_df = pd.read_sql_query(query, con=session.bind)

# print(queried_df)

# # Create a new user
# # new_job = Job(jobname="Data Scientist", location={"data-test":["Test1", "Test2", "Test3"]})
# # session.add(new_job)
# # session.commit()

# # jobs = session.query(Job).all()


