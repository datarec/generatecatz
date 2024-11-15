from tkinter import *
import win32api
import time
import threading
import tkinter as tk

def open_window():
    root = Tk()
    cat_picture = PhotoImage(file="cat.gif")
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


if __name__ == "__main__":
    main()
