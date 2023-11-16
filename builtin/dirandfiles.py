import os
import string

#1
def LD(path):
    print("Directories:")
    for DR in os.listdir(path):
        if os.path.isdir(os.path.join(path, DR)):
            print(DR)

def LF(path):
    print("\nFiles:")
    for FL in os.listdir(path):
        if os.path.isfile(os.path.join(path, FL)):
            print(FL)

def LAC(path):
    print("\nAll Directories and Files:")
    for IM in os.listdir(path):
        IP = os.path.join(path, IM)
        print(IM, "(Directory)" if os.path.isdir(IP) else "(File)")

SP = 'C:\\Users\\ramazan\\Desktop\\pp2'

LD(SP)

LF(SP)

LAC(SP)

 

 
#2
def CPA(path):
    # Check if the path exists
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    # Check readability
    if os.access(path, os.R_OK):
        print(f"Read access to '{path}' is allowed.")
    else:
        print(f"No read access to '{path}'.")

    # Check writability
    if os.access(path, os.W_OK):
        print(f"Write access to '{path}' is allowed.")
    else:
        print(f"No write access to '{path}'.")

    # Check executability
    if os.access(path, os.X_OK):
        print(f"Execute access to '{path}' is allowed.")
    else:
        print(f"No execute access to '{path}'.")


PTC = input("Enter the path: ")
CPA(PTC)
    
    
#3
def CPE(P):
    if os.path.exists(P):
        print(f"The path '{P}' exists.")
        FN = os.path.basename(P)
        D = os.path.dirname(P)
        print(f"filename: {FN}")
        print(f"directory: {D}")
    else:
        print(f"The path '{P}' does not exist.")

PTC = r"C:\Users\ramazan\Desktop\pp2"

CPE(PTC)

#4
FPTC = r'C:\Users\ramazan\Desktop\Ответики.txt'

with open(FPTC, 'r', encoding="utf-8") as file:
    LC = sum(1 for line in file)

print(f"The number of lines in the file '{FPTC}' is: {LC}")

#5
def WLTF(FP, ML):
      with open(FP, 'w') as file:
        for item in ML:
                file.write(str(item) + '\n')
        print(FP)
    


ML = [1, 2, 3, 4, 5]
FP = 'output.txt'

WLTF(FP, ML)

#6
for letters in string.ascii_uppercase:
    FN = f'{letters}.txt'
    with open(FN, 'w'):
        pass

#7
def CPIP(P1,P2):
    with open(P2,'r') as P2:
        F = P2.read()
        
    with open(P1, 'w') as RF:
        RF.write(file)
    print(RF)
P1 = "path.txt"
P2 = "path2.txt"
CPIP(P1,P2)

#8
def DF(FTD):
    if(os.path.exists(FTD)):
        if(os.access(FTD, os.W_OK)):
            os.remove(FTD)
        else:
            print("Has no acces to file")
    else:
        print("File does not exist")

FTD = "text.txt"
DF(FTD)
