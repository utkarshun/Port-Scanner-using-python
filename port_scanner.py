#!/usr/bin/python3
import socket
import sys
import time
import threading
usage="python3 port_scan.py TARGET START_PORT END_PORT"
print("-"*70)
print("Python Simple Port Scanner")
print("-"*70)
start_time=time.time()
if (len(sys.argv)!= 4):
    print(usage)
    sys.exit()
try:
    target=socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error!")
    sys.exit()
start_port=int(sys.argv[2])
end_port=int(sys.argv[3])
print("Scanning Target ",target)
def scan_port(port):
    try:
   # print("Scanning Port: ",port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        conn= s.connect_ex((target, port))
        if(not conn):
            print("Port {} is OPEN".format(port))
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
threads=[]    
for port in range(start_port, end_port+1):
    thread=threading.Thread(target=scan_port,args=(port,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
end_time=time.time()
print("Time Elapsed: ",end_time-start_time,"s")
