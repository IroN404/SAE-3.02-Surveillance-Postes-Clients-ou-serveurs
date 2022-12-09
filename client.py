# Importation des modules
from PyQt6 import *
import csv, sys, socket
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import os

# Create the application
class UI(QWidget):
    def __init__(self):
        # Create the window
        super().__init__()  # Call the QWidget constructor
        self.setWindowTitle("Surveillance poste client")    # Set the title
        self.setFixedWidth(750) # Set the width of the window
        self.setFixedHeight(500)    # Set the height of the window
        self.layout = QGridLayout() # Create the layout
        self.setLayout(self.layout) # Set the layout

        # Create the widgets
        self.LabelHost = QLabel("Server's IP")   # Create the IP label
        self.LabelPort = QLabel("Server's Port") # Create the PORT label
        self.LabelConnexion = QLabel("Connection State : ")   # Create the connexion label
        self.LabelConnexionState = QLabel("Not Connected")   # Create the connexion state label
        self.ButtonConnect = QPushButton("Connect") # Create the connect button
        self.ButtonDisconnect = QPushButton("Disconnect")   # Create the disconnect button
        self.ButtonClear = QPushButton("Clear")  # Create the clear button
        self.ButtonKill = QPushButton("Kill")   # Create the kill button
        self.ButtonQuit = QPushButton("Quit")   # Create the quit button
        self.ButtonSend = QPushButton("Send")   # Create the send button
        self.ButtonReset = QPushButton("Reset")   # Create the reset button
        self.ButtonAdd = QPushButton("Add")   # Create the add button
        self.ButtonRemove = QPushButton("Remove")   # Create the remove button
        self.ServerList = QListWidget() # Create the server table
        self.Host = QLineEdit() # Create the host line edit
        self.Port = QLineEdit() # Create the port line edit
        self.Message = QLineEdit()  # Create the message line edit
        self.Response = QTextEdit() # Create the response text edit

        # Tableau des serveurs
        self.layout.addWidget(self.ServerList, 0, 0,2,2) # Add the server table to the layout

        # Manually Enter Host
        self.layout.addWidget(self.Port, 4, 0, 1, 1)   # Add the IP label to the layout
        self.layout.addWidget(self.Host, 3,0,1,1)   # Add the host line edit to the layout
        self.layout.addWidget(self.ButtonAdd, 3,1,2,1)   # Add the add button to the layout

        # Etat de la connexion
        self.layout.addWidget(self.LabelConnexion, 2,0,1,1)  # Add the connexion label to the layout
        self.layout.addWidget(self.LabelConnexionState, 2, 1, 1, 1) # Add the connexion state label to the layout

        # Boutons de connexion
        self.layout.addWidget(self.ButtonConnect, 5, 0, 1, 1)   # Add the connect button to the layout
        self.layout.addWidget(self.ButtonDisconnect, 6, 0, 1, 1)    # Add the disconnect button to the layout
        self.layout.addWidget(self.ButtonKill, 5, 1, 1, 1)  # Add the kill button to the layout
        self.layout.addWidget(self.ButtonReset, 6, 1, 1, 1) # Add the reset button to the layout
        self.layout.addWidget(self.ButtonQuit, 7, 0, 1, 2)  # Add the quit button to the layout
        
        # Fenetres de message
        self.layout.addWidget(self.Response, 0, 3, 1, 2)    # Add the response text edit to the layout

        # Envoi message manuel
        self.layout.addWidget(self.Message, 7, 3, 1, 2) # Add the message line edit to the layout
        # Connexion des boutons
        self.ButtonAdd.clicked.connect(self.AddServer)    # Connect the add button to the AddServer function
        self.ButtonConnect.clicked.connect(self.Connect)  # Connect the connect button to the Connect function
        self.ButtonQuit.clicked.connect(self.Quit)    # Connect the quit button to the Quit function

        # Definition des attributs
        self.Response.setReadOnly(True) # Set the response text edit to read only
        self.ServerList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)    # Set the server table edit triggers to no edit triggers
        self.LabelConnexionState.setStyleSheet("color: red")    # Set the connexion state label color to red
        self.ServerList.setFixedWidth(300)   # Set the server table fixed width to 300
        self.Response.setFixedWidth(400)    # Set the response text edit fixed width to 400
        self.Response.setFixedHeight(440)   # Set the response text edit fixed height to 400
        self.Message.setFixedWidth(400) # Set the message line edit fixed width to 400
        self.Message.setPlaceholderText("Enter your command here >")    # Set the message line edit placeholder text
        self.Message.setFixedHeight(30) # Set the message line edit fixed height to 30
        self.Message.setStyleSheet("border: 1px solid black")   # Set the message line edit border to 1px solid black
        self.Response.setStyleSheet("border: 1px solid black")  # Set the response text edit border to 1px solid black  
        self.Response.setPlaceholderText("Server's reply will be displayed here")    # Set the response text edit placeholder text
        self.Response.setStyleSheet("background-color: black; color: white")  # Set the response text edit background color to black and the text color to white
        self.Host.setPlaceholderText("Enter the server's IP here")   # Set the host line edit placeholder text
        self.Port.setPlaceholderText("Enter the server's PORT here")    # Set the port line edit placeholder text
        self.Host.setStyleSheet("border: 1px solid black")    # Set the host line edit border to 1px solid black
        self.Port.setStyleSheet("border: 1px solid black")    # Set the port line edit border to 1px solid black
        self.Host.setFixedHeight(30)    # Set the host line edit fixed height to 30
        self.Port.setFixedHeight(30)    # Set the port line edit fixed height to 30
        self.LabelConnexion.setStyleSheet("margin-left: 60px")  # Set the connexion label margin left to 70px
        self.Host.setFixedWidth(180)    # Set the host line edit fixed width to 150
        self.Port.setFixedWidth(180)    # Set the port line edit fixed width to 150
        self.CSVToList()    # Call the CSVToList function
        
        # Affichage de la fenetre
        self.show() # Show the window
        
    def CSVToList(self):
        global file
        self.ServerList.clear()
        file = True
        try:
            with open("./server.csv", "r") as f:
                reader = csv.reader(f)
                for column in reader:
                    ip = column[0].split(";")
                    port = column[0].split(";")
                    self.ServerList.addItem("Adresse : " + ip[0] + " Port : " + port[1])
        except:
            file=False
            self.ServerList.addItem("No CSV file found, add a server to create one")

    def AddServer(self):
        self.CSVToList()
        if file != False:
            if self.Host.text() == "" or self.Port.text() == "":
                self.Response.append("Please enter a valid IP and a valid PORT")
            else :
                global flag
                flag = False
                if ("." in self.Host.text()):
                    elements_array = self.Host.text().strip().split(".")
                    if(len(elements_array) == 4):
                        for i in elements_array:
                            if (i.isnumeric() and int(i)>=0 and int(i)<=255):
                                flag=True
                            else:
                                flag=False
                                break
                if flag or self.Host.text() == "localhost":
                    self.Response.append("Server added")
                    with open("./server.csv", "a") as f:
                    # Write an new line in the CSV file
                        # if f is empty, write the first line
                        if os.stat("./server.csv").st_size == 0:
                            f.write(self.Host.text() + ";" + self.Port.text())
                        else:
                            f.write("\n" + self.Host.text() + ";" + self.Port.text())
                    self.CSVToList()
                else:
                    self.Response.append("Please enter a valid IP and a valid PORT")
        else:
            if self.Host.text() == "" or self.Port.text() == "":
                self.Response.append("Please enter a valid IP and a valid PORT")
            else :
                flag = False
                if ("." in self.Host.text()):
                    elements_array = self.Host.text().strip().split(".")
                    if(len(elements_array) == 4) :
                        for i in elements_array :
                            if (i.isnumeric() and int(i)>=0 and int(i)<=255):
                                flag=True
                            else:
                                flag=False
                                break
                if flag or self.Host.text() == "localhost":
                    self.Response.append("Server added")
                    with open("./server.csv", "w") as f:
                    # Write an new line in the CSV file
                        # if f is empty, write the first line
                        if os.stat("./server.csv").st_size == 0:
                            f.write(self.Host.text() + ";" + self.Port.text())
                        else:
                            f.write("\n" + self.Host.text() + ";" + self.Port.text())
                    self.CSVToList()
                else:
                    self.Response.append("Please enter a valid IP and a valid PORT")

    def Connect(self):
        global socket
        global host
        global port
        host = self.Host.text()
        port = self.Port.text()
        if self.Host.text() == "" or self.Port.text() == "":
            self.Response.append("Please enter a valid IP and a valid PORT")
            self.LabelConnexionState.setStyleSheet("color: orange")
            self.LabelConnexionState.setText("Connection Error")
        else :
            try :
                socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.connect((self.Host.text(), int(self.Port.text())))
                self.LabelConnexionState.setStyleSheet("color: green")
                self.LabelConnexionState.setText("Connected")
                self.Response.append("Connected to " + self.Host.text() + ":" + self.Port.text())
            except :
                self.Response.append("Connection failed")
                self.LabelConnexionState.setStyleSheet("color: orange")
                self.LabelConnexionState.setText("Connection Error")


    def Quit(self):
        self.close()    # Close the window
        
        


if __name__ == "__main__":  # If the name is main
    app = QApplication(sys.argv)    # Create the app variable and set it to the application
    window = UI()   # Create the window variable and set it to the UI class
    sys.exit(app.exec())    # Exit the application