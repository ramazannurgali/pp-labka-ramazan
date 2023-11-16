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

specified_path = 'C:\\Users\\ramazan\\Desktop\\pp2'

LD(specified_path)

LF(specified_path)

LAC(specified_path)

 

 
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
CPA(path_to_check)
    
    
#3
def CPE(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{path}' does not exist.")

path_to_check = r"C:\Users\ramazan\Desktop\pp2"

CPE(path_to_check)

#4
file_path_to_count = r'C:\Users\Daniyar\Desktop\Ответики.txt'

with open(file_path_to_count, 'r', encoding="utf-8") as file:
    line_count = sum(1 for line in file)

print(f"The number of lines in the file '{file_path_to_count}' is: {line_count}")

#5
def write_list_to_file(file_path, my_list):
      with open(file_path, 'w') as file:
        for item in my_list:
                file.write(str(item) + '\n')
        print(file_path)
    


my_list = [1, 2, 3, 4, 5]
file_path = 'output.txt'

write_list_to_file(file_path, my_list)

#6
for letters in string.ascii_uppercase:
    file_name = f'{letters}.txt'
    with open(file_name, 'w'):
        pass

#7
def copy_path2_in_path1(path1,path2):
    with open(path2,'r') as path2:
        file = path2.read()
        
    with open(path1, 'w') as res_file:
        res_file.write(file)
    print(res_file)
path1 = "path.txt"
path2 = "path2.txt"
copy_path2_in_path1(path1,path2)

#8
def delete_file(file_to_delete):
    if(os.path.exists(file_to_delete)):
        if(os.access(file_to_delete, os.W_OK)):
            os.remove(file_to_delete)
        else:
            print("Has no acces to file")
    else:
        print("File does not exist")

file_to_delete = "text.txt"
delete_file(file_to_delete)
