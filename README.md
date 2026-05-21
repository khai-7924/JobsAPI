<img width="1512" height="326" alt="image" src="https://github.com/user-attachments/assets/a6d0bb7d-e868-43d6-8cb9-ce4b70445d51" />

## Get Started
1. git clone <repo>
2. pip install -r requirements.txt
3. Mac/Linux: python3 setup_db.py | Windows: python setup_db.py
4. fastapi run main.py


## Testing
"/docs" on server provides graphical interface to simplifying interacting with API

Mac/Linux:

python3 tests/test_jobs.py

python3 tests/test_applications.py

Windows:

python tests/test_jobs.py

python tests/test_applications.py

## PostgreSQL
Manually create DB:
1. psql -U $(whoami) -d postgres
2. CREATE DATABASE jobsdb

Can confirm DB Creation manually with: 
1. psql -U $(whoami) -d postgres
2. \l

Delete DB with:
1. psql -U $(whoami) -d postgres -c "DROP DATABASE jobsdb;"

Print table contents:
1. psql -U $(whoami) -d postgres
2. \c jobsdb
3.
Jobs: SELECT * FROM Jobs;

Applications: SELECT * FROM Applications;

------------------
Two tables within db: Job & Application

Models.py = structure of each table


