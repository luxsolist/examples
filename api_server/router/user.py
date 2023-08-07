from fastapi import APIRouter, Depends, HTTPException
from model.user_model import *
from repository import user_repo
from resource.database import get_db
from sqlalchemy.orm import Session
from typing import List


user_router = APIRouter()


@user_router.post("/signup", response_model=UserRes)
def signup(user: UserSignupReq, db: Session = Depends(get_db)):
    db_user = user_repo.get_by_user_id(db, user_id=user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail=f"user {user.user_id} already registered")
    return user_repo.insert(db=db, user=user)


@user_router.get("/list", response_model=List[UserRes])
def get_all(db: Session = Depends(get_db)):
    return user_repo.get_all(db=db)
