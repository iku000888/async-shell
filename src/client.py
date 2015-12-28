import socket
import sys
import os

HOST = 'localhost'
# The remote host
PORT = 50008
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
