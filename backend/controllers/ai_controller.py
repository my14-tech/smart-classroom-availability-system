# backend/controllers/ai_controller.py

from utils.recommendation_engine import suggest_best_room

def get_room_suggestion(data):
    try:
        print("Incoming AI request:", data)  # ✅ debug

        result = suggest_best_room(
            data["date"],
            data["start_time"],
            data["end_time"]
        )

        if "room_number" in result:
            return {
                "status": "success",
                "room": result
            }, 200
        else:
            return {
                "status": "error",
                "message": result["message"]
            }, 404

    except Exception as e:
        print("AI ERROR:", e)  # ✅ important
        return {
            "status": "error",
            "message": str(e)
        }, 500