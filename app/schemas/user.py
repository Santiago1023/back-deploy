from typing import List
from pydantic import BaseModel
from datetime import datetime
from app.schemas.sign import ShowSign as Sign


class UserBase(BaseModel):
    name: str
    email: str
    password: str
    creation_date: datetime
    modification_data: datetime
    role: str
    location: str
    documentId: str
    university: str
    signs: List[Sign]

    class Config:
        orm_mode = True


class CurrentUser(BaseModel):
    id: str
    role: str
    email: str


class CreateUser(BaseModel):
    name: str
    email: str
    role: str
    location: str
    documentId: str
    university: str


class ShowUser(BaseModel):
    name: str
    email: str
    location: str
    documentId: str
    university: str
    signs: List[Sign] = []


class EditUser(BaseModel):
    name: str
    email: str
    role: str
    fecha_modificacion: datetime
    signs: List[Sign] = []


class EditCredentials(BaseModel):
    new_password: str


class UserAllInfomation(BaseModel):
    id: str
    name: str
    email: str
    creation_date: datetime
    modification_data: datetime
    role: str
    location: str
    documentId: str
    university: str