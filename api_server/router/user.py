from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 
from model.user_model import *
from repository import user_repo
from resource.database import get_db
from sqlalchemy.orm import Session
from typing import List


user_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@user_router.post("/signup", response_model=UserRes)
def signup(user: UserSignupReq, db: Session = Depends(get_db)):
    db_user = user_repo.get_by_user_id(db, user_id=user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail=f"user {user.user_id} already registered")
    return user_repo.insert(db=db, user=user)


@user_router.get("/list", response_model=List[UserRes])
def get_all_users(db: Session = Depends(get_db)):
    return user_repo.get_all(db=db)


@user_router.get("/web/list", response_class=HTMLResponse)
async def get_all_users_html(request: Request, db: Session = Depends(get_db)):
    list_users = user_repo.get_all(db=db)
    context = {
        "request": request,
        "users" : list_users  # user/list.html의 {%- for u in users %} 부분의 'users' 에서 사용
    }
    return templates.TemplateResponse("user/list.html", context)