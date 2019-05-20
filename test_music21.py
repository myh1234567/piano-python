from music21 import *

p1 = pitch.Pitch('c#4')

print(p1.octave)

print(p1.pitchClass)

print(p1.name)

print(p1.midi)


n1 = note.Note()
n1.pitch

print(n1.duration)

n1.pitch.nameWithOctave = 'E-5'
n1.duration.quarterLength = 3.0

print(n1.duration.type)

print(n1.duration.dots)

print(n1.pitch.name)

print(n1.pitch.accidental)

print(n1.octave)

print(n1.name)

print(n1.quarterLength)

n1.quarterLength = 1.0

otherNote = note.Note("F6")
otherNote.lyric = "I'm the Queen of the Night!"


n1.addLyric(n1.nameWithOctave)
n1.addLyric(n1.pitch.pitchClassString)

n1.addLyric('QL: %s' % n1.quarterLength)


n1.show()

n1.quarterLength = 6.25
n1.show()