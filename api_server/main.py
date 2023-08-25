from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates 
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

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(user_router, prefix="/user")

@app.get("/")
async def home(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("home.html", context)

@app.get("/layout-static")
async def layout_static(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("layout-static.html", context)

@app.get("/charts")
async def view_charts(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("charts.html", context)

@app.get("/tables")
async def view_tables(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("tables.html", context)
