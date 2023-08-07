from model.user_model import *
from resource.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Session
from typing import List


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, index=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String)
    email = Column(String)
    is_active = Column(Boolean, default=True)


def insert(db: Session, user: UserSignupReq) -> User:
    db_user = User(user_id=user.user_id, password=user.password, name=user.name, email=user.email)
    db.add(db_user)
    db.commit()

    return db_user

def get_by_user_id(db: Session, user_id: str) -> User:
    return db.query(User).\
        filter(User.user_id == user_id).first()

def get_all(db:Session) -> List[User]:
    return db.query(User).all()
