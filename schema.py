from models import workouts
from sqlalchemy import Table, Column, Integer, String

user = Table(
    "user",
    Column("id",Integer),
    Column("username", Integer, primary_key=True),
    Column("email", String(16), nullable=False),
    Column("password", String(60)),
    Column("weight", String(50)),
    Column("age",Integer),
    Column("height",Integer)
)

workouts = Table(
    'workouts',
    Column("id",Integer),
    Column("plan_name",String(50),nullable=False),
    Column("difficulty_level",String(50),nullable=False),
    Column('duration',Integer),
    Column('target_muscle_groups',String(50)),
    Column('exercises_list',String(50))
)



