from tkinter import ttk
from tkinter import *

import sqlite3

class Productos:

    def _init_(self,root):
        
        self.wind=root
        self.wind.title("Productos")
        self.wind.geometry("850*600")
        

if __name__ == '__main__':
    root = Tk()
    product= Productos(root)
    root.mainloop()
    

     

