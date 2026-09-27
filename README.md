# FitTrack AI Backend

AI-powered backend API for FitTrack, designed to manage health and fitness data, provide personalized insights, and support intelligent fitness tracking.

## Features

- User profile management
- Fitness data storage
- Steps, calories, workout, hydration, sleep and heart-rate tracking
- AI-style personalized fitness insights
- Dashboard endpoint
- SQLite database
- FastAPI interactive documentation

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Setup

```bash
python -m venv venv
```

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

## Main Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API status |
| POST | `/users` | Create user |
| GET | `/users/{user_id}` | Get user |
| POST | `/fitness` | Add fitness data |
| GET | `/fitness/{user_id}` | Get fitness history |
| GET | `/ai/insights/{user_id}` | Get AI insights |
| GET | `/dashboard/{user_id}` | Get dashboard data |

## Example User

```json
{
  "name": "Vikash",
  "age": 19,
  "height": 170,
  "weight": 60
}
```

## Example Fitness Data

```json
{
  "user_id": 1,
  "date": "2026-09-27",
  "steps": 8500,
  "calories": 520,
  "workout_minutes": 45,
  "water_liters": 2.2,
  "sleep_hours": 7.5,
  "heart_rate": 78
}
```

## Note

The current AI module uses rule-based personalized insights. It can later be connected to an external AI/LLM service for more advanced recommendations.
