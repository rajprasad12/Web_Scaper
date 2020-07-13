import subprocess 
import os
import time
url= input('enter the website name-->')
cmd='python sublist3r.py -d {} -o list.txt'.format(url)
subprocess.call(cmd) # it prompt the cmd to execute the command
os.system("list.txt") # it will open the list.txt file


