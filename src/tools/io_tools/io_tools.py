#!/usr/bin/env python
import os
import sys


class IOTools():

    def __init__(self):
        pass    

    def get_folder_names_from_path(self, target_path: str) -> list:
        try:
            # 使用 os.listdir 获取目标路径下的所有文件和文件夹
            items = os.listdir(target_path)
            
            # 过滤出仅包含文件夹的名称，并返回结果列表
            folder_names = [item for item in items if os.path.isdir(os.path.join(target_path, item))]
            
            return folder_names
        except Exception as e:
            print(f"Error occurred: {e}")
            return []

    def check_target_folder_exist(self, target_folder_path: str) -> bool:

        if not os.path.exists(target_folder_path):
            return False
        else:
            return True
        
    def create_target_folder(self, target_folder_path: str) -> dict:
        """
        创建目标文件夹

        :param target_folder_path: 目标文件夹路径
        :return: 0: 创建成功; 1: 创建失败; -1: 目标文件夹已存在
        """
        return_value  = 1
        massage = f"create target file path: {target_folder_path}"
        # 如果目标文件夹存在,返回错误
        if self.check_target_folder_exist(target_folder_path=target_folder_path):
            return_value = -1
            massage += f", target file already exists!"
        else:
            os.makedirs(target_folder_path)
            if self.check_target_folder_exist(target_folder_path=target_folder_path):
                return_value = 0
                massage += f", create success!"
            else:
                return_value = 1
                massage += f", create failed!"
        return_info = {
            "return_value": return_value,
            "massage": massage
        }
        return return_info
    

    def create_target_file(self, target_file_path: str) -> dict:
        """
        创建目标文件

        :param target_file_path: 目标文件路径
        :return: 0: 创建成功; 1: 创建失败; -1: 目标文件已存在
        """
        return_value  = 1
        massage = f"create target file path: {target_file_path}"
        # 如果目标文件存在,返回错误
        if os.path.exists(target_file_path):
            return_value = -1
            massage += f", target file already exists!"
        else:
            open(target_file_path, 'w').close()
            if os.path.exists(target_file_path):
                return_value = 0
                massage += f", create success!"
            else:
                return_value = 1
                massage += f", create failed!"
        return_info = {
            "return_value": return_value,
            "massage": massage
        }
        return return_info
