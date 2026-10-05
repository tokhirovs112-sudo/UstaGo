from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    html_path = os.path.join("templates", "index.html")
    with open(html_path, "r", encoding="utf-8") as file:
        return file.read()

@app.get("/technicians")
def get_technicians():
    return [
        ["Azizbek (Mebelchi)", "4.9", 120, "1.2 km"],
        ["Sardor (Santexnik)", "4.8", 85, "2.5 km"],
        ["Jasur (Elektrik)", "4.7", 42, "0.8 km"],
        ["Bobur (Texnika ustasi)", "5.0", 210, "3.1 km"]
    ]
