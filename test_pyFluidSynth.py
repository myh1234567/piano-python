import time
import numpy
import pyaudio
import fluidsynth
from fluidsynth import *

pa = pyaudio.PyAudio()
strm = pa.open(
    format = pyaudio.paInt16,
    channels = 2,
    rate = 44100,
    output = True)

s = []

fl = fluidsynth.Synth()

# Initial silence is 1 second
# s = numpy.append(s, fl.get_samples(44100 * 1))
print("111")
print(s)
print("222")

# settings = new_fluid_settings()
# synth = new_fluid_synth(settings)
# sfid = fl.sfload("/Users/yuhaomao/Desktop/pyfluidsynth/test/example.sf2", 7)
sfid = fl.sfload("/Users/yuhaomao/Downloads/Steinway B-JNv2.0.sf2")
fl.program_select(0, sfid, 0, 0) # (channel, soundfont ID, bank, preset )

fl.noteon(0, 60, 100)
# fl.noteon(0, 67, 30)
# fl.noteon(0, 76, 30)
# fluidsynth.fluid_synth_noteon("",0, 60, 100)

# Chord is held for 2 seconds
s = numpy.append(s, fl.get_samples(44100 * 5))
print("333")
print(s)
print("444")
fl.noteoff(0, 60)
# fl.noteoff(0, 67)
# fl.noteoff(0, 76)

# Decay of chord is held for 1 second
# s = numpy.append(s, fl.get_samples(44100 * 1))

fl.delete()

samps = fluidsynth.raw_audio_string(s)

# print (len(samps))
# print ('Starting playback')
strm.write(samps)
