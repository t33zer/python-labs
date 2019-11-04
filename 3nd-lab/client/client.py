#!/usr/bin/python3

import psutil
import json

# returns dict of total, used and available memory
# used + available != total, coz linux is weird
def get_memory_info():
    memory = psutil.virtual_memory()
    delimeter = 1024.0 ** 3
    memory_info = {
            'total' : str(round(memory.total / delimeter, 1))+"Gb",
            'used' : str(round(memory.used / delimeter, 1))+"Gb",
            'available' : str(round(memory.available / delimeter, 1))+"Gb"
            }
    print(memory_info)
    return memory_info


def get_processor_info():
    processor = {
            'processor_load' : str(psutil.cpu_percent())
            }
    return processor


def get_disk_freespace_info():
    disk = psutil.disk_usage() 
    free = {'disk free space' : disk.free / (1024.0 ** 3)}
    return free

def get_procs_count():
    quantity = 0
    for _ in psutil.process_iter():
        quantity += 1
    return { 'processes' : quantity }
        

def get_users_list():
    users = psutil.users()
    users_list = []
    for entry in users:
        if entry[0] not in users_list:
            users_list.append(entry[0])
    return { 'users' : users_list}


users = get_users_list()
with open("./users.txt", "a+") as f:
    f.write(json.dumps(users))
    
