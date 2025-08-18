# 
#* this file will help with getting the snap package name and revision number 
# 
#* provide the output of 
#! snap list --all | grep disabled 
#* to the terminal after running the program 
#* you will find a bash script to remove all the disabled snap packages


import re
import os

lines = os.system("snap list --all | grep disabled")
with open("removeSnapPackage.sh", "w") as f:
    f.write("#! /bin/bash\n\n")

def format_cmd(name, rev):
    return f"sudo snap remove --purge {name} --revision {rev}\n"

def extract(line):
    pattern = r"(\S+)\s+\S+\s+(\d+)\s+.*disabled"
    match = re.match(pattern, line)
    if match:
        return match.groups()

def output(cmd):
    with open("removeSnapPackage.sh", "a") as f:
        f.write(cmd)

def inp():
    while True:
        try:
            line = input()
        except EOFError:
            break

        result = extract(line)
        if result:
            name, rev = result
            cmd = format_cmd(name, rev)
            output(cmd)
    
if __name__ == "__main__":
    inp()
