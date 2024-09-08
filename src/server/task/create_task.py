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
from src.model.return_info import ReturnCode
from src.model.task import Task
from src.tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools

# import other server
from src.tools.log_tools.log_tools import LogTools

# from pathlib import Path

# import logging

# from settings import app_root_path
# from settings import upload_folder
# from settings import log_file_path

router = APIRouter()


class TaskCreate(BaseModel):
    task_name: str

@router.post("/create")
def create(task_data: TaskCreate = Body(...)):
    
    log_server = LogTools()
    
    task_name = task_data.task_name
    log_server.write_log(log=LogModel(f"create task: {task_name}", "INFO"))
    
    task_names = Task(task_name=task_name).select_all_task_name_core()
    if task_names.get_code() == ReturnCode.FAILED:
        log_info = f"get old task names failed!"
        log_server.write_log(log=LogModel(log_info, "ERROR"))
        return {"code": ReturnCode.FAILED, "message": log_info, "resout": {}}
    
    if task_name in task_names.get_data()["folder_names"]:
        log_info = f"task name: {task_name} already exists!"
        log_server.write_log(log=LogModel(log_info, "ERROR"))
        return {"code": ReturnCode.FAILED, "message": log_info, "resout": {}}
    else:
        log_server.write_log(log=LogModel(f"task name: {task_name} not exists! create task.", "INFO"))
    
    task = Task(task_name)
    task.init_for_create()
    return_info = task.create()
    return return_info
    
    