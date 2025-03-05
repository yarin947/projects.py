import socket
from pynput.keyboard import Controller,Key  # type: ignor
from threading import Thread, Lock
from pynput.mouse import Button, Controller   # type: ignore
from vidstream import ScreenShareClient


ip = "192.168.1.152"
port_keyboard = 50000
client_socket = socket.socket()
client_socket.connect((ip,port_keyboard))

special_dict = {
    "Key.space":Key.space,
    "Key.alt":Key.alt,
    "Key.backspace":Key.backspace,
    "Key.caps_lock":Key.caps_lock,
    "Key.cmd":Key.cmd,
    "Key.ctrl":Key.ctrl,
    "Key.shift":Key.shift,
    "Key.tab":Key.tab,
    "Key.enter":Key.enter,
    "Key.esc":Key.esc,
    "Key.down":Key.down,
    "Key.up":Key.up,
    "Key.left":Key.left,
    "Key.right":Key.right
}

def keyboard_action():
        keyboard = Controller()
        print("waiting for key... ")
        key = client_socket.recv(1024).decode()
        keyboard.press(key)
        keyboard.release(key)     
        while key != "Key.esc":
                try:
                    key = client_socket.recv(1024).decode()
                    keyboard.press(key)
                    keyboard.release(key)
                except ValueError:
                    if key in special_dict:
                        pressing = special_dict[key]
                        keyboard.press(pressing)
                        keyboard.release(pressing)
                    

first = Thread(target=keyboard_action)
first.start()
first.join()

ip = "192.168.1.152"
port_key = 50000
button_dict = {
    "Button.left" : Button.left,
    "Button.right": Button.right
}
port_mouse = 23456
client_socket_mouse = socket.socket()
client_socket_mouse.connect((ip, port_mouse))
print("waiting for the mouse to move")

def mouse_move():
    mouse = Controller()
    coordinate_x = client_socket_mouse.recv(1024).decode()
    coordinate_y = client_socket_mouse.recv(1024).decode()
    mouse.position= (int(coordinate_x),int(coordinate_y))
    while coordinate_x and coordinate_y:
        coordinate_x = client_socket_mouse.recv(1024).decode()
        coordinate_y = client_socket_mouse.recv(1024).decode()
        if coordinate_x.isnumeric() == True and coordinate_y.isnumeric() == True:
                    coordinate_x = coordinate_x[:4]
                    coordinate_y = coordinate_y[:4]
                    x = int(coordinate_x)
                    y = int(coordinate_y)
                    if x<1921 and y<1081:
                        if x < 0:
                            x = int(coordinate_x[:2])
                        elif x >= 0 and x <= 9:
                            x = int(coordinate_x[:1])
                           
                        elif x >= 10 and x <= 99:
                            x = int(coordinate_x[:2])

                        elif x >= 100 and x <= 999:
                            x = int(coordinate_x[:3])
                            
                        elif x >= 1000 and x <= 1920:
                            x = int(coordinate_x[:4])
                        
                        if y < 0:
                            y = int(coordinate_y[:2])
                        
                        elif y<= 0 and y <= 9:
                            y = int(coordinate_y[:1])
                    
                        elif y<= 10 and y <= 99:
                            y = int(coordinate_y[:2])
                            
                        elif y<= 100 and y <= 999:
                            y = int(coordinate_y[:3])
                                    
                        elif y<= 1000 and y <=1080:
                            y = int(coordinate_y[:4])
                        
                        print("x coordinate --> {}".format(x))
                        print("y coordinate --> {}".format(y)) 
                        mouse.position= (x,y)
        else:
            button = client_socket_mouse.recv(1024).decode()
            if button == "Button.left" or button == "Button.right":
                pressing_button = button_dict[button]
                print("{} need to be pressed".format(pressing_button))
                mouse.press(pressing_button)
                mouse.release(pressing_button)
                dy = client_socket_mouse.recv(1024).decode()
                if dy == "1 up" or dy == "-1 down":
                    if "down" in dy:
                        whereTo = "down"
                        scrolling = -1
                    elif "up" in dy:
                        whereTo = "up"
                        scrolling = 1
                    print("need to scroll by {} {}".format(scrolling, whereTo))
                    mouse.scroll(0,scrolling)
                else:
                    continue
second = Thread(target=mouse_move)
second.start()
second.join()

ip = "192.168.1.152"  
port_screen = 34567  

sender = ScreenShareClient(ip,port_screen)
sender.start_stream()