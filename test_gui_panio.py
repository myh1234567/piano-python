from tkinter import *
import time
import datetime
import pygame
import tkinter as Tk
# pygame.init()
pygame.mixer.init(44100, -16,2,2048)

root = Tk.Tk()
root.title("Panio GUI")
# width,height = 1000,500
# root.geometry("%dx%d+30+30"%(width,height))
root.configure(background = "white")

mainframe = Frame(root,bg = "white",bd = 20)
mainframe.grid()


tmp_frame1 = Frame(mainframe,bg = "white",bd = 20)
tmp_frame1.grid()
tmp_frame2 = Frame(mainframe,bg = "white",bd = 20)
tmp_frame2.grid()
tmp_frame3 = Frame(mainframe,bg = "white",bd = 20)
tmp_frame3.grid()


str1 = StringVar()
str1.set("Just Like Music")
Date1 = StringVar()
Time1 = StringVar ()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H/%M/%S"))

def value_Cs():
    str1.set("C#")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/C_s.wav")
    sound.play()

def value_Ds():
    str1.set("D#")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/D_s.wav")
    sound.play()

def value_Fs():
    str1.set("F#")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/F_s.wav")
    sound.play()

def value_Gs():
    str1.set("G#")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/G_s.wav")
    sound.play()

def value_Bb():
    str1.set("Bb")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/Bb.wav")
    sound.play()

def value_Cs1():
    str1.set("C_s1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/C_s1.wav")
    sound.play()

def value_Ds1():
    str1.set("D_s1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/D_s1.wav")
    sound.play()

def value_C():
    str1.set("C")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/C.wav")
    sound.play()

def value_D():
    str1.set("D")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/D.wav")
    sound.play()

def value_E():
    str1.set("E")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/E.wav")
    sound.play()

def value_F():
    str1.set("F")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/F.wav")
    sound.play()

def value_G():
    str1.set("G")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/G.wav")
    sound.play()

def value_A():
    str1.set("A")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/A.wav")
    sound.play()

def value_B():
    str1.set("B")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/B.wav")
    sound.play()

def value_C1():
    str1.set("C1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/C1.wav")
    sound.play()

def value_D1():
    str1.set("D1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/D1.wav")
    sound.play()

def value_E1():
    str1.set("E1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/E1.wav")
    sound.play()

def value_F1():
    str1.set("F1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/F1.wav")
    sound.play()

# ==========Lable with Title========= #

Label(tmp_frame1,text = "Piano Musical Keys",font = ("Impact",25,"bold"), bg = "white").grid(row = 0, column = 0, columnspan = 11)

# =================================== text

txtDate = Entry(tmp_frame1, textvariable = Date1,font = ("arial",18,"bold"), bg = "white").grid(row = 1, column = 0,pady = 1)

txtDisplay = Entry(tmp_frame1, textvariable = str1,font = ("arial",18,"bold"), bg = "white").grid(row = 1, column = 1,pady = 1)

txtTime = Entry(tmp_frame1, textvariable = Time1,font = ("arial",18,"bold"), bg = "white").grid(row = 1, column = 2,pady = 1)

#=================================== black key
btnCs = Tk.Label(tmp_frame2,height = 6, width = 6,text = "C#",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnCs.grid(row = 0, column = 0, padx = 5, pady = 5)
btnCs.bind("<Button-1>",lambda event:value_Cs())
root.bind("<e>", lambda event: value_Cs())


btnDs = Tk.Label(tmp_frame2,height = 6, width = 6,text = "D#", bg = "black",fg = "white",font = ("arial",18,"bold"))
btnDs.grid(row = 0, column = 1, padx = 5, pady = 5)
btnDs.bind("<Button-1>",lambda event:value_Ds())
root.bind("<r>", lambda event: value_Ds())


btnFs = Tk.Label(tmp_frame2,height = 6, width = 6, text="F#", bg = "black",fg="white", font = ("arial",18,"bold"))
btnFs.grid(row = 0, column = 2, padx = 5, pady = 5)
btnFs.bind("<Button-1>",lambda event:value_Fs())
root.bind("<t>", lambda event: value_Fs())


btnGs = Tk.Label(tmp_frame2,height = 6, width = 6,text = "G#",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnGs.grid(row = 0, column = 3, padx = 5, pady = 5)
btnGs.bind("<Button-1>",lambda event:value_Gs())
root.bind("<y>", lambda event: value_Gs())


btnBb = Tk.Label(tmp_frame2,height = 6, width = 6,bd = 4,text = "Bb",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnBb.grid(row = 0, column = 4, padx = 5, pady = 5)
btnBb.bind("<Button-1>",lambda event:value_Bb())
root.bind("<u>", lambda event: value_Bb())


btnCs1 = Tk.Label(tmp_frame2,height = 6, width = 6,bd = 4,text = "C#1",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnCs1.grid(row = 0, column = 5, padx = 5, pady = 5)
btnCs1.bind("<Button-1>",lambda event:value_Cs1())
root.bind("<i>", lambda event: value_Cs1())


btnDs1 = Tk.Label(tmp_frame2,height = 6, width = 6,bd = 4,text = "D#1",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnDs1.grid(row = 0, column = 6, padx = 5, pady = 5)
btnDs1.bind("<Button-1>",lambda event:value_Ds1())
root.bind("<o>", lambda event: value_Ds1())



# =================================== white key
btnC = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "C",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnC.grid(row = 0, column = 0, padx = 5, pady = 5)
btnC.bind("<Button-1>",lambda event:value_C())
root.bind("<a>", lambda event: value_C())


btnD = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "D",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnD.grid(row = 0, column = 1, padx = 5, pady = 5)
btnD.bind("<Button-1>",lambda event:value_D())
root.bind("<s>", lambda event: value_D())


btnE = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "E",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnE.grid(row = 0, column = 2, padx = 5, pady = 5)
btnE.bind("<Button-1>",lambda event:value_E())
root.bind("<d>", lambda event: value_E())


btnF = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "F",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnF.grid(row = 0, column = 3, padx = 5, pady = 5)
btnF.bind("<Button-1>",lambda event:value_F())
root.bind("<f>", lambda event: value_F())


btnG = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "G",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnG.grid(row = 0, column = 4, padx = 5, pady = 5)
btnG.bind("<Button-1>",lambda event:value_G())
root.bind("<g>", lambda event: value_G())


btnA = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "A",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnA.grid(row = 0, column = 5, padx = 5, pady = 5)
btnA.bind("<Button-1>",lambda event:value_A())
root.bind("<h>", lambda event: value_A())


btnB = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "B",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnB.grid(row = 0, column = 6, padx = 5, pady = 5)
btnB.bind("<Button-1>",lambda event:value_B())
root.bind("<j>", lambda event: value_B())


btnC1 = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "C1",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnC1.grid(row = 0, column = 7, padx = 5, pady = 5)
btnC1.bind("<Button-1>",lambda event:value_C1())
root.bind("<k>", lambda event: value_C1())


btnD1 = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "D1",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnD1.grid(row = 0, column = 8, padx = 5, pady = 5)
btnD1.bind("<Button-1>",lambda event:value_D1())
root.bind("<l>", lambda event: value_D1())


btnE1 = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "E1",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnE1.grid(row = 0, column = 9, padx = 5, pady = 5)
btnE1.bind("<Button-1>",lambda event:value_E1())
root.bind("<;>", lambda event: value_E1())


btnF1 = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "F1",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnF1.grid(row = 0, column = 10, padx = 5, pady = 5)
btnF1.bind("<Button-1>",lambda event:value_F1())
root.bind("<'>", lambda event: value_F1())



#========= main loop

root.mainloop()