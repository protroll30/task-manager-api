{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from fastapi.testclient import TestClient\
from app.main import app\
\
client = TestClient(app)\
\
def test_create_task():\
    response = client.post("/tasks", json=\{"title": "Test task", "description": "testing"\})\
    assert response.status_code == 200\
    data = response.json()\
    assert data["title"] == "Test task"\
\
def test_get_tasks():\
    response = client.get("/tasks")\
    assert response.status_code == 200\
    assert isinstance(response.json(), list)}