#!/usr/bin/python3

import psutil
import json
import requests

# returns dict of total, used and available memory
# used + available != total, coz linux is weird
def get_memory_info():
    memory = psutil.virtual_memory()
    delimeter = 1024.0 ** 3
    memory_info = {
            'total memory' : str(round(memory.total / delimeter, 1))+"Gb",
            'memory used' : str(round(memory.used / delimeter, 1))+"Gb",
            'available memory' : str(round(memory.available / delimeter, 1))+"Gb"
            }
    return memory_info


def get_processor_info():
    processor = {
            'processor_load' : (psutil.cpu_percent())
            }
    print(processor)
    return processor


def get_disk_freespace_info():
    disk = psutil.disk_usage("/") 
    free = {'disk free space' : disk.free / (1024.0 ** 3)}
    return free

def get_procs_count():
    quantity = 0
    for _ in psutil.process_iter():
        quantity += 1
    return { 'processes' : quantity }
        

def get_users_list():
    users = psutil.users()
    users_string = str()
    for entry in users:
        if " " + entry[0] + " " not in users_string:
            # users_list.append(entry[0])
            users_string += f"{entry[0]} "
    return { 'users' : users_string}


#users = get_users_list()
#with open("./users.txt", "a+") as f:
#    f.write(json.dumps(users))
def get_all_info():
    memory_info = get_memory_info()
    cpu_info = get_processor_info()
    disk_space = get_disk_freespace_info()
    procs_count = get_procs_count()
    user_list = get_users_list()

    data = {}
    data.update(memory_info)
    data.update(cpu_info)
    data.update(disk_space)
    data.update(procs_count)
    data.update(user_list)
    return data

# data of type dict
def send_data(host='localhost', port=5000, data={}):
    req = requests.post(f"http://{host}:{port}/api/data", json=data)
    if req.status_code != 200:
        return False
    return True
    
    
if __name__ == "__main__":
    info_dict = get_all_info()
    send_data(data=info_dict)
