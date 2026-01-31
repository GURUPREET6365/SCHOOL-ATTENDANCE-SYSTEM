from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date, Time
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, nullable=False , index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    student_id = Column(Integer, unique=True, nullable=False)
    student_qr_secret = Column(String, unique=True, nullable=False)
    standard = Column(Integer, nullable=True)
    streamORsection= Column(String, nullable=True)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
        )
    attendances = relationship(
        "Attendance",
        back_populates="student",
        cascade="all, delete"
    )
    
class Attendance(Base):
    __tablename__='attendance'

    id = Column(Integer, primary_key=True, nullable=False, index=True)

    student_id = Column(Integer, ForeignKey("students.id", ondelete='CASCADE'))

    present = Column(Boolean, nullable=False)

    created_at = Column(Date,server_default=func.current_date())

    entry_time = Column(Time, nullable=True)

    exit_time = Column(Time, nullable=True)

    student = relationship(
        "Students",
        back_populates="attendances"
    )