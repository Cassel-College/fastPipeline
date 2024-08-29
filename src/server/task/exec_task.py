#! /usr/bin/env python3

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse

from src.model.task import Task

router = APIRouter()

@router.post("/exec_task")
def select_all_task_name_server(request: Request):

    task_name = "test001"
    task = Task(task_name)
    task_exec_results = task.exec_task()
    return JSONResponse(content=task_exec_results)