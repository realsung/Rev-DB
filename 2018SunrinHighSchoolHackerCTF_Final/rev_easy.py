enc = "51564e534f497f473e78396a51573c7f4d4362217426277867"
bb = enc.decode("hex")
flag = ""
for i in range(len(bb)):
	flag += chr(ord(bb[i])^2^i)
print flag
