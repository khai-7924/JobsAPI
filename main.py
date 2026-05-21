# API ENDPOINTS
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import engine, Base, SessionLocal
from models import Application
import schemas
from crud import get_jobsDB, create_applicationDB, delete_applicationDB

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/jobs/")
def get_jobs(db: Session = Depends(get_db)):
    return get_jobsDB(db)

@app.post("/api/applications/")
def create_application(application_data: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    return create_applicationDB(db, application_data)

@app.get("/api/applications/{application_id}")
def get_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(Application).filter(Application.application_id == application_id).first()
    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

#Additonal delete endpoint to clean up after tests..
@app.delete("/api/applications/{application_id}")
def delete_application(application_id: int, db: Session = Depends(get_db)):
    return delete_applicationDB(db, application_id)
