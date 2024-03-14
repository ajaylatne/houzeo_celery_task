from sqlalchemy import create_engine, Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace 'username', 'password', 'hostname', and 'database_name' with your MySQL credentials
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_DATABASE = os.getenv("DB_DATABASE")

# Create an engine
engine = create_engine(f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_DATABASE}')

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a simple table
class Articles(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    source = Column(JSON)
    author = Column(String(255))
    title = Column(String(255))
    description = Column(String(1000))
    url = Column(String(1000))
    urlToImage = Column(String(1000))
    publishedAt = Column(DateTime)
    content = Column(String(3000))
   
# Create the tables in the database
Base.metadata.create_all(engine)

# Create a sessionmaker

def save_data_to_db(records):
    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert data
    for record in records:
        publishedAt = record['publishedAt'][:-1:]
        final_dict = {**record, "publishedAt":publishedAt}
        new_user = Articles(**final_dict)
        session.add(new_user)
        session.commit()

    # Close the session
    session.close()
