#!/usr/bin/env python
import os
import sys

from src.tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools

class Step:

    def __init__(self, task_name: str, step_name: str):
        self.task_name = task_name
        self.step_name = step_name
        self.script_type = ""
        self.script_file_path = ""
        self.script_exec_input_file_path = ""
        self.script_exec_output_file_path = ""
        self.script_exec_log_file_path = ""
        self.config = ConfigTools()

    def create_step_in_work_folder(self) -> bool:

        create_status = True
        if self.create_step_dir().get("create_status") != 0 or not create_status:
            log_info = f"create step folder failed!"
            print(log_info)
            create_status = False
        else:
            log_info = f"create step folder success!"
            print(log_info)
        if self.create_script_empty_file().get("create_status") != 0 or not create_status:
            log_info = f"create step script failed!"
            print(log_info)
            create_status = False
        else:
            log_info = f"create step script success!"
            print(log_info)
        if self.create_script_exec_input_file_path().get("create_status") != 0 or not create_status:
            log_info = f"create step script exec input file path failed!"
            print(log_info)
            create_status = False
        else:
            log_info = f"create step script exec input file path success!"
            print(log_info)
        if self.create_script_exec_output_file_path().get("create_status") != 0 or not create_status:
            log_info = f"create step script exec output file path failed!"
            print(log_info)
            create_status = False
        else:
            log_info = f"create step script exec output file path success!"
            print(log_info)
        if self.create_script_exec_log_file_path().get("create_status") != 0 or not create_status:
            log_info = f"create step script exec log file path failed!"
            print(log_info)
            create_status = False
        else:
            log_info = f"create step script exec log file path success!"
            print(log_info)
        return create_status
    
    def create_step_dir(self) -> dict:

        source_folder_path = self.config.get_source_folder_path()
        step_folder_path = os.path.join(source_folder_path, self.task_name, self.step_name)
        log_info = f"step folder path: {step_folder_path}"
        print(log_info)
        self.step_folder_path = step_folder_path
        create_results = IOTools().create_target_folder(step_folder_path)
        return create_results
    
    def create_script_empty_file(self) -> dict:

        source_folder_path = self.config.get_source_folder_path()
        abs_step_folder_path = os.path.join(source_folder_path, self.task_name, self.step_name)
        script_file_path = os.path.join(abs_step_folder_path, self.step_name + ".py")
        self.script_file_path = script_file_path
        log_info = f"step file path: {script_file_path}"
        create_results = IOTools().create_target_file(script_file_path)
        return create_results

    def create_script_exec_input_file_path(self) -> dict:

        source_folder_path = self.config.get_source_folder_path()
        abs_step_folder_path = os.path.join(source_folder_path, self.task_name, self.step_name)
        script_exec_input_file_name = self.config.get_input_file_name()
        script_exec_input_file_path = os.path.join(abs_step_folder_path, script_exec_input_file_name)
        self.script_exec_input_file_path = script_exec_input_file_path
        log_info = f"script exec input file path: {script_exec_input_file_path}"
        create_results = IOTools().create_target_file(script_exec_input_file_path)
        return create_results
    
    def create_script_exec_output_file_path(self) -> dict:

        source_folder_path = self.config.get_source_folder_path()
        abs_step_folder_path = os.path.join(source_folder_path, self.task_name, self.step_name)
        script_exec_output_file_name = self.config.get_output_file_name()
        script_exec_output_file_path = os.path.join(abs_step_folder_path, script_exec_output_file_name)
        self.script_exec_output_file_path = script_exec_output_file_path
        log_info = f"script exec output file path: {script_exec_output_file_path}"
        create_results = IOTools().create_target_file(script_exec_output_file_path)
        return create_results
    
    def create_script_exec_log_file_path(self) -> dict:

        source_folder_path = self.config.get_source_folder_path()
        abs_step_folder_path = os.path.join(source_folder_path, self.task_name, self.step_name)
        script_exec_log_file_name = self.config.get_step_log_file_name()
        script_exec_log_file_path = os.path.join(abs_step_folder_path, script_exec_log_file_name)
        self.script_exec_log_file_path = script_exec_log_file_path
        log_info = f"script exec log file path: {script_exec_log_file_path}"
        create_results = IOTools().create_target_file(script_exec_log_file_path)
        return create_results

    def to_dict(self) -> dict:
        return {
            "task_name": self.task_name,
            "step_name": self.step_name,
            "script_file_path": self.script_file_path,
            "script_exec_input_file_path": self.script_exec_input_file_path,
            "script_exec_output_file_path": self.script_exec_output_file_path,
            "script_exec_log_file_path": self.script_exec_log_file_path
        }
        
    def get_step_base_info(self) -> dict:
        
        config = ConfigTools()
        source_folder_path = config.get_source_folder_path()
        folder_names = IOTools().get_folder_names_from_path(source_folder_path)
        return folder_names