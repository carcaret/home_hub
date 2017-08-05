from signal import SIGKILL
from subprocess import check_output,CalledProcessError

def stop_picam():
    pids = get_pids('picam')
    for pid in pids:
        os.kill(pid, SIGKILL)

def get_pids(name):
    pids = []
    try:
        pids = map(int, check_output(["pidof", name]).split())
    except CalledProcessError as e:
        print(e)
    return pids
        
        
