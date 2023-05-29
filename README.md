# Wifi tracker
Tracking if client is connected to same network and writing it into log file
## Run Locally

Clone the project

```bash
  git clone https://github.com/Derday/Wifi_tracker.git
```

Go to the project directory

```bash
  cd Wifi_tracker
```

Create `clients.json` containing names of clients and their IP addresses

```json
{
    "name1":"1.1.1.1",
    "name2":"2.2.2.2"
}
```

Start the server

```bash
  python main.py
```

