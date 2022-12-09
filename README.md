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
- Install python 3.x

    You can download it from [python.org](https://www.python.org/downloads/)

- Install pip

    Usually, pip is automatically installed if you are:

    - working in a virtual environment
    - using Python downloaded from python.org
    - using Python that has not been modified by a redistributor to remove ensurepip

    If pip is not installed, you can install it by running the following command:

    ```bash
    python get-pip.py
    ```

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

Then the server will be launched and will wait for clients to connect.

## Client side

### Usage
```bash
python client.py
```

### In application usage

once the client is launched, you can choose a csv file to use to display server information.

After that, you can choose a server in  the list then click on the "Connect" button

You can also manually enter the server's ip and port in the corresponding fields and click on the "Connect" button.
After entering the server's ip and port, you can click on the "Add" button to add the server to the list.

Once connected, you can send a command to the server by entering it in the "Command" field and pressing enter key.

Here is a list of the  predifined commands that can be sent to the server:

| Command | Description |
| ------- | ----------- |
| help    | Display the list of commands |
| os      | Retrieve the server OS and version |
| cpu     | Retrieve the server CPU usage in percent |
| ram     | Retrieve the different server RAM usage in percent |
| hostname| Retrieve the server hostname |
| ip      | Retrieve the server IP address |
| clear   | Clear the terminal |
| exit    | Disconnect from the server |

There are commands specific to the os of the server:

For windows:

| Command | Description |
| ------- | ----------- |
| MS:dir  | Retrieve the list of files and folders in the current directory |

