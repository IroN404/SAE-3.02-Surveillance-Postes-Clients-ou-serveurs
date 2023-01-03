# Importation des modules
import csv, sys, socket, os, threading, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Create the application
class UI(QWidget):
    def __init__(self):
        # Create the window
        super().__init__()  # Call the QWidget constructor
        self.setWindowTitle("Surveillance poste client")    # Set the title
          # Set the height of the window
        self.setStyleSheet("background-color: #2C313C;border: 0px;")    # Set the background color
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
        self.secondlabel = QLabel("Please choose a CSV file with the\nbutton above or start adding a server\nmanually to create a local CSV file")
        """
        self.<name> = <type>()
        """
        # Define Host attributes
        self.Host.setPlaceholderText("Host")
        self.Host.setStyleSheet("background-color: #000; color: #FFF;border-radius:5px;")
        self.Host.setFixedWidth(225)
        self.Host.setFixedHeight(30)
        # Define Port attributes
        self.Port.setPlaceholderText("Port")
        self.Port.setStyleSheet("background-color: #000; color: #FFF;border-radius:5px;")
        self.Port.setFixedWidth(225)
        self.Port.setFixedHeight(30)
        # Define Response attributes
        self.Response.setReadOnly(True)
        self.Response.setPlaceholderText("Server's reply will be displayed here")
        # Define AddButton attributes
        self.AddButton.setStyleSheet("background-color: #55AAFF; color: #FFF;padding: 0,0,0,20;border-radius: 10px 10px / 10px;")
        self.AddButton.setFixedHeight(30)
        # Define ConnectionState attributes
        self.ConnectionState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ConnectionState.setStyleSheet("color: #FFF;padding: 20,0,0,0;color: red;")
        self.ConnectionState.setFont(QFont("Arial", 10))
        self.ConnectionState.setFixedHeight(30)
        # Define ChooseFile attributes
        #self.ChooseFile.setStyleSheet("background-color: #000; color: #FFF;padding: 0,0,0,20;border-top : 1px solid #FFF;")
        self.ChooseFile.setStyleSheet("background-color: #55AAFF; color: #FFF;padding: 0,0,0,20;border-radius: 0px 0px 10px 10px;")
        self.ChooseFile.setFixedHeight(30)
        # Define ServerList attributes
        self.ServerList.setStyleSheet(" background-color: #1B1D23; color: #FFF;")
        self.ServerList.setLineWidth(0)
        # Define Respone attributes
        self.Response.setStyleSheet("background-color: #272C36; color: #FFF;")
        self.Response.setFixedWidth(500)
        # Define Command attributes
        self.Command.setStyleSheet("background-color: #272C36; color: #FFF;border-top : 1px solid #FFF;")
        self.Command.setPlaceholderText("Insert a command here : ")
        self.Command.setFixedHeight(30)
        self.Command.setFixedWidth(500)
        # Define EmptyTextBox attributes
        self.EmptyTextBox.setFixedHeight(50)
        self.EmptyTextBox.setStyleSheet("background-color: #1B1D23; color: #FFF;border-bottom : 1px solid #FFF;")
        self.EmptyTextBox.setFont(QFont("Arial", 20))
        self.EmptyTextBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Define secondlabel attributes
        self.secondlabel.setStyleSheet("background-color: #1B1D23; color: #FFF;padding: 20,20,0,0;")
        self.secondlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.secondlabel.setFont(QFont("Arial", 10))
        # Define Attributes of a new Widgets
        """
        self.<name>.set<Attribute>(<value>)
         """
        # Server list 
        self.LeftBar.addLayout(self.LeftBarTop) # Add the top part of the left bar to the left bar
        self.LeftBar.addLayout(self.LeftBarBottom)   # Add the bottom part of the left bar to the left bar
        self.LeftBarTop.addWidget(self.EmptyTextBox)
        self.LeftBarTop.addWidget(self.secondlabel)
        self.LeftBarTop.addWidget(self.ServerList)
        self.LeftBarTop.addWidget(self.ChooseFile)
        self.LeftBarTop.setContentsMargins(30, 25, 50, 25)
        self.LeftBarTop.setSpacing(0)
        # Server adding side
        self.LeftBarBottom.addWidget(self.Host)
        self.LeftBarBottom.addWidget(self.Port)
        self.LeftBarBottom.addWidget(self.AddButton)
        self.LeftBarBottom.addWidget(self.ConnectionState)
        self.LeftBarBottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LeftBarBottom.setContentsMargins(30, 0, 50, 0)
        self.LeftBarBottom.setSpacing(10)
        # Left Side
        self.LeftBar.setContentsMargins(0, 0, 0, 20)
        self.LeftBar.setSpacing(0)
        # Right Side
        self.RightBar.addWidget(self.Response)
        self.RightBar.addWidget(self.Command)
        self.RightBar.setContentsMargins(0, 0, 0, 0)
        self.RightBar.setSpacing(0)
        """
        self.<wanted layout>.add<Widget>(self.<name>)
        """
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
        self.file = "local"
        self.kill = False
        self.rec = threading.Thread(target=self.Receive)
        self.rec.start()
        """
        self.<name> = <value>
        self.<name>.<action>(lambda: <function>)
        """
        # Display the window
        self.show()

    def Reconnect(self):
        time.sleep(1)
        try :
            client_socket = socket.socket()
            client_socket.connect((ip, int(port)))
            self.Response.append("Reconnected to " + ip + " on port " + port)
        except:
            self.Response.append("Failed to reconnect")
        self.Scroll()

    def Scroll(self):
        self.Response.verticalScrollBar().setValue(self.Response.verticalScrollBar().maximum())

    def Receive(self):
        # wait for the server to send a message
        while self.kill != True:
            try:
                self.Response.append(client_socket.recv(1024).decode())
            except:
                pass
            self.Scroll()
            

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
        elif self.file == "local":
            self.ServerList.clear()
            with open("./ServerList.csv", "r") as f:
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
                    # Write a new line in the CSV file
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
                with open("./ServerList.csv", "a") as f:
                    # Write an new line in the CSV file
                        # if f is empty, write the first line
                    if os.stat("./ServerList.csv").st_size == 0:
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
                with open("./ServerList.csv", "w") as f:
                    # Write an new line in the CSV file
                        # if f is empty, write the first line
                        if os.stat("./ServerList.csv").st_size == 0:
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

    def Send(self):
        try :
            if self.Command.text() == "":
                self.Response.append("Please enter a command")
            elif self.Command.text() != "":
                if self.Command.text() == "disconnect" or self.Command.text() == "DISCONNECT":
                    self.ConnectionState.setStyleSheet("color: red")
                    client_socket.send(self.Command.text().encode())
                    self.ConnectionState.setText("Disconnected")
                    self.Response.append("Disconnected from "+ ip+":"+port)
                    client_socket.close()
                    self.Command.clear()
                elif self.Command.text() == "clear":
                    self.Response.clear()
                    self.Command.clear()
                elif self.Command.text() == "help":
                    self.Response.append("#################### Maintenance Commands ####################")
                    self.Response.append("kill : kill the server")
                    self.Response.append("disconnect : disconnect from the server")
                    self.Response.append("connection info : show the connection info")
                    self.Response.append("reset : reset the server")
                    self.Response.append("\n#################### Built-in Commands ####################")
                    self.Response.append("os : show the server os")
                    self.Response.append("ram : show the server ram")
                    self.Response.append("cpu : show the server cpu")
                    self.Response.append("ip : show the server ip")
                    self.Response.append("name : show the server name")
                    self.Response.append("clear : clear the response")
                    self.Response.append("\n#################### Specific OS Commands ####################")
                    self.Response.append("Windows command --> dos:<command> : execute a windows command")
                    self.Response.append("Linux command --> linux:<command> : execute a linux command")
                    self.Command.clear()
                elif self.Command.text() == "kill":
                    self.Response.append("The server has been killed")
                    client_socket.send(self.Command.text().encode())
                    self.ConnectionState.setStyleSheet("color: red")
                    self.ConnectionState.setText("Disconnected")
                    client_socket.close()
                    self.Command.clear()
                elif self.Command.text() == "reset":
                    client_socket.send(self.Command.text().encode())
                    self.Response.append("Server reset")
                    self.Command.clear()
                    client_socket.close()
                    i = 0
                    while i < 3:
                        try:
                            self.Response.append("Trying to reconnect ...")
                            time.sleep(2)
                            self.connect()
                            break
                        except:
                            pass
                        i += 1
                    if i == 3:
                        self.Response.append("Reconnection failed")
                        self.ConnectionState.setStyleSheet("color: red")
                        self.ConnectionState.setText("Disconnected")
                # Uncomment the following lines if you want to add a command
                    """
                elif self.Command.text() == "command":
                    client_socket.send(self.Command.text().encode())
                    """
                else :
                    client_socket.send(self.Command.text().encode())
                    self.Command.clear()
        except :
            self.Response.append("Not connected to a server")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Do you want to quit ?", 
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.kill = True
        else:
            event.ignore()
        


if __name__ == "__main__":  # If the name is main
    app = QApplication(sys.argv)    # Create the app variable and set it to the application
    window = UI()   # Create the window variable and set it to the UI class
    sys.exit(app.exec())    # Exit the application