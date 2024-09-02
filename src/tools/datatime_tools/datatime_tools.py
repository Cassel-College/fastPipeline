#! /usr/bin/env python3

from datetime import datetime

class DatetimeTools:
    def __init__(self):
        pass
    
    def get_now_YYYY_MM_DD_HH_MM_SS(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_now_YYYY_MM_DD(self) -> str:
        return datetime.now().strftime("%Y-%m-%d")
    
    def get_now_HH_MM_SS(self) -> str:
        return datetime.now().strftime("%H:%M:%S")
    