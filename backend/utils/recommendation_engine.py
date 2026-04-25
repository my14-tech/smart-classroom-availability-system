from utils.db import get_db_connection

def suggest_best_room(date, start_time, end_time, required_capacity):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get all rooms
    cursor.execute("SELECT * FROM classrooms")
    rooms = cursor.fetchall()

    # Get schedules for that date
    cursor.execute("SELECT * FROM schedules WHERE date = ?", (date,))
    schedules = cursor.fetchall()

    best_room = None
    best_score = -1

    for room in rooms:
        room_id = room["id"]
        room_capacity = room["capacity"]

        # ❌ Skip if capacity is less
        if room_capacity < required_capacity:
            continue

        conflict = False
        usage_count = 0

        for s in schedules:
            if s["room_id"] == room_id:
                usage_count += 1

                if not (end_time <= s["start_time"] or start_time >= s["end_time"]):
                    conflict = True
                    break

        if conflict:
            continue

        # 🎯 Better scoring (closer capacity + less usage)
        capacity_score = 100 - (room_capacity - required_capacity)
        usage_score = 100 - (usage_count * 10)

        score = capacity_score + usage_score

        if score > best_score:
            best_score = score
            best_room = room

    conn.close()

    if best_room:
        return {
            "room_number": best_room["room_number"],
            "message": "Best available room found",
            "reason": f"Fits required capacity ({required_capacity}) with minimal usage"
        }
    else:
        return {
            "message": "No rooms available for given capacity"
        }