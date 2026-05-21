from pydantic import BaseModel, EmailStr
from datetime import datetime

class ApplicationCreate(BaseModel):
    job_id: int
    candidate_name: str
    email: EmailStr # pydantic EmailStr type handles email validation
    resume_file_path: str
    cover_letter: str
