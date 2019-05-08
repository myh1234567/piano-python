# from magenta.music.midi_io import midi_file_to_sequence_proto
# import time
# #
# filename = "/Users/yuhaomao/Downloads/midi0.mid"
#
# note_sequ = midi_file_to_sequence_proto(filename)

# """
# 输出格式：
#
# notes {
#   pitch: 67
#   velocity: 85
#   start_time: 20.400000000000002
#   end_time: 21.0
# }
#
# total time: 28.8
#
# control_changes {
#   control_number: 91
#   control_value: 48
# }
#
# """
# start_time = time.time()
#
# filename = "/Users/yuhaomao/Downloads/twinkle_twinkle.mid"
#
# note_sequ = midi_file_to_sequence_proto(filename)
#
# def sleep(x):
#     time.sleep(x)
# sleep(1)
#
# end_time = time.time()
#
# time_dif = end_time - start_time
# print(start_time)
# print(end_time)
# print(time_dif)
#
#
# # import tkinter as tk
# #
# # master = tk.Tk()
# #
# #
# # def my_mainloop():
# #     print("Hello World!")
# #     master.after(1000, my_mainloop)
# #
# #
# # master.after(1000, my_mainloop)
# #
# # master.mainloop()


# import threading
# import tkinter as tki
#
# def pri():
#     # exit(0)
#     exit(0)
#     # print("???")
#
# tk=tki.Tk()
#
# t=threading.Timer(3,pri)
# t.start()
# #t.cancel()
# tk.mainloop()

# import magenta
# from magenta.models.melody_rnn import melody_rnn_generate
# from magenta.models.melody_rnn import melody_rnn_sequence_generator
# from magenta.models.melody_rnn import melody_rnn_model
#
#
#
# melody_rnn_generate(config="lookback_rnn.mag",
#                     bundle_file="/Users/yuhaomao/Downloads/lookback_rnn.mag",
#                     output_dir="/tmp/melody_rnn/generated",
#                     num_outputs=30, num_steps=128,
#                     primer_melody=[60,-2,60,-2,67,-2,67,-2])

# import os
# primer_melody=[60,-2,60,-2,67,-2,67,-2]
# os.system("python3 /Users/yuhaomao/Desktop/magenta/magenta/models/melody_rnn/melody_rnn_generate.py --config=lookback_rnn --bundle_file=/Users/yuhaomao/Downloads/lookback_rnn.mag --output_dir=/tmp/melody_rnn/generated --num_outputs=30 --num_steps=128 --primer_melody=\"%s\"" % str(primer_melody))

# age = 22
# name = 'Swaroop'
# print ('%s is %d years old' % (name, age))
# print ('Why is %s playing with that python?' % name)

import pygame as pg
def play_music(music_file):
  '''
  stream music with mixer.music module in blocking manner
  this will stream the sound from disk while playing
  '''
  clock = pg.time.Clock()
  try:
    pg.mixer.music.load(music_file)
    print("Music file {} loaded!".format(music_file))
  except pg.error:
    print("File {} not found! {}".format(music_file, pg.get_error()))
    return
  pg.mixer.music.play()
  # check if playback has finished
  while pg.mixer.music.get_busy():
    clock.tick(30)
# pick a midi or MP3 music file you have in the working folder
# or give full pathname
music_file = "/Users/yuhaomao/Downloads/twinkle_twinkle.mid"
#music_file = "Drumtrack.mp3"
freq = 44100  # audio CD quality
bitsize = -16  # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 2048  # number of samples (experiment to get right sound)
pg.mixer.init(freq, bitsize, channels, buffer)
# optional volume 0 to 1.0
pg.mixer.music.set_volume(0.8)
try:
  play_music(music_file)
except KeyboardInterrupt:
  # if user hits Ctrl/C then exit
  # (works only in console mode)
  pg.mixer.music.fadeout(1000)
  pg.mixer.music.stop()
  raise SystemExit