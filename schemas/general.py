from pydantic import BaseModel
from typing import Optional, List


class Installment(BaseModel):
    name: str
    unique_id: str
    patch: Optional[bool] = False


class State(BaseModel):
    name: str
    unique_id: str
    patch: Optional[bool] = False


class StudentInstallment(BaseModel):
    date: Optional[str] = None
    amount: Optional[int] = None
    invoice: Optional[int] = None
    unique_id: str
    install_unique_id: str
    student_unique_id: str
    patch: Optional[bool] = False


class Student(BaseModel):
    name: str
    school: str
    branch_id: Optional[int]
    governorate_id: Optional[int]
    institute_id: Optional[int]
    state_unique_id: str
    first_phone: Optional[str] = None
    second_phone: Optional[str] = None
    code_1: Optional[str] = None
    code_2: Optional[str] = None
    telegram_user: Optional[str] = None
    created_at: Optional[str] = None
    note: Optional[str] = None
    total_amount: Optional[float]
    poster: Optional[int]
    remaining_amount: Optional[float]
    unique_id: str
    patch: Optional[bool] = False


class Del(BaseModel):
    unique_id_students: Optional[List[str]] = []
    unique_id_students_install: Optional[List[str]] = []
    unique_id_states: Optional[List[str]] = []
    unique_id_installment: Optional[List[str]] = []
    unique_id_users: Optional[List[str]] = []
    patch: Optional[bool] = False


class GetStudents(BaseModel):
    deleted: Optional[bool] = False


class Authority(BaseModel):
    state_unique_id: str
    unique_id: str

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    password: str
    authority: List[Authority]
    unique_id: str
    name: Optional[str] = None

    class Config:
        orm_mode = True
