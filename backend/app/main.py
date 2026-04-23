from typing import Annotated
from contextlib import asynccontextmanager

from db.base import init_db, close_db, get_session
from sqlmodel import Session

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from api.main_router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    close_db()

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI(
    lifespan=lifespan,
)

app.include_router(router)

origins = [
    "http://localhost:5173",
    "127.0.0.1.5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api", summary="Main root")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)