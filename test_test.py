from magenta.music.midi_io import midi_file_to_sequence_proto
import time
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
start_time = time.time()

filename = "/Users/yuhaomao/Downloads/twinkle_twinkle.mid"

note_sequ = midi_file_to_sequence_proto(filename)

def sleep(x):
    time.sleep(x)
sleep(1)

end_time = time.time()

time_dif = end_time - start_time
print(start_time)
print(end_time)
print(time_dif)
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