def generate_insights(data):
    insights = []

    if data.steps < 5000:
        insights.append(
            "Your daily activity is relatively low. "
            "Consider adding a short walk or light activity."
        )
    else:
        insights.append("Good job maintaining your daily activity.")

    if data.sleep_hours < 7:
        insights.append(
            "Your sleep duration is below 7 hours. "
            "Try to maintain a consistent sleep schedule."
        )

    if data.water_liters < 2:
        insights.append(
            "Your recorded water intake is below 2 liters. "
            "Remember that hydration needs vary between people."
        )

    if data.workout_minutes < 30:
        insights.append(
            "You could gradually increase your workout duration "
            "if that fits your routine."
        )
    else:
        insights.append("You maintained a solid workout duration today.")

    return insights
