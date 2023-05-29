import time, os, platform, json, pickle
from pathlib import Path
from pprint import pprint

class HomeLogger:
    def __init__(self) -> None:
        self.path = Path(os.path.dirname(__file__))

        try:
            with open(self.path.joinpath('clients.json'), "r", encoding="utf-8") as f:
                self.clients = json.loads(f.read())
        except FileNotFoundError:
            print('No clients to track')
            print('Quiting...')
            exit()

        try:
            with open(self.path.joinpath('lastState.pkl'), 'rb') as f:
                self.last_state = pickle.load(f)
        except FileNotFoundError:
            self.last_state = {}
            for client in self.clients:
                self.last_state[client] = False
            print(self.last_state)
            with open(self.path.joinpath('lastState.pkl'), 'wb') as f:
                pickle.dump(self.last_state, f)

        self.main()

    def main(self):
        while True:
            with open(self.path.joinpath('lastState.pkl'), 'rb') as f:
                self.last_state = pickle.load(f)

            for client in self.clients:
                res = self.ping(self.clients[client])
                if res != self.last_state[client]:
                    self.last_state[client] = res
                    current_time = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime())

                    with open(self.path.joinpath('log.log'), 'a') as f:
                        f.write(f'{current_time}|{client}|{res}\n')

            with open(self.path.joinpath('lastState.pkl'), 'wb') as f:
                pickle.dump(self.last_state, f)
        
            time.sleep(60)


    def ping(self, host) -> bool:
        return os.system(f"ping {'-n' if platform.system().lower()=='windows' else '-c'} 1 {host}") == 0


HomeLogger()
