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
    
    task_names = Task().select_all_task_name_core()
    if task_names.get("code", ReturnCode.FAILED) == ReturnCode.FAILED:
        log_info = f"get old task names failed!"
        print(log_info)
        return {"code": ReturnCode.FAILED, "message": log_info, "resout": {}}
    
    if task_name in task_names.get("data", []):
        log_info = f"task name: {task_name} already exists!"
        print(log_info)
        return {"code": ReturnCode.FAILED, "message": log_info, "resout": {}}
    
    task = Task(task_name)
    task.init_for_create()
    return_info = task.create()
    
    
    
    config = ConfigTools()
    source_folder_path = config.get_source_folder_path()
    all_task_names = select_all_task_name_core()
    log_info = f"all task names: {all_task_names}"
    print(log_info)
    
    resout_code = 1 # 0: success, 1: failed
    if task_name in all_task_names:
        log_info = f"task name: {task_name} already exists!"
        print(log_info)
    else:
        log_info = f"task name: {task_name} not exists!"
        print(log_info)
        io_tools = IOTools()
        task_dir = os.path.join(source_folder_path, task_name)
        resout = io_tools.create_target_folder(task_dir)
        resout_code = resout.get("return_value", 1)
        if resout_code == 0:
            log_info = f"create task folder success!"
            task_index_json_file = os.path.join(source_folder_path, task_name, "task_index.json")
            resout = io_tools.create_target_file(task_index_json_file)
            resout_code = resout.get("return_value", 1)
            if resout_code == 0:
                log_info = f"create task index json file success!"
            else:
                log_info = f"create task index json file failed!"
            print(log_info)
        else:
            log_info = f"create task folder failed!"
            print(log_info)
    return {"code": resout_code, "message": log_info, "resout": resout_code}

