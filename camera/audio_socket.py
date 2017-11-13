import _thread
import json
from channels import Channel

from .audio.audio_recorder import Recorder

MAX_VALUE=3000.0

recorder = Recorder()
thread_started = False

class Sender:
    def __init__(self, channel):
        self.channel = channel

    def normalize(self, value):
        if value > MAX_VALUE:
            value = MAX_VALUE
        return value / MAX_VALUE

    def update(self, arg):
        self.channel.send({
            "text": json.dumps({
                "value": self.normalize(arg),
            })
        })

def ws_connect(message):
    if thread_started == False:
        thread_started == True
        sender = Sender(message.reply_channel)
        recorder.register_observer(sender)
        _thread.start_new_thread(recorder.start, ())


