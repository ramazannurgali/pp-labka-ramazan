import math
import time
#1
L = [int (i) for i in input().split()]
P = math.P(L)
print(P)
 
#2
Sos = str(input())
cUp = 0
clow = 0

for i in Sos:
    if(i.isupper()):
        cUp=cUp+1
    else:
        clow=clow+1
print(cUp, clow) 

#3
Sos = str(input())
r = reversed(Sos)
rever = ''
for i in r:
    rever=rever+i
    
if(Sos == rever):
    print("isPalindrome")
else:
    print("isNoPalindrome")
     
#4
N = int(input("number:"))
MS = int(input("outputAfetTime:"))
res = float(math.sqrt(N))
time.sleep(MS/1000)
print("Square root of ", N, " after ", MS, " miliseconds is ", res )
         
#5
MT = {True,True,True,False}
result = all(MT)
if(result):
    print("All elements is True")
else:
