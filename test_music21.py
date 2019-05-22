import pygame
import pyaudio

pygame.mixer.init(44100, -16,2,2048)

pitch = 0
velocity = 0
end_time = 0
start_time = 0
chunk = 1024

# note_sequence = {pitch: 60, velocity: 100, start_time: 0.25, end_time: 0.25}
note_sequence = """ticks_per_quarter: 220
tempos {
  qpm: 120.0
}
notes {
  pitch: 60
  velocity: 100
  end_time: 0.25
}
notes {
  pitch: 60
  velocity: 100
  start_time: 0.25
  end_time: 0.5
}
notes {
  pitch: 67
  velocity: 100
  start_time: 0.5
  end_time: 0.75
}
notes {
  pitch: 67
  velocity: 100
  start_time: 0.75
  end_time: 1.0
}
notes {
  pitch: 67
  velocity: 100
  start_time: 1.25
  end_time: 1.5
}
notes {
  pitch: 67
  velocity: 100
  start_time: 1.5
  end_time: 1.75
}
notes {
  pitch: 69
  velocity: 100
  start_time: 1.75
  end_time: 2.0
}
notes {
  pitch: 60
  velocity: 100
  start_time: 2.0
  end_time: 2.25
}
notes {
  pitch: 60
  velocity: 100
  start_time: 2.25
  end_time: 2.5
}
notes {
  pitch: 69
  velocity: 100
  start_time: 2.5
  end_time: 2.75
}
notes {
  pitch: 76
  velocity: 100
  start_time: 2.75
  end_time: 3.0
}
notes {
  pitch: 76
  velocity: 100
  start_time: 3.0
  end_time: 3.25
}
notes {
  pitch: 76
  velocity: 100
  start_time: 3.25
  end_time: 3.5
}
notes {
  pitch: 76
  velocity: 100
  start_time: 3.5
  end_time: 3.75
}
notes {
  pitch: 71
  velocity: 100
  start_time: 4.0
  end_time: 4.25
}
notes {
  pitch: 68
  velocity: 100
  start_time: 4.25
  end_time: 4.5
}
notes {
  pitch: 63
  velocity: 100
  start_time: 4.5
  end_time: 4.75
}
notes {
  pitch: 64
  velocity: 100
  start_time: 4.75
  end_time: 5.25
}
notes {
  pitch: 64
  velocity: 100
  start_time: 5.25
  end_time: 5.5
}
notes {
  pitch: 60
  velocity: 100
  start_time: 5.5
  end_time: 5.75
}
notes {
  pitch: 65
  velocity: 100
  start_time: 5.75
  end_time: 6.0
}
notes {
  pitch: 64
  velocity: 100
  start_time: 6.25
  end_time: 6.5
}
notes {
  pitch: 69
  velocity: 100
  start_time: 6.5
  end_time: 6.75
}
notes {
  pitch: 69
  velocity: 100
  start_time: 6.75
  end_time: 7.25
}
notes {
  pitch: 67
  velocity: 100
  start_time: 7.25
  end_time: 7.5
}
notes {
  pitch: 69
  velocity: 100
  start_time: 7.5
  end_time: 7.875
}
notes {
  pitch: 60
  velocity: 100
  start_time: 8.0
  end_time: 8.375
}
notes {
  pitch: 60
  velocity: 100
  start_time: 8.375
  end_time: 8.5
}
notes {
  pitch: 60
  velocity: 100
  start_time: 8.5
  end_time: 8.75
}
notes {
  pitch: 60
  velocity: 100
  start_time: 8.75
  end_time: 9.0
}
notes {
  pitch: 60
  velocity: 100
  start_time: 9.125
  end_time: 9.25
}
notes {
  pitch: 60
  velocity: 100
  start_time: 9.25
  end_time: 9.5
}
notes {
  pitch: 60
  velocity: 100
  start_time: 9.5
  end_time: 9.625
}
notes {
  pitch: 62
  velocity: 100
  start_time: 9.625
  end_time: 10.0
}
notes {
  pitch: 64
  velocity: 100
  start_time: 10.0
  end_time: 10.375
}
notes {
  pitch: 64
  velocity: 100
  start_time: 10.5
  end_time: 10.75
}
notes {
  pitch: 68
  velocity: 100
  start_time: 10.75
  end_time: 11.125
}
notes {
  pitch: 68
  velocity: 100
  start_time: 11.125
  end_time: 11.25
}
notes {
  pitch: 67
  velocity: 100
  start_time: 11.5
  end_time: 11.625
}
notes {
  pitch: 69
  velocity: 100
  start_time: 11.625
  end_time: 11.875
}
notes {
  pitch: 72
  velocity: 100
  start_time: 12.0
  end_time: 12.375
}
notes {
  pitch: 67
  velocity: 100
  start_time: 12.5
  end_time: 12.75
}
notes {
  pitch: 68
  velocity: 100
  start_time: 12.75
  end_time: 13.125
}
notes {
  pitch: 70
  velocity: 100
  start_time: 13.25
  end_time: 13.5
}
notes {
  pitch: 70
  velocity: 100
  start_time: 13.5
  end_time: 13.625
}
notes {
  pitch: 69
  velocity: 100
  start_time: 13.625
  end_time: 13.875
}
notes {
  pitch: 72
  velocity: 100
  start_time: 14.0
  end_time: 14.375
}
notes {
  pitch: 67
  velocity: 100
  start_time: 14.5
  end_time: 14.625
}
notes {
  pitch: 67
  velocity: 100
  start_time: 14.625
  end_time: 14.75
}
notes {
  pitch: 67
  velocity: 100
  start_time: 14.75
  end_time: 14.875
}
notes {
  pitch: 67
  velocity: 100
  start_time: 14.875
  end_time: 15.0
}
notes {
  pitch: 63
  velocity: 100
  start_time: 15.0
  end_time: 15.375
}
notes {
  pitch: 62
  velocity: 100
  start_time: 15.375
  end_time: 15.625
}
notes {
  pitch: 60
  velocity: 100
  start_time: 15.625
  end_time: 15.875
}
notes {
  pitch: 58
  velocity: 100
  start_time: 15.875
  end_time: 16.0
}
total_time: 16.0"""
# pygame.mixer_music.load(note_sequence)
# pygame.mixer_music.play()

data = note_sequence.readframe(chunk)

# p = pyaudio.PyAudio()
#
# stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
#                 channels = wf.getnchannels(),
#                 rate = wf.getframerate(),
#                 output = True)