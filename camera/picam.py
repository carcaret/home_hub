from os import kill
from signal import SIGKILL
from subprocess import call,check_output,CalledProcessError

def start_picam():
    pids = get_pids('picam')
    if not pids:
        call('picam --alsadev hw:1,0 -w 1280 -h 720 -f 30 -o /run/shm/hls &', shell=True)

def stop_picam():
    pids = get_pids('picam')
    for pid in pids:
        kill(pid, SIGKILL)

def get_pids(name):
    pids = []
    try:
        pids = map(int, check_output(['pidof', name]).split())
    except CalledProcessError as ex:
        print(ex)
    return pids
        
        
