# SQLAlchemy
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
    
user = os.getenv("USER")
DATABASE_URL = f"postgresql://{user}@localhost:5432/jobsdb"
if not DATABASE_URL:
    raise ValueError("DATABASE_URL Incorrect, refer to README.md")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()