from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
import time

song = AudioSegment.from_mp3('mp3/lonely.mp3')
print(len(song))
song = song.set_frame_rate(44100)
song = song.get_array_of_samples()
song = np.abs(song)

print(len(song))

plt.plot(song)
plt.show()



song_clean = []
CHUNK = 1000

# for i in range(CHUNK,len(song), CHUNK):
#     data = song[i - CHUNK:i + CHUNK]
#     peak = np.average(data)
#
#     if peak > 12000:
#         song_clean.append(12000)
#     else:
#         song_clean.append(peak)
#     # print("%04d %05d %s"%(i,peak,bars))
#     # time.sleep(0.1)
#
# print(len(song))
# print(len(song_clean))
#
# plt.plot(song)
# plt.show()
# plt.plot(song_clean)
# plt.show()
