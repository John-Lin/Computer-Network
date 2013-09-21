#!/usr/bin/python

import socket
import sys
import time
import cPickle as pickle

def main():
    #ISOTIMEFORMAT='%Y-%m-%d,%X'
    host = socket.gethostname()
    #host = '192.168.2.103' #IP of John-Win7
    port = 9909

    def log(datetime, total_sec, msg):
        items = [datetime, str(total_sec), str(msg)]
        result = ','.join(items)
        try:
            with open('log' + str(addr[0]) + '.csv', 'a') as data:
                data.writelines(result + '\n')
        except IOError as err:
            print ('File error:' + str(err))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print 'Server started!'
    print 'Waiting for clients...'

    try:
        s.bind((host, port))
    except socket.error, msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    try:
        while True:
            packet, addr = s.recvfrom(1024)

            data = pickle.loads(packet)

            if data[2] == 'exit()' or not data:
                break

            datetime = data[0]
            total_sec = data[1]
            value = data[2]

            log(datetime, total_sec, value)

            print addr[0] + ':' + str(addr[1]), '>>', value

            #datetime = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            #total_sec = time.time()

        s.close()

    except KeyboardInterrupt:
        print 'Server stoped'
        s.close()
        sys.exit()

if __name__ == '__main__':
    main()
