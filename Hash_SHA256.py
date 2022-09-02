from genericpath import exists
import hashlib


def return_hash(file_name):
    with open(file_name, 'rb') as file:
        plaintext=file.read()
        print(plaintext)
        hash=hashlib.sha256(plaintext)
        file.close()
        return hash


def Hash_function():
    file_name=input("Enter the name of the input file : ")
    hash = return_hash(file_name)
    hash_sign= file_name + "_hash"
    with open(hash_sign, 'w') as file:
        file.write(hash.hexdigest())
        file.close()

choice=0
start=0
while choice != 1 and choice!=2:
    choice = int(input("Enter 1 to generate a hash from a file or 2 to check the integritry of a file\n"))
    if choice != 1 and choice!=2:
        input("Invalid input")

def Checking():
    file_name=input("Enter the name of the input file : ")
    hash_name=file_name+ "_hash"
    if exists(file_name) and exists(hash_name):
        hash=return_hash(file_name)
        with open(hash_name, 'r') as file:
            hash2=file.read()
            file.close
        print(hash.hexdigest)
        print(hash2)
        if hash.hexdigest() == hash2:
            print("The file is intact")
        else : 
            print("The file has been modified")
    else:
        print("The file or the file's signature is not available in the current repository")

if choice == 1 :
    Hash_function()
else : 
    Checking()