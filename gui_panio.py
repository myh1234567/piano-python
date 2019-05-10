from tkinter import *
import time
import datetime
import pygame
import tkinter as Tk
import threading
import os
import psutil
from kill import kill
# pygame.init()
pygame.mixer.init(44100, -16,2,2048)

pitch_list = []
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
Time1 = StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H/%M/%S"))

def setblackkey(item):
    item.config(bg="black",fg="white")

def setwhitekey(item):
    item.config(bg="Gainsboro", fg="black")

def value_Cs():
    str1.set("C#")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/C_s.wav")
    sound.play()
    pitch_list.append(61)
    btnCs.config(bg="Tan", fg="black")
    root.after(100,setblackkey,btnCs)

def value_Ds():
    str1.set("D#")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/D_s.wav")
    sound.play()
    pitch_list.append(63)
    btnDs.config(bg="Tan", fg="black")
    root.after(100, setblackkey, btnDs)

def value_Fs():
    str1.set("F#")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/F_s.wav")
    sound.play()
    pitch_list.append(66)
    btnFs.config(bg="Tan", fg="black")
    root.after(100, setblackkey, btnFs)

def value_Gs():
    str1.set("G#")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/G_s.wav")
    sound.play()
    pitch_list.append(68)
    btnGs.config(bg="Tan", fg="black")
    root.after(100, setblackkey, btnGs)

def value_Bb():
    str1.set("Bb")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/Bb.wav")
    sound.play()
    pitch_list.append(70)
    btnBb.config(bg="Tan", fg="black")
    root.after(100, setblackkey, btnBb)

def value_Cs1():
    str1.set("C_s1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/C_s1.wav")
    sound.play()
    pitch_list.append(73)
    btnCs1.config(bg="Tan", fg="black")
    root.after(100, setblackkey, btnCs1)

def value_Ds1():
    str1.set("D_s1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/D_s1.wav")
    sound.play()
    pitch_list.append(75)
    btnDs1.config(bg="Tan", fg="black")
    root.after(100, setblackkey, btnDs1)

def value_C():
    str1.set("C")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/C.wav")
    sound.play()
    pitch_list.append(60)
    btnC.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnC)

def value_D():
    str1.set("D")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/D.wav")
    sound.play()
    pitch_list.append(62)
    btnD.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnD)

def value_E():
    str1.set("E")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/E.wav")
    sound.play()
    pitch_list.append(64)
    btnE.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnE)

def value_F():
    str1.set("F")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/F.wav")
    sound.play()
    pitch_list.append(65)
    btnF.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnF)

def value_G():
    str1.set("G")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/G.wav")
    sound.play()
    pitch_list.append(67)
    btnG.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnG)
    print(pitch_list)

def value_A():
    str1.set("A")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/A.wav")
    sound.play()
    pitch_list.append(69)
    btnA.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnA)

def value_B():
    str1.set("B")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/B.wav")
    sound.play()
    pitch_list.append(71)
    btnB.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnB)

def value_C1():
    str1.set("C1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/C1.wav")
    sound.play()
    pitch_list.append(72)
    btnC1.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnC1)

def value_D1():
    str1.set("D1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/D1.wav")
    sound.play()
    pitch_list.append(74)
    btnD1.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnD1)

def value_E1():
    str1.set("E1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/E1.wav")
    sound.play()
    pitch_list.append(76)
    btnE1.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnE1)

def value_F1():
    str1.set("F1")
    sound = pygame.mixer.Sound("/Users/yuhaomao/Downloads/Music_Notes/F1.wav")
    sound.play()
    pitch_list.append(77)
    btnF1.config(bg="DimGray", fg="white")
    root.after(100, setwhitekey, btnF1)



# ==========Lable with Title========= #

Label(tmp_frame1,text = "Piano Musical Keys",font = ("Impact",25,"bold"), bg = "white").grid(row = 0, column = 0, columnspan = 11)

# =================================== text

txtDate = Entry(tmp_frame1, textvariable = Date1,font = ("arial",18,"bold"), bg = "white").grid(row = 1, column = 0,pady = 1)

txtDisplay = Entry(tmp_frame1, textvariable = str1,font = ("arial",18,"bold"), bg = "white").grid(row = 1, column = 1,pady = 1)

txtTime = Entry(tmp_frame1, textvariable = Time1,font = ("arial",18,"bold"), bg = "white").grid(row = 1, column = 2,pady = 1)

#=================================== black key
space = Tk.Label(tmp_frame2,height = 6, width = 4,text = "",font = ("arial",18,"bold"), bg = "white",fg = "white")
space.grid(row = 0, column = 0, padx = 5, pady = 5)

btnCs = Tk.Label(tmp_frame2,height = 6, width = 8,text = "C#",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnCs.grid(row = 0, column = 1, padx = 5, pady = 5)
btnCs.bind("<Button-1>",lambda event:value_Cs())
root.bind("<e>", lambda event: value_Cs())


btnDs = Tk.Label(tmp_frame2,height = 6, width = 8,text = "D#", bg = "black",fg = "white",font = ("arial",18,"bold"))
btnDs.grid(row = 0, column = 2, padx = 5, pady = 5)
btnDs.bind("<Button-1>",lambda event:value_Ds())
root.bind("<r>", lambda event: value_Ds())

space = Tk.Label(tmp_frame2,height = 6, width = 4,text = "",font = ("arial",18,"bold"), bg = "white",fg = "white")
space.grid(row = 0, column = 3, padx = 5, pady = 5)

space = Tk.Label(tmp_frame2,height = 6, width = 4,text = "",font = ("arial",18,"bold"), bg = "white",fg = "white")
space.grid(row = 0, column = 4, padx = 5, pady = 5)

btnFs = Tk.Label(tmp_frame2,height = 6, width = 8, text="F#", bg = "black",fg="white", font = ("arial",18,"bold"))
btnFs.grid(row = 0, column = 5, padx = 5, pady = 5)
btnFs.bind("<Button-1>",lambda event:value_Fs())
root.bind("<t>", lambda event: value_Fs())


btnGs = Tk.Label(tmp_frame2,height = 6, width = 8,text = "G#",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnGs.grid(row = 0, column = 6, padx = 5, pady = 5)
btnGs.bind("<Button-1>",lambda event:value_Gs())
root.bind("<y>", lambda event: value_Gs())


btnBb = Tk.Label(tmp_frame2,height = 6, width = 8,text = "Bb",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnBb.grid(row = 0, column = 7, padx = 5, pady = 5)
btnBb.bind("<Button-1>",lambda event:value_Bb())
root.bind("<u>", lambda event: value_Bb())

space = Tk.Label(tmp_frame2,height = 6, width = 4,text = "",font = ("arial",18,"bold"), bg = "white",fg = "white")
space.grid(row = 0, column = 8, padx = 5, pady = 5)

space = Tk.Label(tmp_frame2,height = 6, width = 4,text = "",font = ("arial",18,"bold"), bg = "white",fg = "white")
space.grid(row = 0, column = 9, padx = 5, pady = 5)

btnCs1 = Tk.Label(tmp_frame2,height = 6, width = 8,text = "C#1",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnCs1.grid(row = 0, column = 10, padx = 5, pady = 5)
btnCs1.bind("<Button-1>",lambda event:value_Cs1())
root.bind("<i>", lambda event: value_Cs1())


btnDs1 = Tk.Label(tmp_frame2,height = 6, width = 8,text = "D#1",font = ("arial",18,"bold"), bg = "black",fg = "white")
btnDs1.grid(row = 0, column = 11, padx = 5, pady = 5)
btnDs1.bind("<Button-1>",lambda event:value_Ds1())
root.bind("<o>", lambda event: value_Ds1())

space = Tk.Label(tmp_frame2,height = 6, width = 4,text = "",font = ("arial",18,"bold"), bg = "white",fg = "white")
space.grid(row = 0, column = 12, padx = 5, pady = 5)

space = Tk.Label(tmp_frame2,height = 6, width = 4,text = "",font = ("arial",18,"bold"), bg = "white",fg = "white")
space.grid(row = 0, column = 13, padx = 5, pady = 5)

space = Tk.Label(tmp_frame2,height = 6, width = 4,text = "",font = ("arial",18,"bold"), bg = "white",fg = "white")
space.grid(row = 0, column = 14, padx = 5, pady = 5)

# =================================== white key
btnC = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "C",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnC.grid(row = 1, column = 0, padx = 5, pady = 5)
btnC.bind("<Button-1>",lambda event:value_C())
root.bind("<a>", lambda event: value_C())


btnD = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "D",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnD.grid(row = 1, column = 1, padx = 5, pady = 5)
btnD.bind("<Button-1>",lambda event:value_D())
root.bind("<s>", lambda event: value_D())


btnE = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "E",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnE.grid(row = 1, column = 2, padx = 5, pady = 5)
btnE.bind("<Button-1>",lambda event:value_E())
root.bind("<d>", lambda event: value_E())


btnF = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "F",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnF.grid(row = 1, column = 3, padx = 5, pady = 5)
btnF.bind("<Button-1>",lambda event:value_F())
root.bind("<f>", lambda event: value_F())


btnG = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "G",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnG.grid(row = 1, column = 4, padx = 5, pady = 5)
btnG.bind("<Button-1>",lambda event:value_G())
root.bind("<g>", lambda event: value_G())


btnA = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "A",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnA.grid(row = 1, column = 5, padx = 5, pady = 5)
btnA.bind("<Button-1>",lambda event:value_A())
root.bind("<h>", lambda event: value_A())


btnB = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "B",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnB.grid(row = 1, column = 6, padx = 5, pady = 5)
btnB.bind("<Button-1>",lambda event:value_B())
root.bind("<j>", lambda event: value_B())


btnC1 = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "C1",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnC1.grid(row = 1, column = 7, padx = 5, pady = 5)
btnC1.bind("<Button-1>",lambda event:value_C1())
root.bind("<k>", lambda event: value_C1())


btnD1 = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "D1",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnD1.grid(row = 1, column = 8, padx = 5, pady = 5)
btnD1.bind("<Button-1>",lambda event:value_D1())
root.bind("<l>", lambda event: value_D1())


btnE1 = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "E1",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnE1.grid(row = 1, column = 9, padx = 5, pady = 5)
btnE1.bind("<Button-1>",lambda event:value_E1())
root.bind("<;>", lambda event: value_E1())


btnF1 = Tk.Label(tmp_frame3,height = 6, width = 8,bd = 4,text = "F1",font = ("arial",18,"bold"), bg = "Gainsboro",fg = "black")
btnF1.grid(row = 1, column = 10, padx = 5, pady = 5)
btnF1.bind("<Button-1>",lambda event:value_F1())
root.bind("<'>", lambda event: value_F1())

# ==========detect keyboard input
def root_exit():
    # global pids_begin
    # pids_begin = psutil.pids()
    # print("111")
    # print(pids_begin)
    print("111")
    os.system("python3 /Users/yuhaomao/Desktop/magenta/magenta/models/melody_rnn/melody_rnn_generate.py --config=lookback_rnn --bundle_file=/Users/yuhaomao/Downloads/lookback_rnn.mag --output_dir=/tmp/melody_rnn/generated --num_outputs=30 --num_steps=128 --primer_melody=\"%s\"" % str(pitch_list))
    # os.system("python3 /Users/yuhaomao/PycharmProjects/piano-python/play_midi.py /private/tmp/melody_rnn/generated/2019-05-07_143707_30.mid")
    pygame.mixer.music.load("/private/tmp/melody_rnn/generated/2019-05-07_143707_30.mid")
    pygame.mixer.music.play()
timer=threading.Timer(3,root_exit)


def detectInput():
    global timer
    timer.cancel()
    timer = threading.Timer(3,root_exit)
    timer.start()

def stop_music():
    pygame.mixer.music.stop()
    # pids_stop = psutil.pids()
    # print("222")
    # print(pids_stop)
    # kill(pids_stop[-1])
    # for pid in pids_stop:
    #     # if pid not in pids_begin:
    #     p = psutil.Process(pid)
    #     print("pid-%d,pname-%s" % (pid, p.name()))
    #         # kill(pid)
    #         pass


root.bind("<KeyRelease>", lambda event:detectInput())
root.bind("<Button-1>", lambda event:stop_music())
#========= main loop

root.mainloop()