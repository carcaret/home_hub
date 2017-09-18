import pyaudio
import wave

from percentile_buffer import PBuffer

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 16384
 
audio = pyaudio.PyAudio()
   
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    input_device_index=2,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

pbuffer = PBuffer(RATE * SECONDS)

while(True):
    for i in range(0, int(RATE / CHUNK)):
        pbuffer.put(stream.read(CHUNK))
    print(pbuffer.percentile(50))
                                  
stream.stop_stream()
stream.close()
audio.terminate()
