#!/usr/bin/env python

from typing import Union
from fastapi import FastAPI, Depends, HTTPException
# from starlette.middleware.sessions import SessionMiddleware
# from starlette.requests import Request


from src.server.task import select_task 
from src.server.task import create_task
from src.tools.config_tools import ConfigTools
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(select_task.router, prefix="/api/v1/task")
app.include_router(create_task.router, prefix="/api/v1/task")

@app.get("/")
async def root():
    
    a = ConfigTools()
    print(a.get_config())
    return {"message": "Hello World"}
