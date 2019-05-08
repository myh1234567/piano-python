import pygame as pg
import sys

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

# music_file1 = "/private/tmp/improv_rnn/generated/2019-05-07_014920_10.mid"
# music_file2 = "/Users/yuhaomao/Downloads/twinkle_twinkle.mid"
#music_file = "Drumtrack.mp3"

freq = 44100  # audio CD quality
bitsize = -16  # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 2048  # number of samples (experiment to get right sound)
pg.mixer.init(freq, bitsize, channels, buffer)
# optional volume 0 to 1.0
pg.mixer.music.set_volume(0.8)



try:
  play_music(sys.argv[1])
except KeyboardInterrupt:
  # if user hits Ctrl/C then exit
  # (works only in console mode)
  pg.mixer.music.fadeout(1000)
  pg.mixer.music.stop()
  raise SystemExit
