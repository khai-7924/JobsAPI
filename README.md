## Get Started
1. git clone <repo>
2. pip install -r requirements.txt
3. # Mac/Linux
python3 setup_db.py

# Windows
python setup_db.py
4. fastapi run main.py

## Testing
# Mac/Linux
python3 tests/test_jobs.py
python3 tests/test_applications.py
# Windows
python tests/test_jobs.py
python tests/test_applications.py
## PostgreSQL
Can confirm DB Creation manually with: 
1. psql -U $(whoami) -d postgres
2. \l

Delete DB with:
1. psql -U $(whoami) -d postgres -c "DROP DATABASE jobsdb;"

Print table contents:
1. psql -U $(whoami) -d postgres
2. \c jobsdb
3. # Jobs
SELECT * FROM Jobs
# Applications
SELECT * FROM Applications

Manually create DB:
Get to default DB with:
psql -U $(whoami) -d postgres
--> Then "CREATE DATABASE jobsdb"

Two tables within db: Job & Application
Models.py = structure of each table


