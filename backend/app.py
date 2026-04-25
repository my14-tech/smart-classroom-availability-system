from flask import Flask
from flask_cors import CORS
from config import Config
from routes.ai_routes import ai_bp

# ✅ CREATE APP FIRST
app = Flask(__name__)
app.config.from_object(Config)

# ✅ APPLY CORS (VERY IMPORTANT - BEFORE ROUTES)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

# 🔽 IMPORT ROUTES AFTER CORS
from routes.auth_routes import auth_bp
from routes.classroom_routes import classroom_bp
from routes.schedule_routes import schedule_bp
from routes.availability_routes import availability_bp

# 🔽 IMPORT DB
from utils.db import get_db_connection


# ✅ INITIALIZE DATABASE
def init_db():
    conn = get_db_connection()
    with open("database/schema.sql") as f:
        conn.executescript(f.read())
    conn.close()
    print("✅ Database initialized successfully")


# ✅ CREATE TEST USER
from werkzeug.security import generate_password_hash

def create_test_user():
    conn = get_db_connection()
    cursor = conn.cursor()

    password = generate_password_hash("1234")

    # ✅ Insert admin separately
    try:
        cursor.execute("""
            INSERT INTO users (username, password_hash, role)
            VALUES (?, ?, ?)
        """, ("admin", password, "admin"))
        print("✅ Admin created")
    except:
        print("⚠️ Admin already exists")

    # ✅ Insert faculty separately
    try:
        cursor.execute("""
            INSERT INTO users (username, password_hash, role)
            VALUES (?, ?, ?)
        """, ("faculty1", password, "faculty"))
        print("✅ Faculty created")
    except:
        print("⚠️ Faculty already exists")

    conn.commit()
    conn.close()


# 🔽 CALL INIT FUNCTIONS
init_db()
create_test_user()


# ✅ DEBUG ROUTE (OPTIONAL)
@app.route('/check-users')
def check_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return {"users": [dict(u) for u in users]}


# ✅ REGISTER BLUEPRINTS
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(classroom_bp, url_prefix='/classroom')
app.register_blueprint(schedule_bp, url_prefix='/schedule')
app.register_blueprint(availability_bp, url_prefix='/availability')
app.register_blueprint(ai_bp, url_prefix='/ai')


# ✅ DEFAULT ROUTE
@app.route('/')
def index():
    return {
        "status": "success",
        "message": "🚀 Classroom Availability & Scheduling System API is running"
    }


# ✅ RUN APP
if __name__ == '__main__':
    app.run(debug=True, port=5001)