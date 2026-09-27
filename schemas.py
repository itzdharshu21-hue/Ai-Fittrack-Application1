from datetime import date
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    age: int
    height: float
    weight: float


class FitnessCreate(BaseModel):
    user_id: int
    date: date
    steps: int = 0
    calories: float = 0
    workout_minutes: int = 0
    water_liters: float = 0
    sleep_hours: float = 0
    heart_rate: int | None = None
