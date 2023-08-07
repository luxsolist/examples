from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.user import user_router


app = FastAPI()

# 원래는 보안상 이렇게 하면 안됨
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user")