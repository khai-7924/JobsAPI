# CREATE - READ - UPDATE - DELETE funcs for the API
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Job, Application
import schemas

def get_jobsDB(db: Session):
    return db.query(Job).all()

def create_applicationDB(db: Session, application_data: schemas.ApplicationCreate):
    # validate job_id exists before creating application
    if not db.query(Job).filter(Job.id == application_data.job_id).first():
        raise HTTPException(status_code=404, detail=f"Job with id {application_data.job_id} does not exist.")

    new_application = Application(
        job_id=application_data.job_id,
        candidate_name=application_data.candidate_name,
        email=application_data.email,
        resume_file_path=application_data.resume_file_path,
        cover_letter=application_data.cover_letter
    )
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application

def delete_applicationDB(db: Session, application_id: int):
    application = db.query(Application).filter(Application.application_id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(application)
    db.commit()
    return {"message": "Application deleted"}
