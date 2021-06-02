import wave


recorded_file = wave.open('Recorded_Audio_Clip_16b_PCM.wav')
n = recorded_file.getnchannels()
print('no. of audio channels ->',n)
frame_rate = recorded_file.getframerate()
print('frame rate ->', frame_rate)
no_of_frames = recorded_file.getnframes()
print('no. of audio frames ->',no_of_frames)
sample_width = recorded_file.getsampwidth()
print('width of a sample in bytes ->',sample_width)
recorded_file.close()