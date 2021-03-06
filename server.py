import os
import socket
import sys
from os import path

TCP_IP = '0.0.0.0'
TCP_PORT = int(sys.argv[1])
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)


def Connection(lines):
    for line in lines:
        if "Connection: " in line:
            return line + "\n"


while True:
    conn, addr = s.accept()
    flag = False
    while not flag:
        try:
            conn.settimeout(1)
            data = conn.recv(BUFFER_SIZE)
            print(data.decode("utf-8"), end="")
            if not data:
                conn.close()
                break
            requests = data.decode().split("\r\n\r\n")
            flag = False
            for request in requests:
                if request == '':
                    break
                lines = request.split("\n")
                length = lines[0].find("HTTP/1.1")
                fileName = lines[0][5: length - 1]
                connection = ""
                if fileName == "redirect":
                    headerString = "HTTP/1.1 301 Moved Permanently\r\nConnection: close\r\nLocation:/result.html\r\n\r\n"
                    conn.send(bytes(headerString, "utf-8"))
                    flag = True
                    break
                if fileName == "":
                    fileName = "index.html"
                pathFile = sys.path[0] + "\\files\\" + fileName
                if not path.exists(pathFile):
                    headerString = "HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n"
                    conn.send(bytes(headerString, "utf-8"))
                    flag = True
                    break
                try:
                    file = open(pathFile, "rb")
                    sizeFile = os.path.getsize(pathFile)
                    length = "Content-Length: " + str(sizeFile) + "\r\n\r\n"
                    fileContent = file.read(sizeFile)
                    file.close()
                    headerString = "HTTP/1.1 200 OK\r\n"
                    connection = Connection(lines)
                    headerString += connection
                    headerString += length
                    toSend = bytes(headerString, "utf-8") + fileContent
                    conn.send(toSend)
                    if connection.split(" ")[1] == "close\r\n":
                        flag = True
                        break
                    else:
                        flag = False
                except PermissionError:
                    headerString = "HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n"
                    conn.send(bytes(headerString, "utf-8"))
                    flag = True
                    break
            if flag:
                conn.close()
                break
        except socket.timeout:  # timeout exception
            flag = True
            conn.close()
            break
        except ConnectionResetError:  # client close the socket after "keep-alive"
            flag = True
            conn.close()
            break
        except ConnectionAbortedError:
            flag = True
            conn.close()
            break
