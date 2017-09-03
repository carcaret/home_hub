from .base import *

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'raspberrypi',
]

STREAM_URL = 'http://raspberrypi/hls/index.m3u8'
STREAM_KEY = 'f0f1f2f3f4f5f6f7f8f9fafbfcfdfefe'

PICAM_COMMAND = 'picam --alsadev hw:1,0 -w 1280 -h 720 -f 30 -o /run/shm/hls --tcpout tcp://127.0.0.1:8181 &'
#PICAM_COMMAND = 'picam --alsadev hw:1,0 -w 1280 -h 720 -f 30 -o /run/shm/hls \
#        --hlsenc --hlsenckeyur http://raspberrypi/camera/enc.key --hlsenckey f0f1f2f3f4f5f6f7f8f9fafbfcfdfefe --hlsenciv 000102030405060708090a0b0c0d0e0f &'
