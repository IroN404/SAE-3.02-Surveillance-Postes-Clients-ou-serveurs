import socket, platform, psutil, sys, subprocess, signal, time,os

def handler(signum, frame):
    res = input("Are you sure you want to exit ? (y/n) : ")
    if res == 'y':
        try :
            conn.close()
            serversocket.close()
            print("Server closed")
            sys.exit()
        except:
            exit(1)
    else :
        pass

def get_infos():
    # Create a TCP/IP socket in order to grab server's IP address
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    global IPadress
    IPadress = sock.getsockname()[0]
    sock.close()
    # Get the server's hostname
    global hostname
    hostname = socket.gethostname()
    # Get the server's OS
    global OperatingSystem
    OperatingSystem = platform.system()

def server():
    signal.signal(signal.SIGINT, handler)
    msg = ""
    global conn
    conn = None
    port  = None
    global serversocket
    serversocket = None
    while msg != 'kill':
        # Create the server's socket
        serversocket = socket.socket()
        host = "0.0.0.0"
        # add the port as a command line argument like this : python server.py -p 1234
        if len(sys.argv) == 3:
            if sys.argv[1] == '-p':
                try :
                    if len(sys.argv[2]) > 5 or int(sys.argv[2]) > 65535:
                        return print("Port number must be between 0 and 65535")
                    else :
                        try :
                            port = int(sys.argv[2])
                        except:
                            return print("Port number must be an integer")
                except:
                    return print("Port number must be an integer")
            elif sys.argv[1] != '-p':
                return print("Use -p to specify the port number")
        if len(sys.argv) < 3:
            if len(sys.argv) == 2:
                if sys.argv[1] != '-p':
                    return print("Use -p to specify the port number")
                else :
                    return print("not enough arguments, add the port number after -p")
            else :
                return print("not enough arguments, use -p followed by the port number")
        if len(sys.argv) > 3:
            return print("Too many arguments")
        # connection error handling
        try :
            serversocket.bind((host, port))
        except socket.error as e:
            print(str(e))

        # Listen for connections
        while True:
            msg = ""
            serversocket.listen(1)
            print(f"Server is listening on address : {IPadress}, Port : {port} \nWaiting for connection...")
            try :
                conn, addr = serversocket.accept()
                print ("Connection from: " + str(addr))
            except ConnectionError:
                print("Connection error")
                break
            while True :
                try :
                    msg = conn.recv(1024).decode()
                    if msg.startswith('dos'):
                        if OperatingSystem == 'Windows':
                            cmd = msg.split(":")[1]
                            reply = subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='cp850',shell=True)
                            out, err = reply.communicate()
                            if reply.returncode == 0:
                                conn.send(f"[{hostname}] {cmd} {time.strftime('%H:%M:%S')} \n{out} \n".encode())
                            else :
                                conn.send(f"[{hostname}] {cmd} {time.strftime('%H:%M:%S')} \n{err} \n".encode())
                        else :
                            conn.send(f"[{hostname}] {cmd} {time.strftime('%H:%M:%S')} \n This command is only available for Windows".encode())
                    elif msg.startswith('linux'):
                        if OperatingSystem != 'Windows':
                            cmd = msg.split(":",1)[1]
                            reply = subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='cp850',shell=True)
                            out, err = reply.communicate()
                            if reply.returncode == 0:
                                conn.send(f"[{hostname}] {cmd} {time.strftime('%H:%M:%S')} \n{out} \n".encode())
                            else :
                                conn.send(f"[{hostname}] {cmd} {time.strftime('%H:%M:%S')} \n{err} \n".encode())
                        else :
                            conn.send(f"[{hostname}] {cmd} {time.strftime('%H:%M:%S')} \n This command is only available for Linux type system".encode())
                    elif msg == 'cpu':
                        conn.send(f"[{hostname}] {msg} {time.strftime('%H:%M:%S')} \nThe CPU usage is {psutil.cpu_percent()} % \n".encode())
                    elif msg == 'ram':
                        conn.send(f"[{hostname}] {msg} {time.strftime('%H:%M:%S')} \nThe memory usage is {psutil.virtual_memory()[2]} % \n".encode())
                    elif msg == 'ip':
                        conn.send(f"[{hostname}] {msg} {time.strftime('%H:%M:%S')} \nThe server's IP address is : {IPadress} \n".encode())
                    elif msg == 'hostname':
                        conn.send(f"[{hostname}] {msg} {time.strftime('%H:%M:%S')} \nThe server's hostname is {hostname} \n".encode())
                    elif msg == 'os':
                        conn.send(f"[{hostname}] {msg} {time.strftime('%H:%M:%S')} \nThe server's Operating System is {OperatingSystem} \n".encode())
                    elif msg.startswith('ping'):
                        cmd = msg
                        if OperatingSystem == 'Windows':
                            reply = subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='cp850',shell=True)
                            out, err = reply.communicate()
                            if reply.returncode == 0:
                                conn.send(f"[{hostname}] {cmd} {time.strftime('%H:%M:%S')} \n{out} \n".encode())
                            else :
                                conn.send(f"[{hostname}] {cmd} {time.strftime('%H:%M:%S')} \n{err} \n".encode())
                        else :
                            cmd = cmd + " -c 4"
                            reply = subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='cp850',shell=True)
                            out, err = reply.communicate()
                            if reply.returncode == 0:
                                conn.send(f"[{hostname}] {cmd} {time.strftime('%H:%M:%S')} \n{out} \n".encode())
                            else :
                                conn.send(f"[{hostname}] {cmd} {time.strftime('%H:%M:%S')} \n{err} \n".encode())
                            
                    elif msg == 'disconnect':
                        conn.close()
                        print("Connection closed")
                        break
                    elif msg == 'reset':
                        # disconnect and reconnect to the client
                        conn.close()
                        print("Connection closed")
                        print("Server restarted")
                        break
                    elif msg == 'kill':
                        conn.close()
                        print("Connection closed")
                        serversocket.close()
                        print("Server closed")
                        sys.exit()
                    # Uncomment the code below if you want to add more commands, you can also add more command by copying the elif line and pasting it below the last elif line and changing the command and the message.
                        """
                    elif msg == '<enter the command>':
                        conn.send(f"[{hostname}] {msg} {time.strftime('%H:%M:%S')} \n""message""\n".encode())
                        """
                    else :
                        try:
                            reply = subprocess.Popen(msg,stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='cp850',shell=True)
                            out, err = reply.communicate()
                            if reply.returncode == 0:
                                conn.send(f"[{hostname}] {msg} {time.strftime('%H:%M:%S')} \n{out} \n".encode())
                            else :
                                conn.send(f"[{hostname}] {msg} {time.strftime('%H:%M:%S')} \n{err} \n".encode())
                        except:
                            conn.send("Command not found".encode())
                    print (msg)
                except ConnectionResetError:
                    print("Connection closed")
                    break

if __name__ == "__main__":
    get_infos()
    server()