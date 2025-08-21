{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from fastapi import FastAPI, Depends\
from sqlalchemy.orm import Session\
from . import models, schemas, crud, database\
\
models.Base.metadata.create_all(bind=database.engine)\
\
app = FastAPI()\
\
def get_db():\
    db = database.SessionLocal()\
    try:\
        yield db\
    finally:\
        db.close()\
\
@app.get("/tasks", response_model=list[schemas.Task])\
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):\
    return crud.get_tasks(db, skip=skip, limit=limit)\
\
@app.post("/tasks", response_model=schemas.Task)\
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):\
    return crud.create_task(db=db, task=task)\
\
@app.put("/tasks/\{task_id\}", response_model=schemas.Task)\
def complete_task(task_id: int, db: Session = Depends(get_db)):\
    return crud.complete_task(db=db, task_id=task_id)}