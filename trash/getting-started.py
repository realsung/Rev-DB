a = [102,108,97,103,123,119,101,108,99,111,109,101,95,116,111,95,108,101,118,101,108,95,49,125]
flag = ""
for i in range(len(a)):
	flag += chr(a[i])
print(flag)