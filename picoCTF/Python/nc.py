from pwn import *

r = remote('jupiter.challenges.picoctf.org', 25103)

while True:
	try:
		print(r.recv().decode())
	except EOFError:
		break
