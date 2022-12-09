<h1 align = "center">
    <br>
    <img src="https://i.ibb.co/dWvj19V/Sans-titre-3.png" alt="Sans-titre-3" border="0" width="300">
    <br>
    SAE-3.02-Surveillance-Postes-Clients-ou-serveurs
    <br>
</h1>

<h4 align="center">A Python based GUI app made with PyQt to monitor a server's resources and send commands to it.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#Requirements">Requirements</a> •
  <a href="#Installation">Installation</a> •
  <a href="#Server Side">Server Side Usage</a> •
  <a href="#Client Side">Client Side Usage</a> •
  <a href="#license">License</a>
</p>

## Key Features

* Monitor a server's resources
* Send commands to the server
* Save the server's ip and port in a csv file
* Connect to a server by entering its ip and port
* Connect to a server by choosing it from a list

## Requirements
- Python 3.6
- pip
- psutil
- socket
- threading

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

## Server Side

### Usage
```bash
python server.py -p <port>
```
<img margin-left=auto margin-right=auto src="https://i.ibb.co/NYvBhcP/CMD.gif" alt="CMD" border="0">

### Options

| Option | Description |
| ------ | ----------- |
| -p     | Port to use |

Then the server will be launched and will wait for clients to connect.

## Client Side

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

#### Here is a list of the  predifined commands that can be sent to the server:

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

#### There are commands specific to the os of the server:

##### For windows:

| Command | Description |
| ------- | ----------- |
| MS:dir  | Retrieve the list of files and folders in the current directory |

##### For linux:

| Command | Description |
| ------- | ----------- |
| LS:dir  | Retrieve the list of files and folders in the current directory |

