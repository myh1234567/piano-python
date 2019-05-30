import time
import tkinter as tk
from time import sleep

root = tk.Tk()


def detectInput():
    print("SPACE\n")

def release():
    print("release\n")

root.bind("<KeyPress-a>", lambda event:detectInput())
root.bind("<KeyRelease-a>", lambda event:release())


root.mainloop()