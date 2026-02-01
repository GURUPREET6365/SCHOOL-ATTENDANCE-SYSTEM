# School Attendance Manager

> **Generated with AI** - This project's Frontend and README.md file was developed with AI assistance to create a modern, efficient school attendance management system.

## 📋 About This Project

School Attendance Manager is a comprehensive web-based application designed to streamline student attendance tracking using QR code technology. The system provides an intuitive interface for generating, viewing, and managing student QR codes for attendance purposes.

### ✨ Key Features

- **🎯 QR Code Generation**: Create unique QR codes for students with their details
- **👀 QR Code Viewing**: Search and view existing QR codes by student ID
- **💾 Download Functionality**: Download QR codes as PNG files
- **🌙 Modern Dark Theme**: Beautiful, responsive dark-themed UI
- **📱 Mobile Responsive**: Works seamlessly on desktop and mobile devices
- **🔍 Student Search**: Easy search functionality by student ID
- **📊 Database Integration**: PostgreSQL database for reliable data storage

### 🏗️ Technology Stack

**Backend:**
- FastAPI (Python web framework)
- PostgreSQL (Database)
- Alembic (Database migrations)
- Pydantic (Data validation)
- QR Code generation libraries

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- Modern CSS with CSS Variables
- Responsive design
- Dark theme UI

## 🚀 Getting Started

### Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8+
- PostgreSQL
- Git

### 📥 Cloning the Repository

```bash
git clone <your-repository-url>
cd school-attendance-manager
```

### 🔧 Environment Setup

1. **Create a virtual environment:**
```bash
python -m venv venv
```

2. **Activate the virtual environment:**

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

3. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create environment file:**
Create a `.env` file in the root directory with the following variables:

```env
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/database_name
ALEMBIC_URL=postgresql+psycopg2://username:password@localhost:5432/database_name
```

**Replace the following:**
- `username`: Your PostgreSQL username
- `password`: Your PostgreSQL password  
- `localhost:5432`: Your PostgreSQL host and port
- `database_name`: Your database name

### 🗄️ Database Setup

1. **Create PostgreSQL database:**
```sql
CREATE DATABASE school_attendance_system;
```

2. **Run database migrations:**
```bash
alembic upgrade head
```

## 🖥️ Running the Application

### 🔧 Starting the Backend (FastAPI Server)

1. **Navigate to the project root directory**
2. **Activate your virtual environment** (if not already activated)
3. **Start the FastAPI server:**

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The API server will be available at: `http://127.0.0.1:8000`

**API Documentation:** `http://127.0.0.1:8000/docs`

### 🌐 Starting the Frontend

The frontend is a static web application. You can serve it using any of these methods:

**Option 1: Python HTTP Server**
```bash
cd FRONTEND
python -m http.server 5500
```

**Option 3: Live Server (VS Code Extension)**
- Install the "Live Server" extension in VS Code
- Right-click on `FRONTEND/index.html`
- Select "Open with Live Server"

The frontend will be available at: `http://localhost:3000`

## 📖 How to Use

### 1. **Generate QR Code**
- Navigate to "Generate QR" in the navigation
- Fill in student details:
  - First Name
  - Last Name
  - Email
  - Student ID
  - Standard/Grade
  - Stream or Section
- Click "Generate QR Code"
- View and download the generated QR code

### 2. **View Existing QR Code**
- Navigate to "View QR Code" in the navigation
- Enter the Student ID
- Click "View QR Code"
- Download the QR code if needed

### 3. **Download QR Codes**
- All QR codes can be downloaded as PNG files
- Files are automatically named with student information
- Format: `FirstName_LastName_QR.png` or `Student_ID_QR.png`

## 🔌 API Endpoints

### Generate QR Code
```http
POST /api/qr-gen
Content-Type: application/json

{
    "first_name": "string",
    "last_name": "string", 
    "email": "string",
    "student_id": integer,
    "standard": integer,
    "streamORsection": "string"
}
```

### View QR Code
```http
GET /api/view/QRcode/{student_id}
```

## 📁 Project Structure

```
school-attendance-manager/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── database/
│   │   ├── database.py      # Database configuration
│   │   └── models.py        # Database models
│   └── qr-code-gen.py       # QR code generation logic
├── FRONTEND/
│   ├── css/
│   │   └── styles.css       # Main stylesheet
│   ├── js/
│   │   ├── main.js          # Common JavaScript
│   │   ├── qr-generator.js  # QR generation logic
│   │   ├── qr-display.js    # QR display logic
│   │   └── view-qr.js       # QR viewing logic
│   ├── index.html           # Home page
│   ├── genqr.html          # Generate QR page
│   ├── view-qr.html        # View QR page
│   └── show-qr-page.html   # QR display page
├── alembic/                 # Database migrations
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🛠️ Development

### Adding New Features

1. **Backend changes**: Modify files in the `app/` directory
2. **Frontend changes**: Modify files in the `FRONTEND/` directory
3. **Database changes**: Create new Alembic migrations

### Database Migrations

**Create a new migration:**
```bash
alembic revision --autogenerate -m "Description of changes"
```

**Apply migrations:**
```bash
alembic upgrade head
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **AI-Assisted Development**: This project was developed with AI assistance
- **FastAPI**: For the excellent Python web framework
- **PostgreSQL**: For reliable database management
- **Modern Web Technologies**: For creating a responsive user interface

---

**Note**: This project was generated with AI assistance to demonstrate modern web development practices and efficient attendance management solutions.