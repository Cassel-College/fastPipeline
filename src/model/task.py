import os


from src.tools.config_tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools


class Task:
    
    def __init__(self, task_name: str):
        self.task_name = task_name
        self.config = ConfigTools()
        
        
    def get_all_step_name(self) -> dict:
        
        return_value = 0
        source_folder_path = self.config.get_source_folder_path()
        abs_task_path = os.path.join(source_folder_path, self.task_name)
        step_names = IOTools().get_folder_names_from_path(abs_task_path)
        return_value = 1
        return_results = {
            "return_value": return_value,
            "step_names": step_names
        }
        return return_results