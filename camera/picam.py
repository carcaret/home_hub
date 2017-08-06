from os import kill
from signal import SIGKILL
from subprocess import call,check_output,CalledProcessError

from django.conf import settings

def start_picam():
    pids = get_pids('picam')
    if not pids:
        call(settings.PICAM_COMMAND, shell=True)

def stop_picam():
    pids = get_pids('picam')
    for pid in pids:
        print('Killing process {}'.format(pid))
        kill(pid, SIGKILL)

def get_pids(name):
    pids = []
    try:
        pids = map(int, check_output(['pidof', name]).split())
    except CalledProcessError as ex:
        print(ex)
    return pids
        
        
