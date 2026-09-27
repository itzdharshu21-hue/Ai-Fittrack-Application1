from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import User, FitnessData
from schemas import UserCreate, FitnessCreate
from ai import generate_insights

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FitTrack AI API",
    description="AI-powered health and fitness tracking backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to FitTrack AI API",
        "status": "running"
    }


@app.post("/users")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user = User(
        name=user_data.name,
        age=user_data.age,
        height=user_data.height,
        weight=user_data.weight
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User created successfully",
        "user_id": user.id
    }


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.post("/fitness")
def add_fitness_data(
    fitness: FitnessCreate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == fitness.user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    record = FitnessData(
        user_id=fitness.user_id,
        date=fitness.date,
        steps=fitness.steps,
        calories=fitness.calories,
        workout_minutes=fitness.workout_minutes,
        water_liters=fitness.water_liters,
        sleep_hours=fitness.sleep_hours,
        heart_rate=fitness.heart_rate
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "message": "Fitness data recorded",
        "record_id": record.id
    }


@app.get("/fitness/{user_id}")
def get_fitness_data(user_id: int, db: Session = Depends(get_db)):
    records = db.query(FitnessData).filter(
        FitnessData.user_id == user_id
    ).all()

    return records


@app.get("/ai/insights/{user_id}")
def get_ai_insights(user_id: int, db: Session = Depends(get_db)):
    latest = (
        db.query(FitnessData)
        .filter(FitnessData.user_id == user_id)
        .order_by(FitnessData.date.desc())
        .first()
    )

    if not latest:
        raise HTTPException(
            status_code=404,
            detail="No fitness data available"
        )

    return {
        "user_id": user_id,
        "date": latest.date,
        "insights": generate_insights(latest)
    }


@app.get("/dashboard/{user_id}")
def dashboard(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    latest = (
        db.query(FitnessData)
        .filter(FitnessData.user_id == user_id)
        .order_by(FitnessData.date.desc())
        .first()
    )

    if not latest:
        return {
            "user": user.name,
            "message": "No fitness data available yet"
        }

    return {
        "user": user.name,
        "profile": {
            "age": user.age,
            "height": user.height,
            "weight": user.weight
        },
        "latest_activity": {
            "date": latest.date,
            "steps": latest.steps,
            "calories": latest.calories,
            "workout_minutes": latest.workout_minutes,
            "water_liters": latest.water_liters,
            "sleep_hours": latest.sleep_hours,
            "heart_rate": latest.heart_rate
        },
        "ai_insights": generate_insights(latest)
    }
