#! /usr/bin/env python3

class ReturnInfo:
    def __init__(self, code: int, message: str, data: int):
        self.code = code
        self.message = message
        self.data = data
        
    def get_code(self) -> int:
        return self.code
    
    def get_message(self) -> str:
        return self.message
    
    def get_data(self) -> int:
        return self.data
    
    def get_return_info(self) -> dict:
        return {"code": self.code, "message": self.message, "data": self.data}