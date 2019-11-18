#!/usr/bin/env python3
from tkinter import *
from tkinter.colorchooser import askcolor
import socket 
import select 
import sys
import re 
from threading import Thread
from time import sleep



class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=10)
        self.choose_size_button.grid(row=1, column=0)

        self.c = Canvas(self.root, bg='white', width=240, height=320)
        self.c.grid(row=1, columnspan=4)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        if len(sys.argv) != 3: 
            print("Correct usage: script, IP address, port number")
            exit() 
        IP_address = str(sys.argv[1]) 
        Port = int(sys.argv[2]) 
        self.server.connect((IP_address, Port)) 

        self.setup()
        receive_thread = Thread(target=self.checkSocket)
        receive_thread.start()
        self.root.mainloop()
        
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def checkSocket(self):

        while True:
            sockets_list = [sys.stdin, self.server] 

            """ There are two possible input situations. Either the 
            user wants to give manual input to send to other people, 
            or the server is sending a message to be printed on the 
            screen. Select returns from sockets_list, the stream that 
            is reader for input. So for example, if the server wants 
            to send a message, then the if condition will hold true 
            below.If the user wants to send a message, the else 
            condition will evaluate as true"""
            read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
            for socks in read_sockets: 
                if socks == self.server: 
                    message = socks.recv(2048)
                    data = message.decode()
                    print(data)
                    match = re.search('%(.+?)%(.+?)%',data)
                    color = re.search('[A-z 0-9 #]*$',data)
                    print(color.group(0))
                    if match:
                        x = match.group(1)
                        print(x)
                        y = match.group(2)
                        print(y)
                    # current_x = data[1:2]
                    # current_y = data[4:6]
                    # color     = data[8:14]
                    # print(current_x, current_y, color)
                    self.c.create_rectangle((x,y)*2, outline = color.group(0))
        
		




   

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button,brush_mode = True)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False,brush_mode = False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode
        self.brush_on = brush_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.server.send(('%'+str(event.x)+'%'+str(event.y)+'%'+str(self.color)).encode()) 
            

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()