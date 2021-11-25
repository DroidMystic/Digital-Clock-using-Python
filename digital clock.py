#IMPORTING MODULES
from time import strftime
import time
from tkinter import *


#INITIALISING ROOT WINDOW
root=Tk()
root.title("DIGITAL CLOCK")
root.geometry("650x300")

#DEFINING TIME
def time():
    String=strftime('%H:%M:%S %p')
    label.config(text=String)
    label.after(1000,time)
#STYLING THE CLOCK  
label=Label(root,bg="black", fg="#4EEE94",font=("ds-digital",80))
label.pack(anchor="center",expand=True,fill=BOTH)

#CALLING TIME FUNCTION
time()
root.mainloop()













