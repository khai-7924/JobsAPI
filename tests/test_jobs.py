import requests
from server import start_server, stop_server

def test_get_jobs():
    response = requests.get("http://localhost:8000/api/jobs/")
    assert response.status_code == 200
    print(f"-> GET /api/jobs/ works | {response.json()}")

if __name__ == "__main__":
    server = start_server()
    try:
        try:
            test_get_jobs()
        except AssertionError:
            print("-> test_get_jobs failed")

        print("\n-> All job tests done!")
    finally:
        stop_server(server)