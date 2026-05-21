#Structure for the database tables
from db import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
import datetime

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    department = Column(String)
    description = Column(Text)

class Application(Base):
    __tablename__ = "applications"
    application_id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id")) # references the id of the job in the jobs table
    candidate_name = Column(String)
    email = Column(String)
    resume_file_path = Column(String)
    cover_letter = Column(Text)
    submitted_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc)) # automatically set to the current date and time when created
