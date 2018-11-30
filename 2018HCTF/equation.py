from z3 import *

s = Solver()

a1 = [Int("a1[%d]"%(i)) for i in range(0,20)]

s.add(a1[15] + a1[4] == 10)
s.add(a1[1] * a1[18] == 2)
s.add(a1[17] - a1[0] == 4)
s.add(a1[5] - a1[17] == -1)
s.add(a1[15] - a1[1] == 5)
s.add(a1[1] * a1[10] == 18)
s.add(a1[8] + a1[13] == 14)
s.add(a1[18] * a1[8] == 5)
s.add(a1[4] * a1[11] == 0)
s.add(a1[8] + a1[9] == 12)
s.add(a1[12] - a1[19] == 1)
s.add(a1[9] % a1[17] == 7)
s.add(a1[14] * a1[16] == 40)
s.add(a1[7] - a1[4] == 1)
s.add(a1[6] + a1[0] == 6)
s.add(a1[2] - a1[16] == 0)
s.add(a1[4] - a1[6] == 1)
s.add(a1[0] % a1[5] == 4)
s.add(a1[5] * a1[11] == 0)
s.add(a1[10] % a1[15] == 2)
s.add(a1[11] + a1[3] == 9)
s.add(a1[14] - a1[13] == -4)
s.add(a1[18] + a1[19] == 4)
print s.check()
print s.model()

#Flag is 42893724579049578813