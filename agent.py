import socket
import sys
import os
import time
import json
import threading
import psutil
import platform


def get_all_processes():
    processes = psutil.process_iter()
    for p in processes:
        process_info = p.as_dict(attrs=['pid', 'name', 'username'])
        print(process_info)

def sysinfo():
    print(platform.uname())

def send_data(data, ip, port):
  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 10000))
    sock.sendall(json.dumps(data).encode())
    sock.close()

if __name__ == '__main__':
    sysinfo()
    get_all_processes()
    while True:
        time.sleep(10)



