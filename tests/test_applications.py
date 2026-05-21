import requests
from server import start_server, stop_server

def test_create_application():
    payload = {
        "job_id": 1,
        "candidate_name": "John Doe",
        "email": "john@example.com",
        "resume_file_path": "/uploads/john_resume.pdf",
        "cover_letter": "I am a great fit."
    }
    response = requests.post("http://localhost:8000/api/applications/", json=payload)
    assert response.status_code == 200
    print(f"\n-- test_create_application --")
    print(f"  INPUT:  {payload}")
    print(f"  OUTPUT: {response.json()}")

    application_id = response.json()["application_id"]
    requests.delete(f"http://localhost:8000/api/applications/{application_id}")

def test_invalid_email():
    payload = {
        "job_id": 1,
        "candidate_name": "John Doe",
        "email": "notanemail",
        "resume_file_path": "/uploads/john_resume.pdf",
        "cover_letter": "I am a great fit."
    }
    response = requests.post("http://localhost:8000/api/applications/", json=payload)
    assert response.status_code == 422
    print(f"\n-- test_invalid_email --")
    print(f"  INPUT:  {payload}")
    print(f"  OUTPUT: {response.json()}")

def test_missing_candidate_name():
    payload = {
        "job_id": 1,
        "email": "john@example.com",
        "resume_file_path": "/uploads/john_resume.pdf",
        "cover_letter": "I am a great fit."
    }
    response = requests.post("http://localhost:8000/api/applications/", json=payload)
    assert response.status_code == 422
    print(f"\n-- test_missing_candidate_name --")
    print(f"  INPUT:  {payload}")
    print(f"  OUTPUT: {response.json()}")

def test_missing_job_id():
    payload = {
        "candidate_name": "John Doe",
        "email": "john@example.com",
        "resume_file_path": "/uploads/john_resume.pdf",
        "cover_letter": "I am a great fit."
    }
    response = requests.post("http://localhost:8000/api/applications/", json=payload)
    assert response.status_code == 422
    print(f"\n-- test_missing_job_id --")
    print(f"  INPUT:  {payload}")
    print(f"  OUTPUT: {response.json()}")

def test_get_application_not_found():
    response = requests.get("http://localhost:8000/api/applications/999")
    assert response.status_code == 404
    print(f"\n-- test_get_application_not_found --")
    print(f"  INPUT:  application_id=999")
    print(f"  OUTPUT: {response.json()}")

if __name__ == "__main__":
    server = start_server()
    try:
        try:
            test_create_application()
        except AssertionError:
            print("test_create_application FAILED")

        try:
            test_invalid_email()
        except AssertionError:
            print("test_invalid_email FAILED")

        try:
            test_missing_candidate_name()
        except AssertionError:
            print("test_missing_candidate_name FAILED")

        try:
            test_missing_job_id()
        except AssertionError:
            print("test_missing_job_id FAILED")

        try:
            test_get_application_not_found()
        except AssertionError:
            print("test_get_application_not_found FAILED")

        print("\nAll application tests worked and have been completed!")
    finally:
        stop_server(server)