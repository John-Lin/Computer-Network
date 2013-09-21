#!/usr/bin/python

import socket
import sys
import time
from thread import *

def clientthread(addr, conn):
    ISOTIMEFORMAT='%Y-%m-%d,%X'

    def log(datetime, total_sec, msg):
        items = [datetime, str(total_sec), msg]
        result = ','.join(items)
        try:
            with open('log' + str(addr[0]) + '.csv', 'a') as data:
                data.writelines(result + '\n')
        except IOError as err:
            print ('File error:' + str(err))

    #conn.send('Welcome to the server. Type something and hit enter\n')
    while True:
        msg = conn.recv(1024)
        if msg == 'exit()' or not msg:
            conn.close()
            break
        datetime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
        total_sec = time.time()
        log(datetime, total_sec, msg)
        print addr[0] + ':' + str(addr[1]), '>>', msg

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    #host = '192.168.2.103' #IP of John-Win7
    port = 9909

    print 'Server started!'
    print 'Waiting for clients...'

    try:
        s.bind((host, port))
    except socket.error, msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    
    #Start listening on socket
    s.listen(10)

    try:
        while True:
            conn, addr = s.accept()
            print 'Got connect from', addr[0] + ':' + str(addr[1])
            start_new_thread(clientthread, (addr, conn, ))
    except KeyboardInterrupt:
        print 'Server stoped'
        s.close()
        sys.exit()

if __name__ == '__main__':
    main()
