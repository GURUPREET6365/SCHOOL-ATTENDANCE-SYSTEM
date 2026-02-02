from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.database.pydantic_model import GenQR
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.database.models import Students, Attendance
import secrets
from app.QRgen import gen_QR_code
from datetime import datetime, date
from sqlalchemy import and_
from fastapi.responses import FileResponse
from pathlib import Path

BASE_DIR = Path(__file__).parent


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {'message':'This is the school attendance manager system.'}

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

        response_file_path = gen_QR_code(token, request.standard, request.streamORsection, request.student_id)

        return FileResponse(response_file_path, media_type='image/png', filename=f'{request.first_name}.png')
    
    else:
        print('found student is already in db....')
        file = BASE_DIR/'StudentQRcode'/f'class-{request.standard}'/f'streamORsection-{request.streamORsection}'/f'{request.student_id}'/f'{request.student_id}.png'
        
        print('Now checking that the file exists or not?')
        if file.exists():
            print('file already exists, now removing that file')
            file.unlink()
            # This will delete the file.
            print('file is removed...')
            # after removing the existing qr code, generate new qr code.
            token = secrets.token_urlsafe(16)
            print('token is ', token)
            
            response_file_path = gen_QR_code(token, request.standard, request.streamORsection, request.student_id)
            print('path is', response_file_path)
            student.student_qr_secret = token
            db.commit()            

            return FileResponse(response_file_path, media_type='image/png', filename=f'{request.first_name}.png')
        
        else:
            path = BASE_DIR/'StudentQRcode'
            for p in path.rglob("*"):
                if p.is_dir() and p.name == f'{request.student_id}':
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Student with id {request.student_id} already exists.')

            else:
                print('file is not present now creating the file')
                # if the file path is not present
                token = secrets.token_urlsafe(16)
                response_file_path = gen_QR_code(token, request.standard, request.streamORsection, request.student_id)

                student.student_qr_secret = token
                db.commit() 

                return FileResponse(response_file_path, media_type='image/png', filename=f'{request.first_name}.png')

@app.get('/api/view/QRcode/{student_id}')
def view_qrcode(student_id):
    print(student_id)
    path = BASE_DIR/'StudentQRcode'
    for p in path.rglob("*"):
        if p.is_dir() and p.name == f'{student_id}':
            response_file_path=f'{p}/{student_id}.png'
            return FileResponse(response_file_path, media_type='image/png', filename=f'{student_id}.png')
        
        else:
            HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"QR code with id: {student_id} not found.")

@app.get('/api/mark/attendance/{qr_secret}')
def mark_attendance(qr_secret, db: Session = Depends(get_db)):
    student = db.query(Students).filter(Students.student_qr_secret == qr_secret).first()
    
    if student is not None:
        
        today_date = date.today()
        attendance = db.query(Attendance).filter(
        and_(
            Attendance.student_id == student.student_id,
            Attendance.created_at == today_date, 
             Attendance.exit_time == None )).first()
        
        if attendance is None:
            current_time = datetime.now().time()
            # Then create new attendance with entry time only
            new_attendance = Attendance(student_id=student.student_id, present=True, entry_time = current_time)

            # add new attendance
            db.add(new_attendance)
            db.commit()
            return {'success':True, 'entry':True}
        
        else:
            # if attendance has the entry time means today attendance is created.
            current_time = datetime.now().time()
            attendance.exit_time = current_time
            db.commit()
            return {'success':True, 'exit':True}

    else:
        return {'success':False}