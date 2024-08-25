#!/usr/bin/env python
import os
import sys

from src.tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools

class Step:

    def __init__(self, ):
        self.task_name = ""
        self.step_name = ""
        self.script_type = ""
        self.script_file_path = ""
        self.script_exec_input_file_path = ""
        self.script_exec_output_file_path = ""
        self.script_exec_log_file_path = ""
        self.config = ConfigTools()

    def create_step_in_work_folder(self, work_folder_path: str) -> bool:

        create_status = True
        if not self.create_step_dir() and create_status:
            log_info = f"create step dir failed!"
            create_status = False
        if not self.create_script_empty_file() and create_status:
            log_info = f"create step script failed!"
            create_status = False
        if not self.create_script_exec_input_file_path() and create_status:
            log_info = f"create step script exec input file path failed!"
            create_status = False
        if not self.create_script_exec_output_file_path() and create_status:
            log_info = f"create step script exec output file path failed!"
            create_status = False
        if not self.create_script_exec_log_file_path() and create_status:
            log_info = f"create step script exec log file path failed!"
            create_status = False
        return create_status
    
    def create_step_dir(self) -> bool:

        source_folder_path = self.config.get_source_folder_path()
        step_folder_path = os.path.join(source_folder_path, self.task_name, self.step_name)
        log_info = f"step folder path: {step_folder_path}"
        create_status = IOTools().create_target_folder(step_folder_path)
        return create_status
    
    def create_script_empty_file(self) -> bool:

        source_folder_path = self.config.get_source_folder_path()
        step_file_path = os.path.join(source_folder_path, self.task_name, self.step_name, self.step_name + ".py")
        log_info = f"step file path: {step_file_path}"
        create_status = IOTools().create_target_file(step_file_path)
        return create_status
    

    def create_script_exec_input_file_path(self) -> bool:

        source_folder_path = self.config.get_source_folder_path()
        script_exec_input_file_name = self.config.get_input_file_name()
        script_exec_input_file_path = os.path.join(source_folder_path, self.task_name, self.step_name, script_exec_input_file_name)
        log_info = f"script exec input file path: {script_exec_input_file_path}"
        create_status = IOTools().create_target_file(script_exec_input_file_path)
        return create_status
    
    def create_script_exec_output_file_path(self) -> bool:

        source_folder_path = self.config.get_source_folder_path()
        script_exec_output_file_name = self.config.get_output_file_name()
        script_exec_output_file_path = os.path.join(source_folder_path, self.task_name, self.step_name, script_exec_output_file_name)
        log_info = f"script exec output file path: {script_exec_output_file_path}"
        create_status = IOTools().create_target_file(script_exec_output_file_path)
        return create_status
    
    def create_script_exec_log_file_path(self) -> bool:

        source_folder_path = self.config.get_source_folder_path()
        script_exec_log_file_name = self.config.get_step_log_file_name()
        script_exec_log_file_path = os.path.join(source_folder_path, self.task_name, self.step_name, script_exec_log_file_name)
        log_info = f"script exec log file path: {script_exec_log_file_path}"
        create_status = IOTools().create_target_file(script_exec_log_file_path)
        return create_status

    