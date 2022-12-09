# SAE-3.02-Surveillance-Postes-Clients-ou-serveurs
This is a project to create a surveillance system for the SAE-3.02 course at the University of Colmar.

## Requirements
- Python 3.6
- pip
- psutil
- platform
- socket
- threading
- subprocess

## Installation
- Install python 3.6

https://www.python.org/downloads/

- Install pip

- Install the requirements
```bash
pip install -r requirements.txt
```

## Server side

### Usage
```bash
python server.py -p <port>
```

### Options

| Option | Description |
| ------ | ----------- |
| -p     | Port to use |

## Client side

### Usage
```bash
python client.py
```

### Options

| Option | Description |
| ------ | ----------- |
| -h     | Show help |
| -p     | Port to use |
| -s     | Server IP address |