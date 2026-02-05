from fastapi import FastAPI, Depends, HTTPException, status, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from app.database.pydantic_model import GenQR
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.database.models import Students, Attendance
import secrets
from app.QRgen import gen_QR_code
from datetime import datetime, date
from sqlalchemy import and_
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI()
BASE_DIR = Path(__file__).parent

# Setup templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Mount sounds directory for audio feedback
app.mount("/sounds", StaticFiles(directory=str(BASE_DIR / "sounds")), name="sounds")



origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post('/api/qr-gen')
def QRgen(request:GenQR,  db: Session = Depends(get_db)):
    print('We have got a request.')
    # student_query = db.query(Students).filter(Students.student_id == request.student_id)
    student = db.query(Students).filter(Students.student_id == request.student_id).first()
    print('Now chekcing that is that students exists or not?')
    if student is None:
        print('found student is new....')
        token = secrets.token_urlsafe(16)
        request.student_qr_secret = token

        student = Students(**request.model_dump())
        db.add(student)
        db.commit()

        # token = secrets.token_urlsafe(16)

        response_file_path = gen_QR_code(token, request.student_id)

        return FileResponse(response_file_path, media_type='image/png', filename=f'{request.first_name}.png')
    
    else:
        print('found student is already in db....')
        file = BASE_DIR/'StudentQRcode'/f'{request.student_id}.png'
        
        print('Now checking that the file exists or not?')
        if file.exists():
            print('file already exists, now removing that file')
            file.unlink()
            # This will delete the file.
            print('file is removed...')
            # after removing the existing qr code, generate new qr code.
            token = secrets.token_urlsafe(16)
            print('token is ', token)
            
            response_file_path = gen_QR_code(token, request.student_id)
            print('path is', response_file_path)
            student.student_qr_secret = token
            db.commit()            

            return FileResponse(response_file_path, media_type='image/png', filename=f'{request.first_name}.png')
        
        else:
            path = BASE_DIR/'StudentQRcode'/f'{request.student_id}.png'
            
            if path.exists():
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Student with id {request.student_id} already exists.')

            else:
                print('file is not present now creating the file')
                # if the file path is not present
                token = secrets.token_urlsafe(16)
                response_file_path = gen_QR_code(token, request.student_id)

                student.student_qr_secret = token
                db.commit() 

                return FileResponse(response_file_path, media_type='image/png', filename=f'{request.first_name}.png')

@app.get('/qrs/{student_id}.png')
def get_qr_image(student_id: str):
    """Serve QR code images directly for mobile access"""
    qr_base_path = BASE_DIR / 'StudentQRcode'
    
    # First, check if QR code exists directly in the StudentQRcode folder (flat structure)
    direct_file_path = qr_base_path / f'{student_id}.png'
    if direct_file_path.exists():
        return FileResponse(str(direct_file_path), media_type='image/png', filename=f'{student_id}.png')
    
    # If not found in flat structure, search in nested directories
    for p in qr_base_path.rglob("*"):
        if p.is_dir() and p.name == f'{student_id}':
            nested_file_path = p / f'{student_id}.png'
            if nested_file_path.exists():
                return FileResponse(str(nested_file_path), media_type='image/png', filename=f'{student_id}.png')
    
    # If we reach here, no QR code was found
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"QR code with id: {student_id} not found.")

@app.get('/api/view/QRcode/{student_id}')
def view_qrcode(student_id):
    print(student_id)
    path = BASE_DIR/'StudentQRcode'/f'{student_id}.png'
    if path.exists():
        return FileResponse(path=path, media_type='image/png', filename=f'{student_id}.png')
        
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"QR code with id: {student_id} not found.")

@app.get('/scanner', response_class=HTMLResponse)
def scanner_page(request: Request):
    """Render the QR code scanning page"""
    return templates.TemplateResponse("scanner.html", {"request": request})

@app.get('/api/mark/attendance/{qr_secret}')
def mark_attendance(qr_secret, db: Session = Depends(get_db)):
    student = db.query(Students).filter(Students.student_qr_secret == qr_secret).first()
    # Here i am just fetching the student data.
    if student is not None:
        # I am checking that the student is in db or not if not then nothing will work so here student not None means the student is present in db and not i can just go ahead and update the db.
        today_date = date.today()
        attendance = db.query(Attendance).filter(
        and_(
            Attendance.student_id == student.student_id,
            Attendance.created_at == today_date, 
            Attendance.exit_time == None )).first()
        # Here to filter the attendance table, we need exit_time for testing purpose only, because if we don't write it then new rows will not created for todays date exit time, and that can not be good for showcase, and it will only update the time exit time if entry is already did.

        # NOTE: Also add the exit_time so that the time will not update and will not do anything when already is marked.
        if attendance is None:
            current_time = datetime.now().time()
            # Then create new attendance with entry time only
            new_attendance = Attendance(student_id=student.student_id, present=True, entry_time = current_time)

            # add new attendance
            db.add(new_attendance)
            db.commit()
            return {'success':True, 'entry':True, 'id':student.student_id, 'name':student.first_name, 'entry_time':current_time, 'exit_time':None}
        
        else:
            # if attendance has the entry time means today attendance is created.
            current_time = datetime.now().time()
            attendance.exit_time = current_time
            db.commit()
            
            return {'success':True, 'exit':True, 'id':student.student_id, 'name':student.first_name, 'entry_time':attendance.entry_time, 'exit_time':current_time}

    else:
        return {'success':False}