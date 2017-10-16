import pyaudio
import audioop

from basic_buffer import Buffer
from percentile_buffer import PBuffer

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 16384
SECONDS = 5

class Recorder:
    def __init__(self):
        self.observers = []
        self.audio = pyaudio.PyAudio()
        self.audio_buffer = Buffer(RATE * SECONDS)
        self.rms_buffer = PBuffer(int(RATE / CHUNK * SECONDS))

    def register_observer(self, observer):
        self.observers.append(observer)

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)

    def rms(self):
        return audioop.rms(bytes(self.audio_buffer.get()), 2)

    def start(self):
        self.stream = self.audio.open(format=FORMAT, channels=CHANNELS,
                        input_device_index=2,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

        while(True):
            for i in range(0, int(RATE / CHUNK)):
                self.audio_buffer.put(self.stream.read(CHUNK))
            self.rms_buffer.put([self.rms()])
            self.update_observers(self.rms_buffer.percentile(50))
            
    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

