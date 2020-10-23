# python3
import subprocess, os, sys
import psutil
import time
import threading
import argparse
import urllib.request
import pyautogui
import zipfile
				
def Dumper():
    p = psutil.Process(int(args.pid))
    p.suspend()
    randdump = str(time.time()) + "_ID" +  args.pid + ".dmp"
    dumpcmd = 'procdump.exe -ma ' + "\"" + args.pid + "\"" + ' -accepteula ' + randdump
    cmdblock =subprocess.Popen(dumpcmd, stdout=subprocess.PIPE)
    cmdblock.wait()
    if args.kill: p.kill()
    else: p.resume()
    return(0)  

parser = argparse.ArgumentParser(description='Dump process by PID and/or kill it')
parser.add_argument('pid', type=str, help='PID of the process')
parser.add_argument('--kill', type=bool, help='Terminate process', default=False)
args = parser.parse_args()

procUrl = 'https://download.sysinternals.com/files/Procdump.zip'
procfile = 'Procdump.zip'

try :
    urllib.request.urlretrieve(procUrl, procfile)
except :
    if not os.path.isfile(procfile):
        alertBox = pyautogui.alert("Can't download sysinternal files. Try manually.", "Dumper install error", "OK") 
        if (alertBox == 'OK'): sys.exit()

zip_ref = zipfile.ZipFile(procfile, 'r')
zip_ref.extractall()
zip_ref.close()

ownp = psutil.Process(os.getpid())
ownp.nice(psutil.HIGH_PRIORITY_CLASS)
d = threading.Thread(target=Dumper)
d.start()