import socket
import sys
import os
from os.path import expanduser
home = expanduser("~")

HOST = 'localhost'
# The remote host
PORT = open(home+'/.async_port', 'r').readline()
PORT = int(PORT)
# The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
try:
    s.sendall(sys.argv[1])
    data = s.recv(1024)
    print repr(data)
except IndexError:
    raise IndexError("expected a string as the only operand.")
finally:
    s.close()
