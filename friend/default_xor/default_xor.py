encode = [0x47,0x4e,0x42,0x43,0x7e,0x59,0x58,0x57,0x56,0x43,0x5f,0x53,0x44,0x5d,0x50,0x54,0x54,0x54,0x52,0x41,0x59,0x42,0x48,0x47,0x46,0x45,0x43,0x2c,0x4f,0x63]
asd ="" 
for i in range(len(encode)):
    asd += chr(encode[i]^i+1)
print(asd)