import os

os.system("python3 /Users/yuhaomao/Desktop/magenta/magenta/models/polyphony_rnn/polyphony_rnn_generate.py --bundle_file=/Users/yuhaomao/Downloads/polyphony_rnn.mag --output_dir=/tmp/polyphony_rnn/generated --num_outputs=10 --num_steps=128 --primer_pitches=\"[67,64,60]\" --condition_on_primer=true --inject_primer_during_generation=false")