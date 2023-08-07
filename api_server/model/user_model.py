from pydantic import BaseModel

class UserSignupReq(BaseModel):
    user_id: str
    password: str
    name: str
    email: str

class UserRes(BaseModel):
    id: int
    user_id: str
    name: str
    email: str
    is_active: int
