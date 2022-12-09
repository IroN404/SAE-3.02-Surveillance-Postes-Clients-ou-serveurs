# SAE-3.02-Surveillance-Postes-Clients-ou-serveurs
This is a project to create a surveillance system for the SAE-3.02 course at the University of Colmar.

## Server side
The server side is a python script that will run on a server. It will be used to send the data to the client side.

### Requirements
- Python 3.6
- pip
- psutil
- platform
- socket
- threading
- subprocess

### Installation
- Install python 3.6

- Install pip

- Install the requirements
```bash
pip install -r requirements.txt
```

- Run the server
```bash
python server.py -p <port>
```

## Client side