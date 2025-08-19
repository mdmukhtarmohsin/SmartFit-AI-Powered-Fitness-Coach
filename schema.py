from models import excercise, nutrition, progress, workouts
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from datetime import date

user = Table(
    "user",
    Column("id",Integer,primary_key=True),
    Column("username", Integer, primary_key=True),
    Column("email", String(16), nullable=False),
    Column("password", String(60)),
    Column("weight", String(50)),
    Column("age",Integer),
    Column("height",Integer)
)

workouts = Table(
    'workouts',
    Column("id",Integer,primary_key=True),
    Column("plan_name",String(50),nullable=False),
    Column("difficulty_level",String(50),nullable=False),
    Column('duration',Integer),
    Column('target_muscle_groups',String(50)),
    Column('exercises_list',String(50))
)


excercise = Table(
    'excercise',
    Column("id",Integer,primary_key=True),
    Column('exercise_name',String(50),nullable=False),
    Column("category",String(50)),
    Column("equipment_needed",String(50)),
    Column('difficulty',String(50)),
    Column('instructions',String(50)),
    Column('target_muscles',String(50))
)

progress = Table(
    'progress',
    Column('user_id',ForeignKey('user.id')),
    Column("workout_id",ForeignKey('workouts.id')),
    Column("date",date),
    Column('exercises_completed',String(50)),
    Column("sets",Integer),
    Column("reps",Integer),
    Column("weights",String(50)),
    Column("duration",Integer),
    Column("calories_burned",Integer)
)

nutrition = Table(
    'nutrition',
    Column("id",Integer,primary_key=True),
    Column("user_id",ForeignKey('user.id')),
    Column("date",date),
    Column("meals",String(50)),
    Column("calories",Integer),
    Column("macros",String(50))
)