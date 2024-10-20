#!/usr/bin/env python

from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# from starlette.middleware.sessions import SessionMiddleware
# from starlette.requests import Request


from src.server.task import select_task 
from src.server.task import create_task
from src.server.task import exec_task
from src.server.step import create_step
from src.server.step import select_step
from src.server.step import edit_step
from src.tools.config_tools import ConfigTools
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源，生产环境中应该更具体
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
   
app.include_router(select_task.router, prefix="/api/v1/task")
app.include_router(create_task.router, prefix="/api/v1/task")
app.include_router(exec_task.router, prefix="/api/v1/task")
app.include_router(create_step.router, prefix="/api/v1/step")
app.include_router(select_step.router, prefix="/api/v1/step")
app.include_router(edit_step.router, prefix="/api/v1/step")

@app.get("/")
async def root():
    a = ConfigTools()
    print(a.get_config())
    return {"message": "Hello World"}
