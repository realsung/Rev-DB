num = [99,111,109,109,97,110,100,58,99,114,101,97,116,101,95,102,108,97,103]
char = ""
for i in range(len(num)):
    char += chr(num[i])
print(char)