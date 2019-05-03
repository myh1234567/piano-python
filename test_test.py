from magenta.music.midi_io import midi_file_to_sequence_proto

# testMidiFileToMelody(self):

# filename = os.path.join(tf.resource_loader.get_data_files_path(),
#                         'testdata', 'melody.mid')
filename = "/Users/yuhaomao/Downloads/twinkle_twinkle.mid"

note_sequ = midi_file_to_sequence_proto(filename)

"""
输出格式：

notes {
  pitch: 67
  velocity: 85
  start_time: 20.400000000000002
  end_time: 21.0
}

total time: 28.8

control_changes {
  control_number: 91
  control_value: 48
}

"""
