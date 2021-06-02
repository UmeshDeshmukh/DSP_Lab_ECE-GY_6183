#Tkinter GUI demo in python

import tkinter as tk

def button1():
 print('Button pressed')
 
def button2():
 print('button2 pressed')

def quit():
 print('hasta la vista BABY')
 root.quit() 
 


root = tk.Tk()

L1 = tk.Label(root,text = 'Hello World from TKinter')


L2 = tk.Label(root,text = 'Are you afraid of the dark?')


str1 = tk.StringVar()
str1.set('PlayStation V')

L3 = tk.Label(root, textvariable = str1)
L3.pack()

B1 = tk.Button(root,text = 'press me',command = button1)
B1.pack()

B2 = tk.Button(root,text = 'button2',command = button2)
B2.pack()

B3 = tk.Button(root,text = 'Quit',command = quit)
B3.pack()

x1 = tk.DoubleVar()
x2 = tk.DoubleVar()

def updateVal():
 print(x1.get())
 print(x2.get()) 

s1 = tk.Scale(root,text = 'scale 1',variable = x1,command = updateVal)
s2 = tk.Scale(root,text = 'scale 2',variable = x2,command = updateVal)
L1 = tk.Label(root,text = 'Hello World from TKinter')

L1.pack()
L2.pack()
s1.pack()
s2.pack()
root.mainloop()



