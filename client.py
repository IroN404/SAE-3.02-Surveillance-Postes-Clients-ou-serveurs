# Importation des modules
from PyQt6 import *
import csv, sys, socket
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import os
import threading
import time

# Create the application
class UI(QWidget):
    def __init__(self):
        # Create the window
        super().__init__()  # Call the QWidget constructor
        self.setWindowTitle("Surveillance poste client")    # Set the title
        self.setFixedWidth(750) # Set the width of the window
        self.setFixedHeight(500)    # Set the height of the window
        self.setStyleSheet("background-color: #131313")    # Set the background color
        # Create the differnt parts of the window
        self.MainFrame = QHBoxLayout() # Create the layout
        self.LeftBar = QVBoxLayout()    # Create the left bar
        self.LeftBarTop = QVBoxLayout() # Create the top part of the left bar
        self.LeftBarBottom = QVBoxLayout()  # Create the bottom part of the left bar
        self.RightBar = QVBoxLayout()   # Create the right bar
        # Create the differnt parts of the left bar
        self.ServerList = QListWidget() # Create the server table
        self.Response = QTextEdit()   # Create the label
        self.ChooseFile = QPushButton("Choose a file") # Create the button
        self.Host = QLineEdit()  # Create the input
        self.Port = QLineEdit()  # Create the input
        self.AddButton = QPushButton("Add a server") # Create the button
        self.Command = QLineEdit()   # Create the input
        self.ConnectionState = QLabel("Not Connected") # Create the label
        self.EmptyTextBox = QLabel("Server List")
        global secondlabel
        self.secondlabel = QLabel("Please choose a CSV file with the\nbutton above or start adding a server\nmanually to create a local CSV file")
        # Define Host attributes
        self.Host.setPlaceholderText("Host")
        self.Host.setStyleSheet("background-color: #000; color: #FFF;")
        self.Host.setFixedWidth(225)
        self.Host.setFixedHeight(30)
        # Define Port attributes
        self.Port.setPlaceholderText("Port")
        self.Port.setStyleSheet("background-color: #000; color: #FFF;")
        self.Port.setFixedWidth(225)
        self.Port.setFixedHeight(30)
        # Define Response attributes
        self.Response.setReadOnly(True)
        self.Response.setPlaceholderText("Server's reply will be displayed here")
        # Define AddButton attributes
        self.AddButton.setStyleSheet("background-color: #000; color: #FFF;")
        # Define ConnectionState attributes
        self.ConnectionState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ConnectionState.setStyleSheet("color: #FFF;padding: 20,0,0,0;color: red;")
        self.ConnectionState.setFixedHeight(30)
        # Define ChooseFile attributes
        #self.ChooseFile.setStyleSheet("background-color: #000; color: #FFF;padding: 0,0,0,20;border-top : 1px solid #FFF;")
        self.ChooseFile.setFixedWidth(250)
        self.ChooseFile.setFixedHeight(30)
        # Define ServerList attributes
        self.ServerList.setStyleSheet(" background-color: #000; color: #FFF;")
        # Define Respone attributes
        self.Response.setStyleSheet("background-color: #000; color: #FFF;")
        self.Response.setFixedWidth(500)
        # Define Command attributes
        self.Command.setStyleSheet("background-color: #000; color: #FFF;border-top : 1px solid #FFF;")
        self.Command.setPlaceholderText("Insert a command here : ")
        self.Command.setFixedHeight(30)
        self.Command.setFixedWidth(500)
        # Define EmptyTextBox attributes
        self.EmptyTextBox.setFixedHeight(50)
        self.EmptyTextBox.setStyleSheet("background-color: #000; color: #FFF;border-bottom : 1px solid #FFF;")
        self.EmptyTextBox.setFont(QFont("Arial", 20))
        self.EmptyTextBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Define secondlabel attributes
        self.secondlabel.setStyleSheet("background-color: #000; color: #FFF;padding: 20,20,0,0;")
        self.secondlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.secondlabel.setFont(QFont("Arial", 14))
        # Server list 
        self.LeftBar.addLayout(self.LeftBarTop) # Add the top part of the left bar to the left bar
        self.LeftBar.addLayout(self.LeftBarBottom)   # Add the bottom part of the left bar to the left bar
        self.LeftBarTop.addWidget(self.EmptyTextBox)
        self.LeftBarTop.addWidget(self.secondlabel)
        self.LeftBarTop.addWidget(self.ServerList)
        self.LeftBarTop.addWidget(self.ChooseFile)
        self.LeftBarTop.setContentsMargins(0, 0, 0, 20)
        # Server adding side
        self.LeftBarBottom.addWidget(self.Host)
        self.LeftBarBottom.addWidget(self.Port)
        self.LeftBarBottom.addWidget(self.AddButton)
        self.LeftBarBottom.addWidget(self.ConnectionState)
        self.LeftBarBottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LeftBarBottom.setSpacing(10)
        # Left Side
        self.LeftBar.setContentsMargins(0, 0, 0, 20)
        self.LeftBar.setSpacing(0)
        # Right Side
        self.RightBar.addWidget(self.Response)
        self.RightBar.addWidget(self.Command)
        self.RightBar.setContentsMargins(0, 0, 0, 0)
        self.RightBar.setSpacing(0)
        # Main Frame
        self.MainFrame.setContentsMargins(0, 0, 0, 0)
        self.MainFrame.addLayout(self.LeftBar)
        self.MainFrame.addLayout(self.RightBar)
        self.setLayout(self.MainFrame)
        # Define the actions
        self.ChooseFile.clicked.connect(lambda: self.getfile())
        self.AddButton.clicked.connect(lambda: self.AddServer())
        self.Command.returnPressed.connect(lambda: self.Send())
        self.ServerList.itemDoubleClicked.connect(lambda: self.connect())
        self.file = None
        self.rec = threading.Thread(target=self.Receive)
        self.rec.start() # Start the receive thread
        # Display the window
        self.show()

    def Receive(self):
        # wait for the server to send a message
        while True:
            try:
                self.Response.append(client_socket.recv(1024).decode())
            except:
                pass
            

    def CSVupdate(self):
        if self.file == "choosen":
            self.ServerList.clear()
            with open(ServerFileList[0], "r") as f:
                reader = csv.reader(f)
                for column in reader:
                    ip = column[0].split(";")
                    port = column[0].split(";")
                    self.ServerList.addItem("Address : " + ip[0] + " Port : " + port[1])
                    self.secondlabel.setText("Choose a server from the list above")
                    self.file = True
        elif self.file == "local":
            self.ServerList.clear()
            with open("SAE 3.02/ServerList.csv", "r") as f:
                reader = csv.reader(f)
                for column in reader:
                    ip = column[0].split(";")
                    port = column[0].split(";")
                    self.ServerList.addItem("Address : " + ip[0] + " Port : " + port[1])
                    self.secondlabel.setText("Choose a server from the list above")

    def getfile(self):
        global ServerFileList
        ServerFileList = QFileDialog.getOpenFileName(self, 'Open file', './',"CSV files (*.csv)")
        self.ServerList.clear()
        try:
            with open(ServerFileList[0], "r") as f:
                reader = csv.reader(f)
                for column in reader:
                    ip = column[0].split(";")
                    port = column[0].split(";")
                    self.ServerList.addItem("Address : " + ip[0] + " Port : " + port[1])
                    self.secondlabel.setText("Choose a server from the list above")
                    self.file = "choosen"
        except:
            self.Response.append("Please choose a valid file")

    
    def AddServer(self):
        if self.file == "choosen":
            if self.Host.text() == "" or self.Port.text() == "":
                self.Response.append("Please enter a valid IP and a valid PORT")
            elif self.Port.text().isdigit() == False:
                self.Response.append("Port must be a number")
            elif int(self.Port.text()) > 65535:
                self.Response.append("Port must be between 0 and 65535")
            else :
                self.Response.append("Server added to existing file")
                with open(ServerFileList[0], "a") as f:
                    # Write an new line in the CSV file
                        # if f is empty, write the first line
                    if os.stat(ServerFileList[0]).st_size == 0:
                        f.write(self.Host.text() + ";" + self.Port.text())
                    else:
                        f.write("\n" + self.Host.text() + ";" + self.Port.text())
            self.CSVupdate()

        elif self.file == "local":
            if self.Host.text() == "" or self.Port.text() == "" or self.Port.text().isdigit() == False:
                self.Response.append("Please enter a valid IP and a valid PORT")
            elif self.Port.text().isdigit() == False:
                self.Response.append("Port must be a number")
            elif int(self.Port.text()) > 65535:
                self.Response.append("Port must be between 0 and 65535")
            else :
                self.Response.append("Server added")
                with open("SAE 3.02/ServerList.csv", "a") as f:
                    # Write an new line in the CSV file
                        # if f is empty, write the first line
                        if os.stat("SAE 3.02/ServerList.csv").st_size == 0:
                            f.write(self.Host.text() + ";" + self.Port.text())
                        else:
                            f.write("\n" + self.Host.text() + ";" + self.Port.text())
            self.CSVupdate()

        else:
            if self.Host.text() == "" or self.Port.text() == "":
                self.Response.append("Please enter a valid IP and a valid PORT")
            elif self.Port.text().isdigit() == False:
                self.Response.append("Port must be a number")
            elif int(self.Port.text()) > 65535:
                self.Response.append("Port must be between 0 and 65535")
            else :
                self.Response.append("Server added")
                with open("SAE 3.02/ServerList.csv", "w") as f:
                    # Write an new line in the CSV file
                        # if f is empty, write the first line
                        if os.stat("SAE 3.02/ServerList.csv").st_size == 0:
                            f.write(self.Host.text() + ";" + self.Port.text())
                        else:
                            f.write("\n" + self.Host.text() + ";" + self.Port.text())
            self.file = "local"
            self.CSVupdate()

    def connect(self):
        global ip
        global port
        global client_socket
        ip = None
        port = None
        client_socket = None
        socket.setdefaulttimeout(0.25) # Set the socket timeout to 0.25 second
        selected = self.ServerList.currentItem()
        if selected != None:
            ip = selected.text().split(" ")[2]
            port = selected.text().split(" ")[5]
            try :
                client_socket = socket.socket() # Create a socket
                client_socket.connect((ip, int(port))) # Connect to the server
                self.ConnectionState.setText("Connected") # Set the connexion state label to "Connecté"
                self.ConnectionState.setStyleSheet("color: green") # Set the connexion state label color to green
                self.Response.append("Connected to " + ip + ":" + port) # Append "Connecté à " + self.Host.text() + ":" + self.Port.text() to the response text edit
            except:
                self.ConnectionState.setText("Not Connected !")
                self.ConnectionState.setStyleSheet("color: red")
                self.Response.append(ip + ":" + port + " is not responding")
                self.Response.append("Connection failed")
        else:
            self.Response.append("Please choose a server")
    
    def disconnect(self):   # Disconnect function
        try:    # Try
            client_socket.send("disconnect".encode())   # Send the disconnect string encoded to the client socket
            client_socket.close()   # Close the client socket
            self.ConnectionState.setText("Disconnected")  # Set the connexion state label to "Déconnecté"
            self.ConnectionState.setStyleSheet("color: red")    # Set the connexion state label color to red
            self.Response.append("Disconnected from " + ip + ":" + port)   # Append "Déconnecté de " + self.Host.text() + ":" + self.Port.text() to the response text edit
        except: # Except
            self.ConnectionState.setText("Not Connected !")  # Set the connexion state label to "Pas Connecté !"
            self.ConnectionState.setStyleSheet("color: orange") # Set the connexion state label color to orange

    def Send(self):
        try :
            if self.Command.text() == "":
                self.Response.append("Please enter a command")
            elif self.Command.text() != "":
                if self.Command.text() == "disconnect" or self.Command.text() == "DISCONNECT":
                    self.ConnectionState.setStyleSheet("color: red")
                    self.ConnectionState.setText("Disconnected")
                    self.Response.append("Disconnected from "+ ip+":"+port)
                    client_socket.close()
                    self.Command.clear()
                elif self.Command.text() == "clear":
                    self.Response.clear()
                    self.Command.clear()
                elif self.Command.text() == "help":
                    self.Response.append("disconnect : disconnect from the server")
                    self.Response.append("clear : clear the response")
                    self.Response.append("help : show the help")
                    self.Response.append("quit : quit the application")
                    self.Command.clear()
                elif self.Command.text() == "kill":
                    self.Response.append("You killed the server, you monster !")
                    client_socket.send(self.Command.text().upper().encode())
                    self.ConnectionState.setStyleSheet("color: red")
                    self.ConnectionState.setText("Disconnected")
                    client_socket.close()
                    self.Command.clear()
                elif self.Command.text() == "reset":
                    self.Response.append("You reset the server, didn't liked it like it was ?")
                    client_socket.send(self.Command.text().upper().encode())
                    self.Command.clear()
                else :
                    client_socket.send(self.Command.text().upper().encode())
                    self.Command.clear()
        except :
            self.Response.append("Not connected to a server")

    def Quit(self):
        try :
            socket.close()
            self.close()
            self.rec.stop()
        except :
            self.close()    # Close the window
        
        


if __name__ == "__main__":  # If the name is main
    app = QApplication(sys.argv)    # Create the app variable and set it to the application
    window = UI()   # Create the window variable and set it to the UI class
    sys.exit(app.exec())    # Exit the application