<h1 align = "center">
    <br>
    <img src="https://i.ibb.co/dWvj19V/Sans-titre-3.png" alt="Sans-titre-3" border="0" width="300">
    <br>
    SAE-3.02-Surveillance-Postes-Clients-ou-serveurs
    <br>
</h1>

<h2 align="center">Programmer Documentation</h2>

<p align="center">
    <a href="#Server">Add a new feature to the server</a> •
    <a href="#Client">Add a new feature to the client</a> •
    <a href="#App">Add a new feature to the GUI</a>
</p>



<h3 align="center">Project Presentation</h3>

<p align="center">
This project is a Python based GUI app made with PyQt to monitor a server's resources and send commands to it using sockets. It consists of two parts: the server and the client. The server is the one that will receive the command from the client and execute it. The server will also send the data to the client. The client is the one that will send the command to the server and receive the data from the server and display it to the user. This repository contains the server.py file that contains the server and the client.py file that contains the client. It also contains the requirements.txt file that contains the requirements to run the app and the README.md file that contains the documentation of the app to explain how to use it.
</p>

#


<h3 align="center">How to add a new feature to the app</h3>

#


<h4 id="Server" align="center">1. Add the feature to the server</h4>

The server is the one that will receive the command from the client and execute it. The server will also send the data to the client.

The server is located in the `server.py` file.

It consists of three functions:

- `get_infos()`: This function is used to get informations about the server's resources. It returns variables that will be sent to the client when the client asks for them.
- `handler()`: This function is used to handle when the user try to exit the app. It will display an input line to ask the user if he really wants to exit the app. It can prevent from closing the app by mistake.
- `server()`: This function is used to start the server. First of all, it will handle the way the user start the script. If the user starts the script with anything but the `-p` argument, it will display an error message and guide the user to the right way to start the script. It will also handle the port set by the user. If the user doesn't set a valid port, like a string or a number that is not between 0 and 65535, it will display an error message and guide the user to the right way to start the script. If the user set a valid port, it will start the server and wait for the client to connect. When the client connects, it will start enter a loop that will wait for the client to send a command. When the client sends a command, it will execute it and send the result to the client. When the client disconnects, it will display a message to inform the user that the client disconnected and it will wait for a new client to connect.

To add a new command to the server, you have to add a new `elif` statement in the `server()` function. The `elif` statement will check if the command sent by the client is the command you want to add. If it is, it will execute the command and send the result to the client. If it isn't, it will check for other elif statements.

To do that, you can find a commented example at the line 153. You juste have to uncomment it and change the command and the result. You can also add a new elif statement after the commented example if you want to add more commands.

<p align="center">
  <a href="https://ibb.co/SXWRcLm"><img src="https://i.ibb.co/KjRFD1s/carbon.png" alt="carbon" border="0" width="800" height="125"></a>
</p>

#
#
#


<h4 id="Client" align="center">2. Add the feature to the client</h4>

The client is the one that will send the command to the server and receive the data from the server.

The client is located in the `client.py` file.

It consists of a class called `UI` that contains all the functions used to create the socket, send the command to the server and receive the data from the server.

The functions are:

- `__init__()`: This function is used to initialize the class. It will contains all the GUI elements and variables.
- `connect()`: This function is used to connect to the server. It will create the socket and connect to the server. It will also start the thread that will receive the data from the server.
- `send()`: This function is used to send the command to the server. It will send the command to the server in order to execute it.
- `receive()`: This function is used to receive the data from the server. It will receive the data from the server and display it in the GUI. It also contains a loop that will wait for the server to send data. When the server sends data, it will display it in the GUI. It works as a thread.
- `Scroll()`: This function is used to scroll the text in the GUI. It will scroll the text in the GUI when the user clicks on the scroll bar. and it will also scroll the text to the bottom when the user sends a command.
- `CSVupdate()`: This function is used to update List containing the data from the CSV file. It will update the list containing the data from the CSV file when the user try to add a new server to the list.
- `getfile()`: This function is used to get the CSV file. It will open a window to ask the user to select the CSV file. It will also update the list containing the data from the CSV file. If no file is selected, it will display an error message indicating that the user has to select a file.
- `addserver()`: This function is used to add a server to the CSV file. When the user clicks on the `Add Server` button, it will add the ip and the port of the server to the CSV file in order to make it appear in the list of servers. If the user doesn't enter a valid ip or a valid port, it will display an error message indicating that the user has to enter a valid ip and a valid port.It will also create a new local CSV file if the user doesn't selected one before.
- `closeEvent()`: This function is used to handle when the user try to exit the app. It will display a message box to ask the user if he really wants to exit the app. It can prevent from closing the app by mistake. It will also properly stop the thread that receives the data from the server.

To add a new command to the client, you have to uncomment the commented example at the line 321 in the `send()` function. You just have to change the command and the result. You can also add a new elif statement after the commented example if you want to add more commands.

You can also add a new variable in the `__init__()` function. You just have to add your variable at the line 127, an example is already there. This is the same if you want to add an action. You just have to add the action at the line 128

#
#
#

<h4 id="App" align="center">3. Add the feature to the GUI</h4>

The GUI is the one that will display the data from the server and send the command to the server.

It is created with the PyQt5 library.

It is composed of a class called `UI` that contains all the Widgets and functions used to create the GUI.

The created Widgets are:

- `self.MainFrame`: This is the main layout of the app. It contains all the other Widgets and layouts.
- `self.LeftBar`: This is the left bar of the app. It contains two other layouts: `self.LeftBarTop` and `self.LeftBarBottom`.
- `self.LeftBarTop`: This is the top part of the left bar. It contains the `self.ServerList` Widget.
- `self.LeftBarBottom`: This is the bottom part of the left bar. It contains the `self.AddServer` button and the `self.Host` and `self.Port` Inputs.
- `self.EmptyTextBox`: This is an empty text box. It is used to create some space between the `self.ServerList` and the top of the window.
- `self.SecondLabel`: This is the label that contains the text `Server List`.
- `self.RightBar`: This is the right bar of the app. It contains the `self.Response` and the `self.Command` Widgets.
- `self.ServerList`: This is the list of servers. It contains the list of servers that the user can connect to.
- `self.ChooseFile`: This is the button that the user can click to select the CSV file that contains the list of servers.
- `self.AddServer`: This is the button that the user can click to add a server to the list of servers.
- `self.Host`: This is the input that the user can use to enter the ip of the server he wants to connect to.
- `self.Port`: This is the input that the user can use to enter the port of the server he wants to connect to.
- `self.Response`: This is the text area that the user can use to display the data from the server.
- `self.Command`: This is the input that the user can use to enter the command he wants to send to the server.

If you want to add a new Widget to the GUI, you can add it in the `__init__()` function. You can find an example at the lines 32 to 34. You just have to uncomment it and change the name of the Widget. You can also edit its properties in the `__init__()` function too, there is an example at the lines 80 to 83, you just have to uncomment it, change the name of the Widget and change the properties.

To make your widget appear in the GUI, you have to add it to a layout. You can find an example at the lines 109 to 111. You just have to uncomment it, change the name of the Widget and change the layout. You can also add a new layout if you want to add more Widgets. You juste have to add this created layout to the `self.MainFrame` layout at the line 114.