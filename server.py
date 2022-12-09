import socket
import platform
import psutil
import sys
import subprocess
import signal

def handler(signum, frame):
    res = input("Do you really want to exit? (y/n) : ")
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
            
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        # connection error handling
        try :
            serversocket.bind((host, port))
        except socket.error as e:
            print(str(e))

        # Listen for connections
        serversocket.listen(1)
        print(f"Server is listening on address : {IPadress}, Port : {port} \nWaiting for connection...")
        while msg != 'kill' and msg != 'reset':
            msg = ""
            try :
                conn, addr = serversocket.accept()
                print ("Connection from: " + str(addr))
            except ConnectionError:
                print("Connection error")
                break
            else :
                while msg != 'kill' and msg != 'reset' and msg != 'disconnect':
                    msg = conn.recv(1024).decode()
                    if msg == 'CPU':
                        conn.send(str(psutil.cpu_percent()).encode())
                    elif msg == 'RAM':
                        conn.send(str(psutil.virtual_memory().percent).encode())
                    elif msg == 'IP':
                        conn.send(IPadress.encode())
                    elif msg == 'hostname':
                        conn.send(hostname.encode())
                    elif msg == 'OS':
                        conn.send(OperatingSystem.encode())
                    else :
                        reply = subprocess.Popen(msg,stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='cp850',shell=True)
                        try :
                            conn.sendf(reply.stdout.read().encode())
                        except:
                            conn.send(reply.stderr.read().encode())
                            
                if msg == 'disconnect':
                    conn.close()
                    print("Connection closed")
                    break
                elif msg == 'reset':
                    conn.close()
                    print("Connection closed")
                    break
                elif msg == 'kill':
                    conn.close()
                    print("Connection closed")
                    serversocket.close()
                    print("Server closed")
                    sys.exit()

if __name__ == "__main__":
    get_infos()
    server()

