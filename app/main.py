from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routers import answers, categories, questions, stats
from app.seed.init_db import create_tables, seed_questions
from app.database import SessionLocal


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    db = SessionLocal()
    try:
        seed_questions(db)
    finally:
        db.close()
    yield


app = FastAPI(
    title="JSTQB FL 学習支援アプリ",
    description="JSTQB Foundation Level 試験の学習を支援する Web アプリ",
    lifespan=lifespan,
)

# JSTQB FL 新 API
app.include_router(categories.router)
app.include_router(questions.router)
app.include_router(answers.router)

# 旧 SQL Silver API（後方互換で維持）
app.include_router(questions.legacy_router)
app.include_router(answers.legacy_router)

app.include_router(stats.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
def serve_index():
    return FileResponse("static/index.html")
