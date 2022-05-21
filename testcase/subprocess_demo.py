import subprocess
import sys


res = subprocess.call("ls -l",shell=True,encoding="utf8")
#print(subprocess.run("ls -l"))
print(res)