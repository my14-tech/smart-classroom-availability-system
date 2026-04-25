# backend/utils/recommendation_engine.py

def suggest_best_room(rooms, schedules, required_capacity, date, start_time, end_time):
    available_rooms = []

    for room in rooms:
        room_id = room["id"]
        capacity = room.get("capacity", 0)

        # skip if capacity not enough
        if capacity < required_capacity:
            continue

        is_available = True

        for s in schedules:
            if s["room_id"] == room_id and s["date"] == date:
                # check time conflict
                if not (end_time <= s["start_time"] or start_time >= s["end_time"]):
                    is_available = False
                    break

        if is_available:
            available_rooms.append(room)

    # simple logic: return smallest suitable room
    if available_rooms:
        return sorted(available_rooms, key=lambda x: x["capacity"])[0]

    return None