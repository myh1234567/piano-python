from tkinter import *
import time
import tkinter as Tk
import pygame

pygame.mixer.init(44100, -16,2,2048)

pitch_list = []

root = Tk.Tk()
root.title("Panio GUI")
root.configure(background = "red")

str1 = StringVar()
str1.set("Just Like Music")

mainframe = Frame(root,bg = "white",bd = 20)
mainframe.grid()


tmp_frame1 = Frame(mainframe,bg = "white",bd = 20)
tmp_frame1.grid()
tmp_frame2 = Frame(mainframe,bg = "white",bd = 20)
tmp_frame2.grid()
tmp_frame3 = Frame(mainframe,bg = "white",bd = 20)
tmp_frame3.grid()


def value_Cs():
    global pitch_list
    str1.set("C#")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/C_s.wav")
    sound.play()
    pitch_list.append(61)
    btnCs.config(bg="Tan", fg="black")
    root.after(100,btnCs)

btnCs = Tk.Label(tmp_frame2,height = 6, width = 8,text = "C#",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnCs.grid(row = 0, column = 1, padx = 5, pady = 5)
btnCs.bind("<Button-1>",lambda event:value_Cs())
root.bind("<e>", lambda event: value_Cs())

root.mainloop()