from sqlalchemy import Column, Integer, String, Float, Date
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)


class FitnessData(Base):
    __tablename__ = "fitness_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    steps = Column(Integer, default=0)
    calories = Column(Float, default=0)
    workout_minutes = Column(Integer, default=0)
    water_liters = Column(Float, default=0)
    sleep_hours = Column(Float, default=0)
    heart_rate = Column(Integer, nullable=True)
