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

once the client is launched, you can choose a csv file to use to display server information with the "Choose a file" button.
If you don't have a CSV file or want to create a new one, you can directly add a new server by entering its ip and port in the corresponding fields and clicking on the "Add" button. It will automatically create a new CSV file called "servers.csv" in the actual directory and add the server to it.

After that, you can choose a server to connect to in the list, and connect to it by double-clicking it in the list.

You can add a server to the list by enterings the correpondings information in the fields above the list, then you can click on the "Add" button to add the new server to the list.

<a href="https://ibb.co/9wX3ZVT"><img src="https://i.ibb.co/vs5vXQP/Capture-d-cran-2022-12-30-13-42-59.png" alt="Capture-d-cran-2022-12-30-13-42-59" border="0" width="200" height="400"></a>

Once connected, you can send a command to the server by entering it in the "Command" field and pressing enter key.

<a href="https://ibb.co/QP9HVQX"><img src="https://i.ibb.co/F56Y13n/Capture-d-cran-2022-12-30-13-51-16.png" alt="Capture-d-cran-2022-12-30-13-51-16" border="0" width="400" hieght="700"></a>

#### Here is a list of the  predifined commands that can be sent to the server:

| Command | Description |
| ------- | ----------- |
| help    | Display the list of commands |
| os      | Retrieve the server OS and version |
| cpu     | Retrieve the server CPU usage in percent |
| ram     | Retrieve the different server RAM usage in percent |
| hostname| Retrieve the server hostname |
| ip      | Retrieve the server IP address |
| python --version | Retrieve the server python version |
| ping <address> | Ping the server |
| clear   | Clear the terminal |
| disconnect | Disconnect from the server |
| connexion information | Retrieve the server's ip and name |
| kill   | Kill the server |
| reset  | Reset the server |
| exit    | Disconnect from the server |

#### There are commands specific to the os of the server:

##### For windows:

| Command | Description |
| ------- | ----------- |
| DOS:dir  | Retrieve the list of files and folders in the current directory |
| DOS:mkdir <folder name> | Create a folder in the current directory |
| DOS:cd <folder name> | Change the current directory |
| DOS:del <file name> | Delete a file in the current directory |
| DOS:rd <folder name> | Delete a folder in the current directory |
| powershell: get-process | Retrieve the list of processes running on the server |
| powershell: stop-process <process name> | Stop a process running on the server |

##### For linux:

| Command | Description |
| ------- | ----------- |
| linux: ls | Retrieve the list of files and folders in the current directory |
| linux: rm <file name> | Delete a file in the current directory |
| linux: rmdir <folder name> | Delete a folder in the current directory |

