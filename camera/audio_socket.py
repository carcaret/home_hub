import _thread
import json
from channels import Channel

from .audio.audio_recorder import Recorder

recorder = Recorder()
thread_started = False

class Sender:
    def update(self, arg):
        print("new value: {}".format(arg))

def ws_connect(message):
    if thread_started == False:
        thread_started == True
        sender = Sender()
        recorder.register_observer(sender)
        _thread.start_new_thread(recorder.start, ())


