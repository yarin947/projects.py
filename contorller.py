from vidstream import StreamingServer
import socket
import io
from pynput import keyboard #type: ignore 
from PIL import Image #type: ignore  
from threading import Thread, Lock
from pynput.mouse import Listener,Button
from threading import Thread, Lock
from io import BytesIO
import os


ip = "192.168.1.152"
port_keyboard = 50000
server_socket_keyboard = socket.socket()
server_socket_keyboard.bind((ip, port_keyboard))
server_socket_keyboard.listen(1)
print("listening to keyboard...")
connection_keyboard, client_address = server_socket_keyboard.accept()
print("keyboard connection made!")

def on_press(key):
        cond = key
        try:
            key = str(key.char)
            print("pressed key --> {}".format(key))
            key = key.encode()
            connection_keyboard.send(key)
        except AttributeError:
            key = str(key)
            print("pressed key --> {}".format(key))
            key = key.encode()
            connection_keyboard.send(key)
        if cond == keyboard.Key.esc:
            return False

listener_keyboard = keyboard.Listener(on_press=on_press)
listener_keyboard.start()
listener_keyboard.join()


port_mouse = 23456
server_socket_mouse = socket.socket()
server_socket_mouse.bind((ip, port_mouse))
server_socket_mouse.listen(1)
print("listening to mouse...")
connection_mouse, client_address = server_socket_mouse.accept()
print("mouse connection made!")

def on_move(x,y):
        print("in the func")
        print("pointer moved to {}".format((x,y)))
        x,y = str(x), str(y)
        x,y = x.encode(), y.encode()   
        connection_mouse.send(x)
        connection_mouse.send(y)


def on_click(x,y,button,pressed):
            print('pressed: {0} at {1}'.format(button, (x, y)))
            if button == Button.left:
                connection_mouse.send(str(button).encode())
            elif button == Button.right:
                connection_mouse.send(str(button).encode())


def on_scroll(x, y, dx, dy):
        if dy < 0:
            scrolled = "down"
        else:
            scrolled = "up"
        print((dx, dy))
        print('scrolled {} to {}'.format(scrolled, (x, y)))
        dy = str(dy)
        print(dy+scrolled)
        connection_mouse.send((dy + " " + scrolled).encode())

listener_mouse = Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
try:
    listener_mouse.start()
    listener_mouse.join()
except KeyboardInterrupt:
      pass

ip = "192.168.1.152"
port_screen = 34567

host = StreamingServer(ip,port_screen)
first = Thread(target=host.start_server)

first.start()

while input("") != 'stop':
    continue
host.stop_server()
