#!/usr/bin/env python
import os
import sys

from src.model.step import Step
from src.tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools
# import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from pathlib import Path
from starlette.requests import Request
# import logging

# from settings import app_root_path
# from settings import upload_folder
# from settings import log_file_path

router = APIRouter()


@router.post("/select_task_all_step_name")
def select_all_task_name_server(request: Request):

    task_name = "test001"
    step_name = "step001"
    step = Step(task_name, step_name)
    step_base_info = step.get_step_base_info()
    return JSONResponse(content=step_base_info)
    

# @router.post("/select_all_step_name")
@router.post("/select_step_full_info")
def select_all_task_name_server(request: Request):

    task_name = "test001"
    step_name = "index001"
    step = Step(task_name, step_name)
    step_full_info = step.get_step_full_info()
    return JSONResponse(content=step_full_info)
