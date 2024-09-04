#!/usr/bin/env python
import os
import sys

from src.model.return_info import ReturnCode, ReturnInfo
from src.tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools

from src.model.task import Task

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



@router.get("/select_all_task_name")
def select_all_task_name_server(request: Request):

    task_names = Task().select_all_task_name_core()
    return JSONResponse(content=task_names)


@router.get("/select_full_info_by_task_name")
def select_all_task_name_server(request: Request):

    task_name = "test001"
    task_full_info = {}
    return_results = {}
    task = Task(task_name)
    if task.check_task_exist():
        task_full_info = task.get_task_full_info()
        if task_full_info.get("return_value", 0) == 0:
            return_results = {
                "code": 1,
                "massage": "get task full info success",
                "data": task_full_info,
            }
        else:
            return_results = {
                "code": 0,
                "massage": "get task full info failed",
                "data": task_full_info
            }
    else:
        return_results = {
            "code": 0,
            "massage": "task not exist",
            "data": task_full_info
        }
    return JSONResponse(content=return_results)


@router.post("/select_all_step_name")
def select_all_task_name_server(request: Request):

    task_name = "test001"
    return_results = {
        "return_value": 0,
        "massage": "get step names failed",
        "step_names": []
    }
    task = Task(task_name)
    all_step_names = task.get_step_base_names()

    if all_step_names.get("return_value", 0) == 1:
        return_results = {
            "return_value": 1,
            "massage": "get step names success",
            "step_names": all_step_names.get("step_names", [])
        } 
    return JSONResponse(content=return_results)