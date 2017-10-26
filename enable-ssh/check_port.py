#!/usr/bin/python
import socket
import sys
import telnetlib
import re

"""
Script checks CISCO device for enabled ssh with version 2
"""

if len(sys.argv) != 3:
    print(str('\nWrong argument list: ' + sys.argv[0] + ' ip_addr port\n'))
    sys.exit(1)

host = sys.argv[1]
port = sys.argv[2]

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.settimeout(2)

if skt.connect_ex((str(host), int(port))) == 0:
    tn = telnetlib.Telnet(host, port, timeout=2)
    data = tn.read_until(b"\n")
    data = data.decode("utf-8").strip()  # to string
    if re.match(r"ssh-2\.", data, flags=re.IGNORECASE):
        print("ok")
        sys.exit(0)
    else:
        print('fail')
        sys.exit(1)
else:
    print('fail')
    sys.exit(1)