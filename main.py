from pathlib import Path
from pprint import pprint
from client import Client
import time
import os
import platform
import json
import pickle

class HomeLogger:
    DEFAULT_STATE = False
    def __init__(self) -> None:
        self.path = Path(os.path.dirname(__file__))

        try:
            with open(self.path.joinpath('clients.json'), "r", encoding="utf-8") as f:
                self.clients_dict:dict = json.loads(f.read())
        except FileNotFoundError:
            print('No clients to track')
            print('Quiting...')
            exit()

        try:
            with open(self.path.joinpath('lastState.pkl'), 'rb') as f:
                self.last_state:list[Client] = list(pickle.load(f))
        except FileNotFoundError:
            self.last_state = []
            for client in self.clients_dict:
                cl = Client(client, self.clients_dict[client], self.DEFAULT_STATE)
                self.last_state.append(cl)

            with open(self.path.joinpath('lastState.pkl'), 'wb') as f:
                pickle.dump(self.last_state, f)
            
        self.main()

    def main(self):
        while True:
            with open(self.path.joinpath('lastState.pkl'), 'rb') as f:
                self.last_state:list[Client] = pickle.load(f)

            for i, client in enumerate(self.last_state):
                if client.update(self.ping(client.host)):
                    with open(self.path.joinpath('tracks.log'), 'a') as f:
                        f.write(str(client)+'\n')
                self.last_state[i] = client

            with open(self.path.joinpath('lastState.pkl'), 'wb') as f:
                pickle.dump(self.last_state, f)
        
            # time.sleep(60)


    def ping(self, host: str) -> bool:
        return os.system(f"ping {'-n' if platform.system().lower()=='windows' else '-c'} 1 {host}") == 0


HomeLogger()
