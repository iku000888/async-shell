import socket
import threading
import os
import sys

class ServerThread(threading.Thread):
   def __init__(self,conn):
      HOST = 'localhost' 
      threading.Thread.__init__(self,None, None,None, (),{},None)
      self.conn = conn 
   def run(self):
      data_str = ""
      while 1:
         data = self.conn.recv(1024)
         if not data: break
         self.conn.sendall('running ' + data)
         data_str= data
         os.system(data_str)
      self.conn.close()

HOST = 'localhost'
# Symbolic name meaning all available interfaces
PORT = int(sys.argv[1])
# Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print "started listening to port:", PORT
while 1:
   s.listen(1)
   conn, addr = s.accept()
   t = ServerThread(conn)
   t.start()




