# 📚 Smart Classroom Availability System

A full-stack web application to manage classrooms, schedules, and availability with role-based access (Admin & Faculty).

---

## 🚀 Features

- 🔐 User Authentication (Admin & Faculty)
- 🏫 Classroom Management (Add, View, Delete)
- 📅 Schedule Management with Conflict Detection
- ⏱️ Real-time Room Availability Check
- 👨‍🏫 Faculty-specific dashboard (limited access)
- 💾 Persistent storage using MySQL
- 🌐 Frontend-Backend Integration using REST APIs

---

## 🛠 Tech Stack

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python (Flask)

Database:
- MySQL

---

## 📁 Project Structure
```
SE PROJECT/
├── backend/                 
│   ├── app.py              
│   ├── config.py           
│   ├── requirements.txt    
│   ├── controllers/        
│   ├── models/            
│   ├── routes/            
│   ├── utils/             
│   └── database/          
├── frontend/               
│   ├── index.html         
│   ├── dashboard.html     
│   ├── style.css          
│   └── js/                
      
```

## 🔑 Default Credentials
- **Admin**: username: `admin`, password: `admin`
- **Faculty**: username: `faculty1`, password: `faculty1`

## 🛠 Troubleshooting

### MySQL Connection Issues
1. Make sure MySQL service is running
2. Check if the user credentials in `.env` match what you created
3. Try connecting manually: `mysql -u classroom_user -p` (password: classroom123)

### Port Already in Use
If port 5000 is busy:
1. Kill the process: `netstat -ano | findstr :5000`
2. Or change the port in `backend/app.py`

### Python Import Errors
1. Make sure you're in the virtual environment
2. Install missing packages: `pip install -r backend/requirements.txt`

## 📊 Features
- ✅ User authentication (admin/faculty)
- ✅ Classroom management
- ✅ Schedule creation with conflict detection
- ✅ Availability checking
- ✅ Permanent data storage with MySQL
- ✅ Responsive web interface

## 🎯 What's Working Now
- All CRUD operations for classrooms and schedules
- User authentication
- Conflict detection for overlapping schedules
- Data persistence across server restarts
- Complete frontend-backend integration

Your classroom scheduling system is now fully functional with permanent data storage! 🎉
   FLUSH PRIVILEGES;
   EXIT;
   ```

4. **Update `.env` file:**
   ```env
   DB_USER=classroom_user
   DB_PASSWORD=classroom123
   ```

5. **Test and setup:**
   ```bash
   python test_connection.py
   python setup_database.py
   ```

## Quick Start

1. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Configure MySQL:**
   - Edit `backend/.env` with your MySQL credentials
   - Test connection: `python test_connection.py`

3. **Setup database:**
   ```bash
   python setup_database.py
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open frontend:**
   - Open `frontend/index.html` in browser

## Default Login Credentials

- **Admin:** username: `admin`, password: `admin`
- **Faculty:** username: `faculty1`, password: `faculty1`

## Installation

1. **Clone or download the project**
   ```bash
   cd backend
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MySQL Database**

   Copy the environment template:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` file with your MySQL settings:
   ```env
   DB_HOST=localhost
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=classroom_scheduler
   DB_PORT=3306
   ```

4. **Setup Database**

   Run the database setup script:
   ```bash
   python setup_database.py
   ```

   This will:
   - Create the `classroom_scheduler` database
   - Create all necessary tables
   - Insert default users

## Running the Application

1. **Start the Flask backend:**
   ```bash
   python app.py
   ```

2. **Open the frontend:**
   - Open `frontend/index.html` in your web browser
   - Or serve the frontend files with a web server

