#!/usr/bin/env python
import os
import sys

# import framework
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request

# import tools
from src.tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools

# import model
from src.model.step import Step

# import other server
from src.server.task.select_task import select_all_task_name_core

# from pathlib import Path

# import logging

# from settings import app_root_path
# from settings import upload_folder
# from settings import log_file_path


router = APIRouter()


@router.post("/create")
def create(request: Request):

    task_name = "test002"
    step_name = "index001"
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
