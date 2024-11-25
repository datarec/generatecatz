from tkinter import *
import win32api
import time
import threading
import tkinter as tk
import os
import pathlib


def open_window():
    root = Tk()
    cat_path = pathlib.Path("C:\\Users\\h0hr\\Scripts\\misc\\advertisement\\cats")
    for cats in cat_path.iterdir():
        root = Tk()
        str_cat = str(cats)
        str_cat_filename = str_cat.strip("C:\\Users\\h0hr\\Scripts\\misc\\advertisement\\cats\\")
        print(str_cat_filename)
    cat_picture = PhotoImage(file="{}".format(str_cat_filename))
    cat = Label(root, image=cat_picture)
    cat.pack()
    root.mainloop()


def main():
    try:
        while True:
            option = input("TEST: ")
            if option == "test":
                cat_window = threading.Thread(target=open_window)
                cat_window.start()
    except KeyboardInterrupt:
        exit()

 

def copy_operation():
    pass
    


if __name__ == "__main__":
    main()
