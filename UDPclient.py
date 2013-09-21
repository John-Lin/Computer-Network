#!/usr/bin/python

import socket
import sys
import random
import time
import cPickle as pickle

def main():
    host = '192.168.0.102'
    ISOTIMEFORMAT='%Y-%m-%d,%X'
    #host = socket.gethostname()
    port = 9909

    def random_msg(sec):
        time.sleep(sec)
        msg = random.random()
        return msg

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error, msg:
        print 'Failed to creat socket. Error Code : ' + str(msg[0]) + ' , Error Message :' + 'msg[1]'
        sys.exit()

    try:
        while True:
            #msg = raw_input('CLIENT >>')

            msg = random_msg(1)
            datetime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            total_sec = time.time()

            data = [datetime, total_sec, msg]

            packet = pickle.dumps(data)

            print str(msg)

            try:
                s.sendto(packet, (host, port))
            except socket.error, msg:
                print 'Error Code : ' + str(msg[0]) + 'Message' + msg[1]
                #s.close()
                sys.exit()

    except KeyboardInterrupt:
            print 'Stopped'
            #s.close()
            sys.exit()

if __name__ == '__main__':
    main()
