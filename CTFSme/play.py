tb = "X\\CZ[ZGR^XFCFXFCF"
flag = ""
for i in range(len(tb)):
	flag += chr(ord(tb[i]) ^ 0x33)
print(flag)