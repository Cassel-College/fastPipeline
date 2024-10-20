#!/usr/bin/env python
import os
import sys

from src.model.log_model import LogModel
from src.model.return_info import ReturnCode, ReturnInfo
from src.tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools
from src.tools.log_tools.log_tools import LogTools

class Step:

    def __init__(self, task_name: str, step_name: str):
        self.task_name = task_name
        self.step_name = step_name
        self.script_file_path = ""
        self.script_exec_input_file_path = ""
        self.script_exec_output_file_path = ""
        self.script_exec_log_file_path = ""
        self.script_exec_local_config_path = ""
        self.config = ConfigTools()
        self.script_engine = self.config.get_script_engine()

    def create_step_in_work_folder(self) -> bool:

        create_status = True
        if self.create_step_dir().get_code() != 0 or not create_status:
            log_info = f"create step folder failed!"
            print(log_info)
            create_status = False
        else:
            log_info = f"create step folder success!"
            print(log_info)
        if self.create_script_empty_file().get_code() != 0 or not create_status:
            log_info = f"create step script failed!"
            print(log_info)
            create_status = False
        else:
            log_info = f"create step script success!"
            print(log_info)
        if self.create_script_exec_input_file_path().get_code() != 0 or not create_status:
            log_info = f"create step script exec input file path failed!"
            print(log_info)
            create_status = False
        else:
            log_info = f"create step script exec input file path success!"
            print(log_info)
        if self.create_script_exec_output_file_path().get_code() != 0 or not create_status:
            log_info = f"create step script exec output file path failed!"
            print(log_info)
            create_status = False
        else:
            log_info = f"create step script exec output file path success!"
            print(log_info)
        if self.create_script_exec_log_file_path().get_code() != 0 or not create_status:
            log_info = f"create step script exec log file path failed!"
            print(log_info)
            create_status = False
        else:
            log_info = f"create step script exec log file path success!"
            print(log_info)
        return create_status
    
    def create_step_dir(self) -> ReturnInfo:

        log_server = LogTools()
        log_server.write_log(log=LogModel(f"create step dir of {self.task_name}:{self.step_name}.", "INFO"))
        source_folder_path = self.config.get_source_folder_path()
        step_folder_path = os.path.join(source_folder_path, self.task_name, self.step_name)
        self.step_folder_path = step_folder_path
        create_results = IOTools().create_target_folder(step_folder_path)
        return create_results
    
    def create_script_empty_file(self) -> ReturnInfo:

        log_server = LogTools()
        log_server.write_log(log=LogModel(f"create step script of {self.task_name}:{self.step_name}.", "INFO"))
        source_folder_path = self.config.get_source_folder_path()
        abs_step_folder_path = os.path.join(source_folder_path, self.task_name, self.step_name)
        script_file_path = os.path.join(abs_step_folder_path, self.step_name + ".py")
        self.script_file_path = script_file_path
        create_results = IOTools().create_target_file(script_file_path)
        return create_results

    def create_script_exec_input_file_path(self) -> ReturnInfo:

        log_server = LogTools()
        log_server.write_log(log=LogModel(f"create step script exec input file path of {self.task_name}:{self.step_name}.", "INFO"))
        source_folder_path = self.config.get_source_folder_path()
        abs_step_folder_path = os.path.join(source_folder_path, self.task_name, self.step_name)
        script_exec_input_file_name = self.config.get_input_file_name()
        script_exec_input_file_path = os.path.join(abs_step_folder_path, script_exec_input_file_name)
        self.script_exec_input_file_path = script_exec_input_file_path
        log_info = f"script exec input file path: {script_exec_input_file_path}"
        create_results = IOTools().create_target_file(script_exec_input_file_path)
        return create_results
    
    def create_script_exec_output_file_path(self) -> ReturnInfo:

        log_server = LogTools()
        log_server.write_log(log=LogModel(f"create step script exec output file path of {self.task_name}:{self.step_name}.", "INFO"))
        source_folder_path = self.config.get_source_folder_path()
        abs_step_folder_path = os.path.join(source_folder_path, self.task_name, self.step_name)
        script_exec_output_file_name = self.config.get_output_file_name()
        script_exec_output_file_path = os.path.join(abs_step_folder_path, script_exec_output_file_name)
        self.script_exec_output_file_path = script_exec_output_file_path
        log_info = f"script exec output file path: {script_exec_output_file_path}"
        create_results = IOTools().create_target_file(script_exec_output_file_path)
        return create_results
    
    def create_script_exec_log_file_path(self) -> ReturnInfo:

        log_server = LogTools()
        log_server.write_log(log=LogModel(f"create step script exec log file path of {self.task_name}:{self.step_name}.", "INFO"))
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
    
    
    def get_exec_step_script_info(self) -> dict:
        
        return_info = {
            "script_file_path": self.script_file_path,
            "input_file_path": self.script_exec_input_file_path,
            "local_config_path": self.script_exec_local_config_path,
            "bash_command": f"python3 {self.script_file_path} {self.script_exec_input_file_path} {self.script_exec_output_file_path} {self.script_exec_log_file_path}",
        }
        return return_info
    
    def get_abs_output_file_path(self) -> dict:
        
        abs_output_file_path = self.script_exec_output_file_path
        return_results = {
            "return_value": 1,
            "massage": abs_output_file_path
        }
        return return_results
    
    def init_at_workspace(self):
        
        init_status = True
        workspace_root_path = self.config.get_source_folder_path()
        setp_workspace_path = os.path.join(workspace_root_path, self.task_name, self.step_name)
        target_script_file_path = os.path.join(setp_workspace_path, self.step_name + ".py")
        if IOTools().check_file_exist(target_script_file_path):
            self.script_file_path = target_script_file_path
        else:
            log_info = f"{self.task_name} {self.step_name} step script file path: {target_script_file_path} not exist!"
            print(log_info)
            init_status = False
        target_script_exec_input_file_path = os.path.join(setp_workspace_path, self.config.get_input_file_name())
        if IOTools().check_file_exist(target_script_exec_input_file_path):
            self.script_exec_input_file_path = target_script_exec_input_file_path
        else:
            log_info = f"{self.task_name} {self.step_name} step script exec input file path: {target_script_exec_input_file_path} not exist!"
            print(log_info)
            init_status = False
        target_script_exec_output_file_path = os.path.join(setp_workspace_path, self.config.get_output_file_name())
        if IOTools().check_file_exist(target_script_exec_output_file_path):
            self.script_exec_output_file_path = target_script_exec_output_file_path
        else:
            log_info = f"{self.task_name} {self.step_name} step script exec output file path: {target_script_exec_output_file_path} not exist!"
            print(log_info)
            init_status = False
        target_script_exec_log_file_path = os.path.join(setp_workspace_path, self.config.get_step_log_file_name())
        if IOTools().check_file_exist(target_script_exec_log_file_path):
            self.script_exec_log_file_path = target_script_exec_log_file_path
        else:
            log_info = f"{self.task_name} {self.step_name} step script exec log file path: {target_script_exec_log_file_path} not exist!"
            print(log_info)
            init_status = False
        return init_status
    
    def get_step_full_info(self) -> ReturnInfo:
        
        result = ReturnInfo(code=1, message="", data=None)
        self.init_at_workspace()
        result.set_code(ReturnCode.SUCCESS)
        result.set_message("Get step full info success!")
        result.set_data(self.to_dict())
        return result
    
    def gen_exec_bash_command(self, step_full_info: dict) -> str:
        
        e = f"{self.script_engine}"
        s = f" {step_full_info.get('script_file_path')}"
        i = f"-input_file_path {step_full_info.get('script_exec_input_file_path')}"
        o = f"-output_file_path {step_full_info.get('script_exec_output_file_path')}"
        l = f"-log_file_path {step_full_info.get('script_exec_log_file_path')}"
        exec_bash_command = f"{e} {s} {i} {o} {l}"
        return exec_bash_command
    
    def exec_step(self) -> dict:
        
        return_value = 0
        return_results = {
            "return_value": return_value,
            "message": ""
        }
        step_full_info_results = self.get_step_full_info()
        if step_full_info_results.get("return_value", 0) == 0:
            return_results["return_value"] = 0
            return_results["message"] = f"Get step full info failed!"
            return return_results
        else:
            return_results["return_value"] = 1
            return_results["message"] = f"Get step full info success!"
        step_full_info = step_full_info_results.get("step_full_info", {})
        exec_bash_command = self.gen_exec_bash_command(step_full_info=step_full_info)
        log_info = f"Exec step bash command: {exec_bash_command}"
        print(log_info)
        
        exec_bash_command_results = {
            "return_value": 1,
            "message": ""
        }
        # exec_bash_command_results = IOTools().exec_bash_command(exec_bash_command)
        if exec_bash_command_results.get("return_value", 0) == 0:
            return_results["return_value"] = 0
            return_results["message"] = f"Exec step bash command failed!"
        else:
            return_results["return_value"] = 1
            return_results["message"] = f"Exec step bash command success!"
        return return_results
    
    def get_step_all_file_info(self) -> ReturnCode:
        
        results = ReturnInfo(code=ReturnCode.SUCCESS, message="Get step all file info success.", data={})
        
        log_server = LogTools()
        log_info = f"Get Task {self.task_name} ; Step {self.step_name} all file info of {self.step_name}."
        log_server.write_log(log=LogModel(log_info, "INFO"))
        
        self.init_at_workspace()
        
        step_files = {
            "script_file_path": self.script_file_path,
            "script_exec_input_file_path": self.script_exec_input_file_path,
            "script_exec_output_file_path": self.script_exec_output_file_path,
            "script_exec_log_file_path": self.script_exec_log_file_path
        }
        step_files_results = {}
        for name, file_path in step_files.items():
            one_file_info_result = {
                "file_path": file_path,
                "file_name": os.path.basename(file_path),
                "file_dir": os.path.dirname(file_path),
                "file_type": os.path.splitext(file_path)[1][1:],
            }
            file_info_result = IOTools().read_target_file(target_file_path=file_path)
            if file_info_result.get_code() != ReturnCode.SUCCESS:
                results.set_code(ReturnCode.FAILED)
                results.set_message(file_info_result.get_message())
                log_server.write_log(log=LogModel(file_info_result.get_message(), "ERROR"))
            one_file_info_result["file_info_result"] = file_info_result
            step_files_results[name] = one_file_info_result
        results.set_data(step_files_results)
        
        return results
        
    def edit_step_file(self, path_name:str, file_path:str, file_info:str) -> ReturnInfo:
        
        results = ReturnInfo(code=ReturnCode.SUCCESS, message="Edit step file success.", data={})
        
        log_info = f"Edit step file of {self.task_name} and {self.step_name}."
        log_server = LogTools()
        log_server.write_log(log=LogModel(log_info, "INFO"))
        
        log_info = f"Get Step All file info of {self.step_name}."
        log_server.write_log(log=LogModel(log_info, "INFO"))
        
        self.init_at_workspace()
        step_files = {
            "script_file_path": self.script_file_path,
            "script_exec_input_file_path": self.script_exec_input_file_path,
            "script_exec_output_file_path": self.script_exec_output_file_path,
            "script_exec_log_file_path": self.script_exec_log_file_path
        }
        
        if path_name not in step_files.keys():
            log_info = f"Path name {path_name} is not in step files."
            log_server.write_log(log=LogModel(log_info, "ERROR"))
            results.set_code(ReturnCode.FAILED)
            results.set_message(log_info)
            return results
        else:
            log_info = f"Path name {path_name} is in step files."
            log_server.write_log(log=LogModel(log_info, "INFO"))
            
            step_file_path = step_files.get(path_name, "")
            
            log_info = f"Begin edit file: {path_name} in step file: {step_file_path}..."
            log_server.write_log(log=LogModel(log_info, "INFO"))
            
            log_info = f"Read Step All file info of {self.step_name}, file_path: {file_path}."
            log_server.write_log(log=LogModel(log_info, "INFO"))
            old_file_info_result = IOTools().read_target_file(target_file_path=file_path)
            if old_file_info_result.get_code() != ReturnCode.SUCCESS:
                results.set_code(ReturnCode.FAILED)
                results.set_message(old_file_info_result.get_message())
                log_server.write_log(log=LogModel(old_file_info_result.get_message(), "ERROR"))
                return results
            else:
                log_info = f"Read step file: {path_name} in step file: {step_file_path} Success."
                log_server.write_log(log=LogModel(log_info, "INFO"))
                old_file_info_result.set_message(f"Edit file: {path_name} in step file: {step_file_path}.")
                
                log_info = f"Write step file: {path_name} in step file: {step_file_path}."
                log_server.write_log(log=LogModel(log_info, "INFO"))
                
                new_file_info_result = IOTools().write_target_file(target_file_path=file_path, content=file_info)
                if new_file_info_result.get_code() != ReturnCode.SUCCESS:
                    log_info = f"Write step file: {path_name} in step file: {step_file_path} failed."
                    log_server.write_log(log=LogModel(log_info, "ERROR"))
                    results.set_code(ReturnCode.FAILED)
                    results.set_message(new_file_info_result.get_message())
                    return results
                else:
                    log_info = f"Write step file: {path_name} in step file: {step_file_path} success."
                    log_server.write_log(log=LogModel(log_info, "INFO"))
                    
                    results.set_code(ReturnCode.SUCCESS)
                    results.set_message(log_info)
                    new_file_info_result = IOTools().read_target_file(target_file_path=file_path)
                    results.set_data({"old_file_info_result": old_file_info_result, "new_file_info_result": new_file_info_result})
        return results