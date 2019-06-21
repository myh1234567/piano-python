# import numpy
# import pyaudio
# import fluidsynth
# from fluidsynth import *
# import sys
#
# pa = pyaudio.PyAudio()
# strm = pa.open(
#     format = pyaudio.paInt16,
#     channels = 2,
#     rate = 44100,
#     output = True)
#
# status = True
#
# def play_note(pitch):
#     s = []
#     fl = fluidsynth.Synth()
#     sfid = fl.sfload("/Users/yuhaomao/Downloads/Steinway B-JNv2.0.sf2")
#     fl.program_select(0, sfid, 0, 0)
#     fl.program_select(1, sfid, 0, 0)
#     fl.program_select(2, sfid, 0, 0)
#     fl.program_select(3, sfid, 0, 0)
#     fl.program_select(4, sfid, 0, 0)
#     fl.program_select(5, sfid, 0, 0)
#     if status == True:
#         for i in pitch:
#             fl.noteon(pitch.index(i), i, 100)
#         s = []
#         s = numpy.append(s, fl.get_samples(44100 * 1))
#         fl.noteoff(pitch.index(i), i)
#         fl.delete()
#
#         samps = fluidsynth.raw_audio_string(s)
#         strm.write(samps)
#     else:
#         return
#
# # i= 0
# # for a in range(10000):
# #     if i == 10:
# #         print("start")
# #         # play_note([60,70,54,63,75])
# #         play_note([60])
# #         # print("note 60")
# #         # print("70 start")
# #         # play_note([70])
# #         # print("70 finish")
# #         i+=1
# #     else:
# #         i+=1
# #         print("i + 1")
# #
# #     if i == 20:
# #         i = 0
# #         status = False
# import os
#
# for i in range(10000):
#     a = "False"
#
#     os.system(a)
#
import multiprocessing
# def write_file(filename,num):
#     target = open(filename, 'w')
#     for i in range(1,num+1):
#         target.write("%d line\n" % i)

from time import sleep
import threading

def printvalue(x):
    print("x")
    print(x)
    print(count)
    sleep(10)

def printvaluey(y):
    print("y")
    print(y)
    print(count)
    sleep(10)

count = 0
for f in range(300):
    print("count",count)
    p1 = threading.Thread(target=printvalue, args=(f,))
    p2 = threading.Thread(target=printvaluey, args=(f,))

    p1.start()
    p2.start()
    count +=1
