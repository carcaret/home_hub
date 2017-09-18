import pyaudio
import audioop

from basic_buffer import Buffer
from percentile_buffer import PBuffer

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 16384
SECONDS = 5
 
def rms(audio_buffer):
    return audioop.rms(bytes(audio_buffer.get()), 2)

audio = pyaudio.PyAudio()
   
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    input_device_index=2,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

audio_buffer = Buffer(RATE * SECONDS)
rms_buffer = PBuffer(int(RATE / CHUNK * SECONDS))

while(True):
    for i in range(0, int(RATE / CHUNK)):
        audio_buffer.put(stream.read(CHUNK))
    rms_buffer.put([rms(audio_buffer)])
                                  
stream.stop_stream()
stream.close()
audio.terminate()

