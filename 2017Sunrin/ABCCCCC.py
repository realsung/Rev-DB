key = "AKF@|D$D$D$D$z"
flag = ""

for i in range(len(key)):
	flag += chr(ord(key[i]) ^ ord('\a'))
print flag