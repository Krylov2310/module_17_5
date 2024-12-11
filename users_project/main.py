from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()
info_ed = ('<h2>Домашнее задание по теме "Использование БД в маршрутизации. 1.2"<br>'
           '<h3>Цель: закрепить навык управления записями в БД, используя SQLAlchemy и маршрутизацию FastAPI.'
           '<br>Задача "Маршрутизация заданий":'
           '<br>Студент Крылов Эдуард Васильевич'
           '<br>Дата: 11.12.2024г.</h3>')


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


@app.get("/info", response_class=HTMLResponse)
async def info():
    return info_ed


app.include_router(task.router)
app.include_router(user.router)

# alembic revision --autogenerate -m "Initial migration"
# python main.py migrate
# alembic upgrade head
# python -m uvicorn main:app
# uvicorn main:app --reload
