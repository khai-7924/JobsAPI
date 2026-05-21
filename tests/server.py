import subprocess
import time
import requests

def start_server():
    server = subprocess.Popen(["fastapi", "run", "main.py"])
    time.sleep(2)
    return server

def stop_server(server):
    server.terminate()
