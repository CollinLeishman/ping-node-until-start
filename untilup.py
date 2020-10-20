#!/usr/bin/python3
import os
import subprocess
import time
print("Pings a host until it is up.")
ip = input("Hostname or IP to ping:\n>")
while True:
    with open(os.devnull, 'w') as devnull:
        try:
            subprocess.check_call(
                ['ping', '-c', '3', ip],
                stdout=devnull,  # suppress output
                stderr=devnull
            )
            is_up = True
        except subprocess.CalledProcessError:
            is_up = False
    if is_up == True:
        print("It is up")
        break
    else:
        #time.sleep(3)
        print("Still down. Trying again")
        continue
