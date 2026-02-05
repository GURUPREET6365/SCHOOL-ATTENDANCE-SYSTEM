# School Attendance Manager

> **Generated with AI** - This project's Frontend and README.md file was developed with AI assistance to create a modern, efficient school attendance management system.

## 📋 About This Project

School Attendance Manager is a comprehensive web-based application designed to streamline student attendance tracking using QR code technology. The system provides an intuitive interface for generating, viewing, scanning, and managing student QR codes for real-time attendance marking with audio feedback.

### ✨ Key Features

- **🎯 QR Code Generation**: Create unique QR codes for students with their details
- **📱 Real-Time QR Scanner**: Live camera-based QR code scanning with continuous operation
- **🔊 Audio Feedback**: Voice announcements for entry/exit confirmations
- **👀 QR Code Viewing**: Search and view existing QR codes by student ID
- **📲 Mobile QR Display**: Generate shareable QR code URLs for mobile access
- **💾 Download Functionality**: Download QR codes as PNG files
- **📷 Multi-Camera Support**: Choose between front and rear cameras
- **⏱️ Auto-Continue Scanning**: Seamless continuous scanning with 4-second cooldown
- **🌙 Modern Dark Theme**: Beautiful, responsive dark-themed UI
- **📱 Mobile Responsive**: Optimized for desktop, tablet, and mobile devices
- **🔍 Student Search**: Easy search functionality by student ID
- **📊 Database Integration**: PostgreSQL database for reliable data storage
- **🎵 Sound Effects**: Professional voice announcements for attendance actions

### 🏗️ Technology Stack

**Backend:**
- FastAPI (Python web framework)
- PostgreSQL (Database)
- Alembic (Database migrations)
- Pydantic (Data validation)
- QR Code generation libraries
- SQLAlchemy (ORM)

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- ZXing Library (QR code scanning)
- Modern CSS with CSS Variables
- Responsive design
- Dark theme UI
- Web Audio API

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
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Note:** Using `0.0.0.0` allows access from other devices on your network (useful for mobile scanning)

The API server will be available at:
- **Local:** `http://127.0.0.1:8000`
- **Network:** `http://your-ip-address:8000`

**API Documentation:** `http://127.0.0.1:8000/docs`

### 🌐 Accessing the Application

The application includes multiple interfaces accessible directly through the FastAPI server:

- **Home Page (QR URL Generator):** `http://127.0.0.1:8000/`
- **QR Scanner:** `http://127.0.0.1:8000/scanner`
- **Frontend Pages:** Serve the `FRONTEND/` directory separately (see below)

### 📱 Serving Frontend Pages (Optional)

For the full frontend experience with navigation:

**Option 1: Python HTTP Server**
```bash
cd FRONTEND
python -m http.server 5500
```

**Option 2: Live Server (VS Code Extension)**
- Install the "Live Server" extension in VS Code
- Right-click on `FRONTEND/index.html`
- Select "Open with Live Server"

The frontend will be available at: `http://localhost:5500`

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

### 3. **Generate QR URL for Mobile Access**
- Visit the home page: `http://your-server-ip:8000/`
- Enter a Student ID
- Click "Show QR Code"
- The QR code will be displayed in full screen
- Share the URL `http://your-server-ip:8000/qrs/{student_id}.png` for direct access

### 4. **Scan QR Codes for Attendance**
- Visit the scanner page: `http://your-server-ip:8000/scanner`
- Select your preferred camera (front or rear)
- Click "Start Scanning"
- Point the camera at a student's QR code
- **Audio Feedback:**
  - 🔊 "You may now enter" - Entry marked
  - 🔊 "You may now exit" - Exit marked
  - 🔊 "Access denied" - Invalid QR code
- View attendance details on screen
- Scanner automatically continues after 4 seconds
- Scan the next student's QR code

### 5. **Download QR Codes**
- All QR codes can be downloaded as PNG files
- Files are automatically named with student information
- Format: `FirstName_LastName_QR.png` or `Student_ID_QR.png`

## 🎯 Scanner Features

### 📷 Camera Selection
- **Auto-Detection**: Automatically detects all available cameras
- **Smart Labeling**: Identifies front (🤳) and rear (📷) cameras
- **Quick Switch**: Toggle between cameras with one click
- **Default Selection**: Automatically selects rear camera for optimal scanning

### 🔊 Audio Feedback
- **Entry Confirmation**: "You may now enter" voice announcement
- **Exit Confirmation**: "You may now exit" voice announcement
- **Error Alert**: "Access denied" for invalid QR codes
- **Automatic Playback**: No configuration needed
- **Mobile Compatible**: Works on all devices

### ⏱️ Continuous Scanning
- **Auto-Continue**: Automatically resumes scanning after 4 seconds
- **Cooldown Period**: Prevents duplicate scans
- **Full-Screen Results**: Shows attendance details without scrolling
- **Visual Timer**: Progress bar shows time until next scan
- **Manual Continue**: Skip timer with "Continue Scanning" button

### 📱 Mobile Optimization
- **Large Scanning Area**: Optimized square camera view
- **Big Scanning Frame**: 280px square overlay for easy targeting
- **Full-Screen Results**: No scrolling needed on mobile
- **Touch-Friendly**: Large buttons and clear interface
- **Responsive Design**: Works on all screen sizes

## 🔌 API Endpoints

### Home Page (QR URL Generator)
```http
GET /
Returns: HTML page for generating QR code URLs
```

### QR Scanner Page
```http
GET /scanner
Returns: HTML page with live QR code scanner
```

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

Returns: PNG image of generated QR code
```

### View QR Code
```http
GET /api/view/QRcode/{student_id}
Returns: PNG image of student's QR code
```

### Get QR Code Image (Direct Access)
```http
GET /qrs/{student_id}.png
Returns: PNG image for mobile/direct access
```

### Mark Attendance
```http
GET /api/mark/attendance/{qr_secret}
Returns: JSON with attendance details

Response:
{
    "success": boolean,
    "entry": boolean (if entry marked),
    "exit": boolean (if exit marked),
    "id": integer,
    "name": "string",
    "entry_time": "HH:MM:SS",
    "exit_time": "HH:MM:SS" or null
}
```

### Audio Files
```http
GET /sounds/you_may_now_enter.mp3
GET /sounds/you_may_now_exit.mp3
GET /sounds/access_granted.mp3
GET /sounds/access_denied.mp3
```

## 📁 Project Structure

```
school-attendance-manager/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── QRgen.py             # QR code generation logic
│   ├── QRreader.py          # QR code reading logic
│   ├── database/
│   │   ├── database.py      # Database configuration
│   │   ├── models.py        # Database models
│   │   └── pydantic_model.py # Pydantic schemas
│   ├── templates/
│   │   ├── home.html        # QR URL generator page
│   │   └── scanner.html     # QR scanner page
│   ├── sounds/              # Audio feedback files
│   │   ├── you_may_now_enter.mp3
│   │   ├── you_may_now_exit.mp3
│   │   ├── access_granted.mp3
│   │   └── access_denied.mp3
│   └── StudentQRcode/       # Generated QR code storage
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
│   ├── versions/            # Migration files
│   └── env.py              # Alembic configuration
├── .env                     # Environment variables
├── .gitignore              # Git ignore rules
├── requirements.txt         # Python dependencies
├── alembic.ini             # Alembic configuration
└── README.md               # This file
```

## 🛠️ Development

### Adding New Features

1. **Backend changes**: Modify files in the `app/` directory
2. **Frontend changes**: Modify files in the `FRONTEND/` directory
3. **Database changes**: Create new Alembic migrations
4. **Templates**: Add new HTML templates in `app/templates/`
5. **Audio files**: Add new sounds in `app/sounds/`

### Database Migrations

**Create a new migration:**
```bash
alembic revision --autogenerate -m "Description of changes"
```

**Apply migrations:**
```bash
alembic upgrade head
```

**Rollback migration:**
```bash
alembic downgrade -1
```

## 🔒 Security Notes

- QR codes are stored locally in `app/StudentQRcode/` (excluded from git)
- Each student has a unique secret token for attendance marking
- Database credentials should be kept secure in `.env` file
- Use HTTPS in production for secure communication
- Audio files are served as static files (no authentication required)

## 📱 Mobile Access

### For Students (QR Code Display)
1. Generate QR code for student
2. Share URL: `http://your-server-ip:8000/qrs/{student_id}.png`
3. Student can access their QR code from any device
4. No app installation required

### For Attendance Marking (Scanner)
1. Access scanner: `http://your-server-ip:8000/scanner`
2. Works on any device with a camera
3. Optimized for mobile phones and tablets
4. Real-time audio feedback
5. Continuous scanning mode

## 🎵 Audio Feedback System

The system includes professional voice announcements:

- **Entry**: "You may now enter" - Played when student marks entry
- **Exit**: "You may now exit" - Played when student marks exit  
- **Access Granted**: Success confirmation sound
- **Access Denied**: Error/invalid QR code alert

**Audio Features:**
- Automatic playback (no configuration needed)
- Maximum volume for clear announcements
- Mobile browser compatible
- Retry mechanism for reliability
- Preloaded for instant playback

## 🌐 Network Access

To access the scanner from mobile devices on the same network:

1. Find your computer's IP address:
   - **Windows**: `ipconfig`
   - **macOS/Linux**: `ifconfig` or `ip addr`

2. Start server with network access:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. Access from mobile:
   - Scanner: `http://your-ip:8000/scanner`
   - QR Display: `http://your-ip:8000/qrs/{student_id}.png`

## 🐛 Troubleshooting

### Audio Not Playing
- Click "Start Scanning" button first (unlocks audio on mobile)
- Check device volume settings
- Ensure browser has audio permissions
- Try refreshing the page

### Camera Not Working
- Grant camera permissions when prompted
- Check if camera is being used by another application
- Try switching between front/rear cameras
- Refresh the page and try again

### QR Code Not Scanning
- Ensure good lighting conditions
- Hold QR code steady in the scanning frame
- Try adjusting distance from camera
- Clean camera lens if blurry

### Database Connection Issues
- Verify PostgreSQL is running
- Check `.env` file credentials
- Ensure database exists
- Run migrations: `alembic upgrade head`

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
- **ZXing**: For QR code scanning library
- **Modern Web Technologies**: For creating a responsive user interface
- **Web Audio API**: For audio feedback functionality

## 🎓 Use Cases

- **School Entry/Exit**: Mark student attendance at school gates
- **Classroom Attendance**: Quick roll call with QR scanning
- **Event Check-in**: Track student participation in events
- **Cafeteria Access**: Monitor meal times and access
- **Library Management**: Track student library visits
- **Bus Boarding**: Record bus boarding and alighting

## 📊 Features Roadmap

- [ ] Attendance reports and analytics
- [ ] Export attendance data (CSV, Excel)
- [ ] Email notifications for parents
- [ ] Multi-language support
- [ ] Offline mode support
- [ ] Attendance history view
- [ ] Admin dashboard
- [ ] Student profiles with photos

---

**Note**: This project was generated with AI assistance to demonstrate modern web development practices and efficient attendance management solutions.

## 📞 Support

For issues, questions, or contributions, please open an issue on the repository or contact the development team.

---

**Version**: 2.0.0  
**Last Updated**: 2026  
**License**: MIT