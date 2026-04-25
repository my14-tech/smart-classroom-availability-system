# backend/controllers/ai_controller.py

from utils.db import get_db_connection
from utils.recommendation_engine import suggest_best_room

def get_room_suggestion(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    # get all rooms
    cursor.execute("SELECT * FROM classrooms")
    rooms = [dict(r) for r in cursor.fetchall()]

    # get schedules
    cursor.execute("SELECT * FROM schedules")
    schedules = [dict(s) for s in cursor.fetchall()]

    conn.close()

    best_room = suggest_best_room(
        rooms,
        schedules,
        int(data["capacity"]),
        data["date"],
        data["start_time"],
        data["end_time"]
    )

    if best_room:
        return {
            "status": "success",
            "room": best_room
        }, 200
    else:
        return {
            "status": "error",
            "message": "No suitable room available"
        }, 404