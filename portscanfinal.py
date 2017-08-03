import optparse
import socket
from socket import *
from threading import *
s = Semaphore(value=1)
def a(host , port):
    try:
       con = socket()
       con.connect((host , port))
       #con.send('hai\r\n')
       #result = con.recv(100)
       print " \t\t\t\t[!!!!!]   %d / TCP OPEN PORT   [!!!!]  " % port
       #print '!!' + str(result)
       s.acquire()
    except:
        s.acquire()
        #print "!!%d / tcp port is closed " % port
    finally:
           s.release()
           con.close()
def portscan(host , ports):
    try:
       tarip = gethostbyname(host)
    except:
       print "unknown host: " + host
       return
    try:
       tarname = gethostaddrr(tarip)
       print " SCANNING HOST : " + tarname[0]
    except:
       print " SCANNING IP : " + tarip
    setdefaulttimeout(1)
    for port in ports:
        t = Thread(target=a,args=(host,int(port)))
        t.start()
def main():
    host = str(raw_input("\t\tEnter the Host:"))
    ports1 = str(raw_input("\t\tEnter the ports:"))
    ps = open(ports1)
    for x in ps.readlines():
        #ports = x.split('\n')
        ports = str(x).split(', ')
        if (host == None) | (ports == None):
               print "target port"
               exit(0)
    portscan(host,ports)
if __name__ == '__main__':
    main()

