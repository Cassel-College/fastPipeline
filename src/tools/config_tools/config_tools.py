#!/usr/bin/env python
import os
import sys
import json  # 添加这个导入


class ConfigTools(object):

    def __init__(self):

        self.exec_root_path = os.getcwd()
        self.config_file_path = os.path.join(self.exec_root_path, "src/config.json")
        self.config_dict = None

    def get_config(self) -> dict:
        
        config = {}

        if not os.path.exists(self.config_file_path):
            raise FileNotFoundError(f"config file: {self.config_file_path} not found!")

        with open(self.config_file_path, "r") as f:
            config = json.load(f)  # 使用 json.load 代替 eval

        return config
    
    def get_log_folder_path(self) -> str:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        log_folder_path = os.path.join(self.exec_root_path, self.config_dict.get("log_folder_path", ""))
        return log_folder_path
    
    def get_source_folder_path(self) -> str:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        source_folder_path = os.path.join(self.exec_root_path, self.config_dict.get("source_folder_path", ""))
        return source_folder_path
    
    def get_input_file_name(self) -> str:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        
        return self.config_dict.get("input_file_name", "")
    
    def get_output_file_name(self) -> str:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        
        return self.config_dict.get("output_file_name", "")

    def get_step_log_file_name(self) -> str:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        
        return self.config_dict.get("step_log_file_name", "")
    
    def get_script_engine(self) -> str:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        
        return self.config_dict.get("script_engine", "")
    
    def get_environment(self) -> str:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        
        return self.config_dict.get("environment", "")

    def get_dev_mode(self) -> dict:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        
        return self.config_dict.get("dev_mode", {})

    def get_dev_mode_open(self) -> bool:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        
        return self.config_dict.get("dev_mode", {}).get("open", False)
    
    def get_dev_mode_print_log_in_terminal(self) -> bool:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        
        return self.config_dict.get("dev_mode", {}).get("print_log_in_terminal", False)
