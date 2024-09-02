import os


from src.model.return_info import ReturnInfo
from src.tools.config_tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools
from src.model.step import Step

class Task:
    
    def __init__(self, task_name: str):
        self.task_name = task_name
        self.readme_path = ""
        self.paramater_path = ""
        self.log_path = ""
        self.config = ConfigTools()
    
    def init_for_create(self):
        pass
        
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
    
    
    def check_task_exist(self) -> dict:
        
        check_status = {}
        task_path = os.path.join(self.config.get_source_folder_path(), self.task_name)
        if IOTools().check_target_folder_exist(task_path):
            check_status = {
                "return_value": 1,
                "task_path": task_path
            }
        else:
            check_status = {
                "return_value": 0,
                "task_path": task_path
            }
        return check_status
    
    def get_task_index_path(self) -> str:
        
        task_index_path = os.path.join(self.config.get_source_folder_path(), self.task_name, "task_index.json")
        return task_index_path
    
    def check_task_efficincy(self, task_full_info: dict) -> dict:
        """
        检查任务的有效性
        """
        log_info = f"Check task efficincy of {self.task_name}."
        print(log_info)
        step_index_names = task_full_info.get("step_index", [])
        step_names = task_full_info.get("task_full_info", {}).keys()
        
        task_efficincy = {
            "status": True,
            "message": ""
        }
        if len(step_index_names) != len(step_names):
            log_info = f"Check task efficincy of {self.task_name} failed, step index name not equal step name."
            print(log_info)
            task_efficincy["status"] = False
            task_efficincy["message"] = log_info
            
        else:
            for step_name in step_names:
                if step_name not in step_index_names:
                    log_info = f"Check task efficincy of {self.task_name} failed, step name {step_name} not in Step index."
                    print(log_info)
                    task_efficincy["status"] = False
                    task_efficincy["message"] = log_info
                    break
        return task_efficincy
    
    def get_task_index_info(self) -> dict:
        """
        获取task_index.json中的信息
        """
        log_info = f"Get task index info of {self.task_name}."
        print(log_info)
        task_index_path = self.get_task_index_path()
        task_index = IOTools().read_json_from_file(task_index_path)
        log_info = f"get task_index: {task_index}, from read json file: {task_index_path}."
        print(log_info)
        if task_index.get("return_code", 1) == 0:
            step_index = task_index.get("return_value", {})
            log_info = f"Get task index info of {self.task_name} success."
        else:
            step_index = {}
            log_info = f"Get task index info of {self.task_name} failed."
        print(log_info)
        return step_index
    
    def get_task_index_of_step_name(self, task_index_info: dict) -> list:
        """
        获取task_index.json中step的index,用step index排序,用step name显示
        """
        log_info = f"Get task index of step name of {self.task_name}."
        print(log_info)
        indexs_numbers = task_index_info.keys()
        print("indexs_numbers", indexs_numbers)
        indexs_numbers = sorted(indexs_numbers, key=lambda x: int(x))
        indexs = [task_index_info[index] for index in indexs_numbers]
        log_info = f"Get task index of step name of {self.task_name} success, indexs: {indexs}."
        print(log_info)
        return indexs
    
    def gen_readme_path(self) -> str:
        
        task_path = os.path.join(self.config.get_source_folder_path(), self.task_name)
        readme_md_path = os.path.join(task_path, "README.md")
        return readme_md_path
    
    def gen_paramater_path(self) -> str:
        
        task_path = os.path.join(self.config.get_source_folder_path(), self.task_name)
        paramater_path = os.path.join(task_path, "paramater.json")
        return paramater_path
    
    def create_readme(self) -> dict:
        """
        创建README文件夹和README.md文件
        """
        return_results = ReturnInfo(code=1, message="", data=None)
        readme_md_path = self.gen_readme_path()
        if not IOTools().check_file_exist(readme_md_path):
            IOTools().create_target_file(readme_md_path)
        return_results.code = 0
        return_results.message = "Create README success."
        return return_results
    
    def create_paramater(self) -> dict:
        """
        创建paramater.json文件
        """
        return_results = ReturnInfo(code=1, message="", data=None)
        paramater_path = self.gen_paramater_path()
        if not IOTools().check_file_exist(paramater_path):
            IOTools().create_target_file(paramater_path)
        return_results.code = 0
        return_results.message = "Create paramater success."
        return return_results
        
        
    def get_step_base_names(self) -> dict:
        
        config = ConfigTools()
        source_folder_path = config.get_source_folder_path()
        task_path = os.path.join(source_folder_path, self.task_name)
        folder_names = IOTools().get_folder_names_from_path(task_path)
        return_results = ReturnInfo(code=1, message="", data=folder_names)
        return return_results
    
    
    def get_task_full_info(self) -> dict:
        
        return_value = 0
        task_full_info = {}
        task_efficincy = {}
        log_info = f"Get task full info of {self.task_name}."
        print(log_info)
        step_names = self.get_all_step_name().get("step_names", [])
        for step_name in step_names:
            step = Step(self.task_name, step_name)
            step_full_info = step.get_step_full_info()
            task_full_info[step_name] = step_full_info
            
        # 获取step的index from task_index.json
        step_index_info = self.get_task_index_info()
        indexs = self.get_task_index_of_step_name(step_index_info)
        # check task info efficiency
        return_results = {
            "task_name": self.task_name,
            "readme_path": self.gen_readme_path(),
            "task_full_info": task_full_info,
            "step_index": indexs,
            "task_efficincy": task_efficincy,
            "return_value": return_value
        }
        return_results["task_efficincy"] = self.check_task_efficincy(return_results)
        return_results["return_value"] = 1
        return return_results
    
    
    def exec_task(self) -> dict:
        """
        执行任务
        """
        return_results = {
            "return_value": 0,
            "message": ""
        }
        
        log_info = f"Exec task of {self.task_name}."
        print(log_info)
        
        task_full_info = self.get_task_full_info()
        
        if task_full_info.get("return_value", 0) == 0:
            return_results["return_value"] = 0
            return_results["message"] = "Get task full info failed."
            log_info = f"Get task full info of {self.task_name} failed."
            print(log_info)
            return return_results
        else:
            log_info = f"Exec task of {self.task_name} success."
            print(log_info)
        print(task_full_info.get("task_efficincy", {}))
        if not task_full_info.get("task_efficincy", {}).get("status", False):
            log_info = f"Check task efficincy failed."
            print(log_info)
            return_results["return_value"] = 0
            return_results["message"] = log_info
            return return_results
        else:
            log_info = f"Check task efficincy success."
            print(log_info)
        log_info = f"Exec step of {self.task_name}."
        step_indexs = task_full_info.get("step_index", [])
        exec_status = True
        for step_name in step_indexs:
            log_info = f"Exec step of {self.task_name}: {step_name}."
            print(log_info)
            step = Step(self.task_name, step_name)
            step_return_results = step.exec_step()
            if step_return_results.get("return_value", 0) == 0:
                log_info = f"Exec step of {self.task_name}: {step_name} failed."
                print(log_info)
                return_results["return_value"] = 0
                return_results["message"] = log_info
                exec_status = False
                break
            else:
                log_info = f"Exec step of {self.task_name}: {step_name} success."
                print(log_info)
        if exec_status:
            return_results["return_value"] = 1
            log_info = f"Exec task of {self.task_name} success."
            print(log_info)
        return return_results