import os


from src.model.log_model import LogModel
from src.model.return_info import ReturnCode, ReturnInfo
from src.tools.config_tools.config_tools import ConfigTools
from src.tools.io_tools.io_tools import IOTools
from src.model.step import Step
from src.tools.log_tools.log_tools import LogTools

class Task:
    
    def __init__(self, task_name: str):
        self.task_name = task_name
        self.task_dir = ""
        self.readme_path = ""
        self.paramater_path = ""
        self.log_path = ""
        self.config = ConfigTools()
        self.log_tools = LogTools()
    
        
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
                    log_info = f"Check task:{self.task_name} efficincy failed, step name {step_name} not in Step index."
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
    
    def select_all_task_name_core(self) -> ReturnInfo:

        log = LogModel(f"select all task name of {self.task_name}.", "INFO")
        self.log_tools.write_log(log)

        source_folder_path = self.config.get_source_folder_path()
        self.log_tools.write_log(LogModel(f"get folder names from path: {source_folder_path}.", "INFO"))

        folder_names = IOTools().get_folder_names_from_path(source_folder_path)
        return_info = ReturnInfo.create(ReturnCode.SUCCESS, "get task names success", {"folder_names": folder_names})
        return return_info

    
    def create_target_folder(self, name: str, task_name: str) -> ReturnInfo:
        
        return_results = ReturnInfo.create(ReturnCode.FAILED, f"create {name} failed", {})
        log_info = f"create {name} of task:{task_name}."
        log = LogModel(log_info, "INFO")
        self.log_tools.write_log(log)
        
        io_tools = IOTools()
        source_folder_path = self.config.get_source_folder_path()
        task_dir = os.path.join(source_folder_path, task_name)
        results = io_tools.create_target_folder(task_dir)
        
        if results.get_code() == 0:
            log_info = f"create {name} success!"
            return_results.set_code(ReturnCode.SUCCESS)
            return_results.set_message(f"create {name} success")
            return_results.set_data({f"{name}_path": task_dir})
        elif results.get_code() == 1:
            log_info = f"create {name} failed!" + results.get_message()
            return_results.set_code(ReturnCode.FAILED)
            return_results.set_message(results.get_message())
            return_results.set_data({})
        elif results.get_code() == -1:
            log_info = f"create {name} failed!" + results.get_message()
            return_results.set_code(ReturnCode.FAILED)
            return_results.set_message(results.get_message())
            return_results.set_data({})
        else:
            log_info = f"create {name} failed!" + results.get_message()
            return_results.set_code(ReturnCode.FAILED)
            return_results.set_message(f"create {name} failed")
            return_results.set_data({})
        log = LogModel(log_info, "INFO")
        self.log_tools.write_log(log)
        return return_results
    
    def create_target_file(self, name: str, file_name: str) -> ReturnInfo:
        
        return_results = ReturnInfo.create(ReturnCode.FAILED, f"create task {name} failed", {})
        log_info = f"create task {name} of {self.task_name}."
        log = LogModel(log_info, "INFO")
        self.log_tools.write_log(log)
        io_tools = IOTools()
        source_folder_path = self.config.get_source_folder_path()
        task_dir = os.path.join(source_folder_path, self.task_name)
        readme_md_path = os.path.join(task_dir, file_name)    
        results = io_tools.create_target_file(readme_md_path)
        if results.get_code() == ReturnCode.SUCCESS:
            log_info = f"create task {name} success!"
            return_results.set_code(ReturnCode.SUCCESS)
            return_results.set_message(f"create task {name} success")
            return_results.set_data({f"{name}_path": readme_md_path})
        else:
            log_info = f"create task {name} failed!"    
            return_results.set_code(ReturnCode.FAILED)
            return_results.set_message(f"create task {name} failed")
            return_results.set_data({})
        log = LogModel(log_info, "INFO")
        self.log_tools.write_log(log)
        return return_results
    
    def create_task_folder(self) -> ReturnInfo:
        
        name = "task_folder"
        task_name = self.task_name
        return self.create_target_folder(name, task_name)
    
    def create_task_readme(self) -> ReturnInfo:
        
        name = "readme"
        file_name = "README.md"
        return self.create_target_file(name, file_name)
    
    def create_task_index(self) -> ReturnInfo:
        
        name = "task_index"
        file_name = "index.json"
        return self.create_target_file(name, file_name)
    
    def create_task_log(self) -> ReturnInfo:

        name = "task_log"
        file_name = "log.txt"
        return self.create_target_file(name, file_name)
    
    def create_task_config(self) -> ReturnInfo:
        
        name = "task_config"
        file_name = "config.json"
        return self.create_target_file(name, file_name)
    
    def gen_task_file_path(self, file_name: str, file_type: str) -> ReturnInfo:
        task_dir = self.task_dir
        file_path = os.path.join(task_dir, file_name)
        setattr(self, f"{file_type}_path", file_path)
        log = LogModel(f"gen task {file_type} path: {file_path}.", "INFO")
        self.log_tools.write_log(log)
        return_results = ReturnInfo.create(ReturnCode.SUCCESS, f"gen task {file_type} path success", {f"{file_type}_path": file_path})
        return return_results

    def gen_task_dir_path(self) -> ReturnInfo:
        source_folder_path = self.config.get_source_folder_path()
        task_dir = os.path.join(source_folder_path, self.task_name)
        self.log_tools.write_log(LogModel(f"gen task dir: {task_dir}.", "INFO"))
        self.task_dir = task_dir
        return_results = ReturnInfo.create(ReturnCode.SUCCESS, "gen task dir success", {"task_dir": task_dir})
        return return_results

    def gen_task_readme_path(self) -> ReturnInfo:
        return self.gen_task_file_path("README.md", "readme")

    def gen_task_index_path(self) -> ReturnInfo:
        return self.gen_task_file_path("index.json", "index")
        
    def gen_task_log_path(self) -> ReturnInfo:
        return self.gen_task_file_path("log.txt", "log")
    
    def gen_task_paramater_path(self) -> ReturnInfo:
        return self.gen_task_file_path("paramater.json", "paramater")
    
    def init_for_create(self):
        results = ReturnInfo(code=ReturnCode.FAILED, message="init task failed.", data={})
        
        steps = [
            ("dir", self.gen_task_dir_path),
            ("readme", self.gen_task_readme_path),
            ("index", self.gen_task_index_path),
            ("log", self.gen_task_log_path),
            ("parameter", self.gen_task_paramater_path)
        ]
        for step_name, step_function in steps:
            step_result = step_function()
            if step_result.code != ReturnCode.SUCCESS:
                error_message = f"Gen task {step_name} path failed."
                results.set_message(error_message)
                self.log_tools.write_log(LogModel(error_message, "ERROR"))
                return results
        
        results.set_code(ReturnCode.SUCCESS)
        
        results.add_data(key="log_path", value=f"{self.log_path}")
        results.add_data(key="readme_path", value=f"{self.readme_path}")
        results.add_data(key="index_path", value=f"{self.index_path}")
        results.add_data(key="paramater_path", value=f"{self.paramater_path}")
        results.add_data(key="task_dir", value=f"{self.task_dir}")

        self.log_tools.write_log(LogModel("Init task success.", "INFO"))
        print(self.__dict__)
        return results


    def create(self) -> ReturnInfo:
        """
        创建任务
        """
        return_results = ReturnInfo.create(ReturnCode.SUCCESS, "create task success", {})
        
        # 1. create task folder
        create_task_folder_results = self.create_task_folder()
        if create_task_folder_results.get_code() == ReturnCode.SUCCESS:
            return_results = create_task_folder_results
            return_results.add_data("task_folder_path", create_task_folder_results.get_data().get("task_dir", ""))
        else:
            return_results = ReturnInfo.create(ReturnCode.FAILED, "create task folder failed", {})
            return return_results
        
        # 2. create task readme file
        if create_task_folder_results.get_code() == ReturnCode.SUCCESS:
            create_readme_results = self.create_task_readme()
            return_results.add_data("readme_path", create_readme_results.get_data().get("readme_path", ""))
        else:
            create_readme_results = ReturnInfo.create(ReturnCode.FAILED, "create task folder failed", {})
            return create_readme_results
        
        # 3. create task index file
        if create_readme_results.get_code() == ReturnCode.SUCCESS:
            create_index_results = self.create_task_index()
            return_results.add_data("task_index_path", create_index_results.get_data().get("index_path", ""))
        else:
            create_index_results = ReturnInfo.create(ReturnCode.FAILED, "create readme failed", {})
            return create_index_results
        
        # 4. create task log file
        if create_index_results.get_code() == ReturnCode.SUCCESS:
            create_log_results = self.create_task_log()
            return_results.add_data("task_log_path", create_log_results.get_data().get("log_path", ""))
        else:
            create_log_results = ReturnInfo.create(ReturnCode.FAILED, "create index failed", {})
            return create_log_results
        
        # 5. create task config file
        if create_log_results.get_code() == ReturnCode.SUCCESS:
            create_config_results = self.create_task_config()
            return_results.add_data("task_config_path", create_config_results.get_data().get("config_path", ""))
        else:
            create_config_results = ReturnInfo.create(ReturnCode.FAILED, "create log failed", {})
            return create_config_results
        
        return return_results