import os

import motor.motor_asyncio
from dotenv import load_dotenv
load_dotenv(".env")


root = os.environ.get("MONGO_USER")
password = os.environ.get("MONGO_PASS")

MONGODB_URL = 'mongodb://root:pass@mongodb'
# client = MongoClient("mongodb://user_name:user_password@SERVER_IP/prod-db")
# db = client['prod-db'

client =  motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
# MongoClient("mongodb://userName:password@<mongodb cointaner name or ip>/sampledb")
# connect to database python_db
database = client.mydb



# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# # MYSQL Series
# # SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/todoapp"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# # MYSQL Series
# # engine = create_engine(
# #     SQLALCHEMY_DATABASE_URL
# # )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base = declarative_base()