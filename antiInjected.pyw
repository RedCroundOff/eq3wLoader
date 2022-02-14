import listdlls
from time import sleep as time_sleep
from os import system as cmd_run

def scan():
    last_detect = None
    detect = None
    while True:
        try:
            detect = listdlls.listdll(process, arc='x86')[2]
        except BaseException:
            break
        if last_detect is not None and not detect == last_detect:
            cmd_run(f'taskkill /f /im "{process}"')
            break
        else:
            last_detect = detect
        time_sleep(1)

process = "eq3wLoader.exe"
if process:
    try:
        pid, cmdline = listdlls.listdll(process, arc='x86')[:2]
    except BaseException:
        exit()
    scan()