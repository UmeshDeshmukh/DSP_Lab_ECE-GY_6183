# demo16ex1
import math
import matplotlib.pyplot as plt 
import tkinter as Tk

root = Tk.Tk()

x  = Tk.DoubleVar()
x.set(0.0)
y  = Tk.DoubleVar()
y.set(0.0)
z  = Tk.DoubleVar()
z.set(0.0)
s1 = Tk.StringVar()
s2 = Tk.StringVar()
s3 = Tk.StringVar()
s4 = Tk.StringVar()

def quitButton():
 root.quit() 

def update():
 s2.set(str(x.get()))

def calculate():
 # if var.get() == 1.0:   
  z.set(math.sqrt(float(s1.get())**2 + float(s2.get())**2))
  s3.set(str(z.get()))
  print('value of a is-' + str(z.get()))
 # if var.get() == 2.0:
  # s3.set(str(float(s1.get())* float(s2.get())*0.5) 
 # elif (var.get() == 2) :
  # s3.set(str(float(s1.get())* float(s2.get())*0.5)
 # else :
  # print('Select correct option.') 

L1 = Tk.Label(root, text = 'Quadratic Formula')
L2 = Tk.Label(root, text = 'First side of a triangle.')
E1  = Tk.Entry(root,textvariable = s1)
L3 = Tk.Label(root, text = 'Second side of a triangle.')
# E2  = Tk.Entry(root,textvariable = s2)

# E3  = Tk.Entry(root)

B1 = Tk.Button(root,text = 'Calculate output')#,command = calculate)
L4 = Tk.Label(root, text = 'Diagonal is')
B2 = Tk.Button(root,text = 'Quit',command = quitButton)
S  = Tk.Scale(root,variable = x, command = update)
L5 = Tk.Label(root, text = 'Length of Diagonal = ',textvariable = s3) 
L6 = Tk.Label(root, text = 'slider value = ',textvariable = s4) 

var = Tk.IntVar()
R1 = Tk.Radiobutton(root, text="Diagonal", variable=var, value=1)

R2 = Tk.Radiobutton(root, text="Area", variable=var, value=2)



L1.pack()
L2.pack()
E1.pack()
L3.pack()
S.pack()
# E2.pack()

R1.pack()
R2.pack()
# E3.pack()
B1.pack()
L4.pack()
L5.pack()
L6.pack()
B2.pack(side = 'bottom')



root.mainloop()