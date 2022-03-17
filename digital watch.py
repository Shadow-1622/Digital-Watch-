# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:39:27 2020

@author: Aditya
"""


import tkinter as tk
root=tk.Tk()
from time import strftime
root.title('clock')

def time():
    string=strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000,time)
    
lbl=tk.Label(root,font=('calibri',50,'bold'),background='sky blue',foreground='black')
lbl.pack(anchor='center')
time()

root.mainloop()