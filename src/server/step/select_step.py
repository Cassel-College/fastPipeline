#!/usr/bin/env python
import os
import sys

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

def select_all_task_name_core() -> list:

    config = ConfigTools()
    source_folder_path = config.get_source_folder_path()
    folder_names = IOTools().get_folder_names_from_path(source_folder_path)
    return folder_names

@router.post("/select_step_base_info")
def select_all_task_name_server(request: Request):

    task_name = ""
    step_name = ""
    pass
    
    
    
@router.post("/select_all_step_name")
def select_all_task_name_server(request: Request):

    task_name = ""
    get_all_step_name

