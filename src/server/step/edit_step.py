#!/usr/bin/env python
import os
import sys

# import framework
from fastapi import APIRouter, Body, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request
from pydantic import BaseModel

# import tools
from src.model.log_model import LogModel
from src.model.return_info import ReturnCode, ReturnInfo
from src.tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools

# import model
from src.model.step import Step
from src.tools.log_tools.log_tools import LogTools

# import other server

# from pathlib import Path

# import logging

# from settings import app_root_path
# from settings import upload_folder
# from settings import log_file_path


router = APIRouter()


class StepEdit(BaseModel):
    task_name: str
    step_name: str
    
    
class StepEditFile(BaseModel):
    task_name: str
    step_name: str
    path_name: str
    file_path: str
    file_info: str
    

@router.post("/edit_step")
def edit(step_data: StepEditFile = Body(...)):

    task_name = step_data.task_name
    step_name = step_data.step_name
    path_name = step_data.path_name
    file_path = step_data.file_path
    file_info = step_data.file_info
    log_server = LogTools()
    
    log_info = f"Edit step of {task_name} and {step_name}."
    log_server.write_log(log=LogModel(log_info, "INFO"))
    
    step = Step(task_name=task_name, step_name=step_name)
    edit_result = step.edit_step_file(path_name=path_name, file_path=file_path, file_info=file_info)
    
    log_info = f"Edit step of {task_name} and {step_name} over."
    log_server.write_log(log=LogModel(log_info, "INFO"))
    return edit_result


@router.post("/get_step")
def get_step_file_info(task_data: StepEdit = Body(...)):
    
    log_server = LogTools()
    
    task_name = task_data.task_name
    step_name = task_data.step_name
    
    log_info = f"Get all step file info of {task_name} and {step_name}."
    log_server.write_log(log=LogModel(log_info, "INFO"))
    
    step = Step(task_name=task_name, step_name=step_name)
    result = step.get_step_all_file_info()
    
    log_info = f"Get all step file info of {task_name} and {step_name} over."
    log_server.write_log(log=LogModel(log_info, "INFO"))
    return result
    