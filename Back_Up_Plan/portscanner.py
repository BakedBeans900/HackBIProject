from socket import *
import sys
import time
from datetime i
mport datetime

host = ''
max_port = 2
min_port = 1

def scan_host(host, port, r_code = 1):
	try:
		s = socket(AF_INET, SOCK_STREAM)

		code = s.connect_ex((host, port))

		if code == 0:
			r_code = code
		s.close()
	except Exception as e:
		pass

	return r_code

try:
	host = input("[^] Enter Target Address: ")
except KeyboardInterrupt:
	print("\n\n[^] User Requested An Interrupt.")
	print('[^] Application Shutting Down. ')
	sys.exit(1)

hostip = gethostbyname(host)
print("[^] Host: %s IP: %s" % (host, hostip))
print("[^] Scanning Started At %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port, max_port):
	try:
		response =  scan_host(host, port)

		if response == 0:
			print("[^] Port %d: Is Open" % (port))

	except Exception as e:
		pass

stop_time = datetime.now()
total_time_duration =  stop_time - start_time
print("\n[^] Scanning Has Completed At %s ..." % (time.strftime("%H:%M:%S")))
print("[^] Scanning Lasted: %s ..." % (total_time_duration))
