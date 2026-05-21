import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

def create_database():
    user = os.getenv("USER")
    print(f"Connected to PostgreSQL as user {user}.")
    conn = psycopg2.connect(
        user=user,
        host="localhost",
        port="5432",
        database="postgres"
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'jobsdb'")
    if not cursor.fetchone():
        cursor.execute("CREATE DATABASE jobsdb")
        print("Database 'jobsdb' created!")
    else:
        print("Database 'jobsdb' already exists, skipping.")

    cursor.close()
    conn.close()

def create_tables():
    from models import Job, Application
    from db import engine, Base
    Base.metadata.create_all(bind=engine)
    print("Tables created:", list(Base.metadata.tables.keys()))

def seed_jobs():
    from models import Job
    from db import engine
    from sqlalchemy.orm import Session

    db = Session(bind=engine)

    if db.query(Job).first():
        print("Jobs already seeded, skipping.")
        db.close()
        return

    jobs = [
        Job(title="Software Engineer", department="Engineering", description="Build and maintain web applications."),
        Job(title="Product Manager", department="Product", description="Define and drive product roadmap."),
        Job(title="Data Analyst", department="Data", description="Analyze data and surface insights."),
        Job(title="UX Designer", department="Design", description="Design intuitive user experiences."),
        Job(title="DevOps Engineer", department="Engineering", description="Maintain and improve infrastructure."),
        Job(title="Marketing Specialist", department="Marketing", description="Develop and execute marketing campaigns."),
    ]

    db.add_all(jobs)
    db.commit()
    db.close()
    print("Jobs seeded!")

if __name__ == "__main__":
    create_database()
    create_tables()
    seed_jobs()