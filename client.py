from pathlib import Path
import time

class Client:
    def __init__(self, client:str = None, host:str = None, state:bool = None) -> None:
        self.client = client
        self.host = host
        self.state = state
        self.curr_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


    def update(self, state: bool) -> bool:
        if state != self.state:
            self.curr_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            self.state = state
            return True
        return False
    
    def __str__(self) -> str:
        return (f'{self.curr_time}|{self.client}|{self.state}')