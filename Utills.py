import datetime
from datetime import time


class Utills:
    @staticmethod
    def current_time_ms():
        return datetime.datetime.now().strftime("%a-%m-%y - %H:%M:%S.%f")