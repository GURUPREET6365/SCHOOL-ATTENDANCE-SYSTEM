from pydantic import BaseModel
from typing import Optional


class GenQR(BaseModel):
    first_name:str
    last_name:str
    email:str
    student_id: int
    student_qr_secret: Optional[str] = None
