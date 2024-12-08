from tkinter import *
import win32api
import time
import threading
import tkinter as tk
import os
import pathlib

def test(cat):
    cats = str(cat).split("C:\\Users\\h0hr\\Scripts\\misc\\advertisement\\kdo\\")
    root = Tk()
    cat_picture = PhotoImage(file="{}".format(cats[1]))
    cat = Label(root, image=cat_picture)
    cat.pack()
    root.mainloop()



def open_window(): 
    cat_path = pathlib.Path(r"C:\Users\h0hr\Scripts\misc\advertisement\kdo")
    os.chdir(cat_path)
    for cat in cat_path.iterdir():
        cats = str(cat).split("C:\\Users\\h0hr\\Scripts\\misc\\advertisement\\kdo\\")
        cat_thread = threading.Thread(target=test, kwargs={"cat":"catd"})
        cat_thread.start()


def main():
    try:
        while True:
            option = input("TEST: ")
            if option == "test":
                cat_window = threading.Thread(target=open_window)
                cat_window.start()
    except KeyboardInterrupt:
        exit()
    

if __name__ == "__main__":
    main()
