{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from sqlalchemy.orm import Session\
from . import models, schemas\
\
def get_tasks(db: Session, skip: int = 0, limit: int = 100):\
    return db.query(models.Task).offset(skip).limit(limit).all()\
\
def create_task(db: Session, task: schemas.TaskCreate):\
    db_task = models.Task(title=task.title, description=task.description)\
    db.add(db_task)\
    db.commit()\
    db.refresh(db_task)\
    return db_task\
\
def complete_task(db: Session, task_id: int):\
    task = db.query(models.Task).filter(models.Task.id == task_id).first()\
    if task:\
        task.completed = True\
        db.commit()\
        db.refresh(task)\
    return task}