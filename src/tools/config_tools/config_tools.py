#!/usr/bin/env python
import os
import sys


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
            config = eval(f.read())

        return config
    
    def get_log_folder_path(self) -> str:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        
        return self.config_dict.get("log_folder_path", "")
    
    def get_source_folder_path(self) -> str:

        if self.config_dict is None:
            self.config_dict = self.get_config()
        
        return self.config_dict.get("source_folder_path", "")
    
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
    


