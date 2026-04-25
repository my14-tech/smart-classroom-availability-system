from utils.db import get_db_connection

def suggest_best_room(date, start_time, end_time):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get all rooms
    cursor.execute("SELECT * FROM classrooms")
    rooms = cursor.fetchall()

    # Get all schedules for that date
    cursor.execute("SELECT * FROM schedules WHERE date = ?", (date,))
    schedules = cursor.fetchall()

    best_room = None
    best_score = -1

    for room in rooms:
        room_id = room["id"]

        conflict = False
        usage_count = 0

        for s in schedules:
            if s["room_id"] == room_id:
                usage_count += 1

                # Check overlap
                if not (end_time <= s["start_time"] or start_time >= s["end_time"]):
                    conflict = True
                    break

        if conflict:
            continue

        # 🎯 SCORING LOGIC
        score = 100 - (usage_count * 10)

        # Prefer less used rooms
        if score > best_score:
            best_score = score
            best_room = room

    conn.close()

    if best_room:
        return {
            "room_number": best_room["room_number"],
            "message": "Best available room found",
            "reason": "Least used room with no schedule conflicts"
        }
    else:
        return {
            "message": "No rooms available"
        }