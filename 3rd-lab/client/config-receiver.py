import socket
from logging import basicConfig, error, warning
import configparser


def get_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(("8.8.8.8", 53))
    except:
        return 'No internet connection, can\'t figure out ip'
    ip = sock.getsockname()[0]
    sock.close()
    return ip

def receive_info():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = get_ip()
    if ip.startswith("No internet"):
        exit("Failed to get local ip!")
    print("ip: ", ip)
    #in case fail with port reusing
#    for port in range(8080, 8088):
#        try:
#            sock.bind((ip, port))
#            print(f"listening at {ip} {port}") 
#            break
#        except:
#            continue
    sock.bind((ip, 5001))
    sock.listen(1)
    conn, addr = sock.accept()
    with open("config.ini", "wb") as f:
        pass
    data = bytes()
    # reading data from socket
    while True:
        part = conn.recv(4096)
        if not part:
            break
        data += part
    config = configparser.ConfigParser()
    data_str = data.decode().split("\n")
    if data_str[-1] == '':
        data_str.pop()
    #needed for configparser
    data_dict = dict()
    for entry in data_str :
        #check for empty value 
        data_splitted = False if entry.split("=")[-1].isspace() else entry.split("=")
        if not data_splitted:
            continue
        data_dict[data_splitted[0]] = data_splitted[1]
    print(data_dict)
    config['default'] = data_dict
    with open("config.ini", "w") as cfgfile:
        config.write(cfgfile)
    sock.close()


if __name__ == "__main__":
    while True:
        receive_info()
