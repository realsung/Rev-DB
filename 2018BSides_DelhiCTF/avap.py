key = 7
index = [0x61,0x6B,0x66,0x60,0x7C,0x33,0x74,0x58,0x62,0x33,0x32,0x7E,0x58,0x33,0x74,0x58,0x36,0x73,0x58,0x60,0x34,0x73,0x74,0x7A]
flag = ""
for j in range(len(index)):
	flag += chr(index[j] ^ key)
print flag