#!/usr/bin/python3
import socket
import sys
import time
import threading

# Usage and Introduction
usage = "python3 port_scan.py TARGET START_PORT END_PORT"
print("-" * 70)
print("Python Simple Port Scanner")
print("-" * 70)

# Track Start Time
start_time = time.time()

# Argument Validation
if len(sys.argv) != 4:
    print(usage)
    sys.exit()

# Resolve Target Hostname
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error!")
    sys.exit()

# Parse Ports
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

# Print Target Information
print("Scanning Target", target)

# Port Scanning Function
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        conn = s.connect_ex((target, port))
        if conn == 0:  # Port is open
            print(f"Port {port} is OPEN")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Start Threads
threads = []
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

# Wait for All Threads to Complete
for thread in threads:
    thread.join()

# Calculate and Print Time Elapsed
end_time = time.time()
print("Time Elapsed:", round(end_time - start_time, 2), "s")
