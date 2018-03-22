from pydub import AudioSegment
# import matplotlib.pyplot as plt
import numpy as np
import time

song = AudioSegment.from_mp3('mp3/lonely.mp3')
# song = song.set_frame_rate(10)
song = song.get_array_of_samples()
song = np.abs(song)

song_clean = []
CHUNK = 50

for i in range(CHUNK,len(song), CHUNK):
    data = song[i - CHUNK:i + CHUNK]
    peak = np.average(data)

    if peak > 12000:
        song_clean.append(12000)
    else:
        song_clean.append(peak)
    # print("%04d %05d %s"%(i,peak,bars))
    # time.sleep(0.1)

for each in song_clean:
    

# plt.plot(song_clean)
# plt.show()
