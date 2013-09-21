#!/usr/bin/python

import socket
import sys
import random
import time

def main():
    #host = '140.138.178.209'
    host = '192.168.0.102'
    port = 9909

    def random_msg(sec):
        time.sleep(sec)
        msg = random.random()
        return msg

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to creat socket. Error Code : ' + str(msg[0]) + ' , Error Message :' + 'msg[1]'
        sys.exit()

    try:
        #remote_ip = socket.gethostname()
        remote_ip = '192.168.0.102'
    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()
    
    try:
        s.connect((remote_ip, port))
        print 'Connected to ',remote_ip, port
    except:
        print 'Unable to connect'
        sys.exit()

    try:
        while True:
            #msg = raw_input('CLIENT >>')
            msg = random_msg(1)
            print str(msg)

            try:
                s.send(str(msg))
            except socket.error:
                print 'Send faild'
                s.close()
                sys.exit()

            if msg == 'exit()':
                s.close()
                break
    except KeyboardInterrupt:
            print 'Stopped'
            s.close()
            sys.exit()

if __name__ == '__main__':
    main()