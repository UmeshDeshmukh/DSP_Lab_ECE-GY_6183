import tkinter as Tk
import math

def fun1():
    # c = float(s1.get()) + float(x.get())
    # s3.set(str(c))
    # s4.set('Diagonal of triangle is:')
    # c = math.sqrt(float(s1.get())**2 + float(x.get())**2)
    # s3.set(str(c))
    if var.get() == 1:
        s4.set('Diagonal of triangle is:')
        c = math.sqrt(float(s1.get())**2 + float(x.get())**2)
        s3.set(str(c))
    elif var.get() == 2:
        s4.set('Area of triangle is:')
        c = (float(s1.get())* float(x.get())*0.5)
        s3.set(str(c))
    else:   
        s4.set('ERROR: Select operation')
    
root = Tk.Tk()

# Define Tk variables
s1 = Tk.StringVar()
s2 = Tk.StringVar()
s3 = Tk.StringVar()
s4 = Tk.StringVar()
var = Tk.IntVar()
x = Tk.DoubleVar()

# Define widgets
L1 = Tk.Label(root, text = 'Height of triangle')
E1 = Tk.Entry(root, textvariable = s1)
# E2 = Tk.Entry(root, textvariable = s2)
L2 = Tk.Label(root, text = 'Base of triangle') 
S1 = Tk.Scale(root, variable = x)
B1 = Tk.Button(root, text = 'Calculate Output', command = fun1)
L4 = Tk.Label(root, textvariable = s4)
L3 = Tk.Label(root, textvariable = s3)
B2 = Tk.Button(root, text = 'Quit', command = root.quit)
L5 = Tk.Label(root, text = 'Select operation')

R1 = Tk.Radiobutton(root, text="Length of Diagonal", variable=var, value=1)
R2 = Tk.Radiobutton(root, text="Area", variable=var, value=2)

# Place widgets
L1.pack()
E1.pack()
# E2.pack()
L2.pack()
S1.pack()
L5.pack()
R1.pack()
R2.pack()
B1.pack()
L4.pack()
L3.pack()



B2.pack()

root.mainloop()
