from sqlalchemy import create_engine
from sqlalchemy import insert , select , delete
from datetime import datetime
from enum import Enum
from sqlalchemy import Enum as SqlEnum
engine = create_engine('postgresql://postgres:abir2016@localhost:5432/to_do_list')
from sqlalchemy import MetaData, or_, and_ ,Table,desc, func , Column, asc,  Integer, String , ForeignKey , TIMESTAMP , CheckConstraint , DECIMAL , Text
metadata = MetaData()

class Status(Enum):
    TODO = "to do"
    DOING = "doing"
    DONE = "done"
    
# class Priority(Enum):
#     VERYIMPORTANT = "very important"
#     IMPORTANT = "important"
#     CASUAL = "casual"
    
# object = Priority()
priorety = {"VERYIMPORTANT" : "very important" , "CASUAL" : "casual" , "IMPORTANT" : "important"}
tasks = Table(
            'tasks' , metadata,
            Column('id' , Integer , primary_key=True),
            Column('subject' , String(300)),
            Column('description' , Text ),
            Column('status' , String , default=priorety["CASUAL"]),
            Column('priority' , String , default=priorety["CASUAL"])
        )
def ajouter_task( subject , description , priority):
    print(subject , description , priority)
    with engine.begin() as conn:
        stmt = insert(tasks).values([{"subject" : subject , "description" : description , "priority" : priority}])
        conn.execute(stmt)
        

def afficher_tasks():
    with engine.connect() as conn:
        stmt = select(tasks)
        return conn.execute(stmt).fetchall()

def supprimer_task( id):
    with engine.connect() as conn:
        stmt = delete(tasks).where(tasks.c.id == id)
        conn.execute(stmt)
        conn.commit()
        
def marquer_task( id):
    with engine.connect() as conn:
        stmt = "je ne sais pas encore comment le faire"
        conn.execute(stmt)
        conn.commit()
metadata.create_all(engine)