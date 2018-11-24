f = "Mh;y;mR1@OijQhHW6Ah=hB"
#v2 = unk_400A40 value
v2 = [8,9,15,5,11,1,3,5,13,1,14,3,5,14,7,4,193,6,6,12,15,10,12,10,2,13,8,7,3,7,1,7,5,8,12,3,4,11,14,5,1,11,3,9,4,5,6,8,12,5,3,10,15,3,14,15,4,8,10,11,15,2]
flag = ""

def r(a1):
	y=17;
	m=12;
	d=21;
	for i in range(y):
		a1 ^= y
		for j in range(m):
			a1 ^= m
			for k in range(d):
				a1 ^= d
	return a1

def sha(a1):
	return v2[r(a1)]

for i in range(len(f)):
	flag += chr(ord(f[i]) ^ sha(i+2))

print(flag)