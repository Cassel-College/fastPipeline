#!/usr/bin/env python
import os
import sys

# import framework
from fastapi import APIRouter, Body,UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request
from pydantic import BaseModel

# import tools
from src.tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools

# import model
from src.model.step import Step

# import other server

# from pathlib import Path

# import logging

# from settings import app_root_path
# from settings import upload_folder
# from settings import log_file_path


router = APIRouter()

class StepCreate(BaseModel):
    task_name: str
    step_name: str

@router.post("/create")
def create(task_data: StepCreate = Body(...)):

    task_name = task_data.task_name
    step_name = task_data.step_name
    log_info = f"task name: {task_name} exists!"
    step = Step(task_name=task_name, step_name=step_name)
    print(step.to_dict())
    create_status = step.create_step_in_work_folder()
    return_info = {
        "message": log_info,
        "create_status": create_status,
        "step": step.to_dict()
    }
    return JSONResponse(content=return_info)
