#! /usr/bin/env python3

import os
from src.model.log_model import LogModel
from src.tools.config_tools.config_tools import ConfigTools


class LogTools:
    def __init__(self, task_name: str=None):
        
        self.log_path = ""
        if task_name is None:
            self.task_log_file_path = self.gen_task_log_path(task_name=task_name)
            self.log_path = self.task_log_file_path
        else:
            self.default_log_file_path = self.gen_default_log_path()
            self.log_path = self.default_log_file_path
        
        
    def gen_default_log_path(self) -> str:
        config = ConfigTools()
        log_folder_path = config.get_log_folder_path()
        default_log_file_path = os.path.join(log_folder_path, "default.log")
        if not os.path.exists(log_folder_path):
            os.makedirs(log_folder_path)
        if not os.path.exists(self.default_log_file_path):
            try:
                with open(self.default_log_file_path, 'w') as file:
                    file.write("")
            except Exception as e:
                print(f"Gen default path: {default_log_file_path} error. {e}")
                default_log_file_path = ""
        return default_log_file_path
        
    def gen_task_log_path(self, task_name: str) -> str:
        
        config = ConfigTools()
        work_folder_path = config.get_source_folder_path()
        task_folder_path = os.path.join(work_folder_path, task_name)
        task_log_file_path = os.path.join(task_folder_path, "log.txt")
        if not os.path.exists(work_folder_path):
            os.makedirs(work_folder_path)
        if not os.path.exists(task_folder_path):
            os.makedirs(task_folder_path)
        if not os.path.exists(self.task_log_file_path):
            try:
                with open(self.task_log_file_path, 'w') as file:
                    file.write("")
            except Exception as e:
                print(f"Gen task log path: {task_log_file_path} error. {e}")
                task_log_file_path = ""
        return task_log_file_path
    
    
    def set_log_file_path(self, log_file_path: str):
        self.log_file_path = log_file_path
    
    def get_log_file_path(self) -> str:
        return self.log_file_path
    
    def write_log(self, log: LogModel):
        log_info = log.gen_log_info()
        with open(self.log_file_path, "a") as f:
            f.write(log_info + "\n")
    