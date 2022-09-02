from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import re
from os import urandom
from Crypto.Util.Padding import pad, unpad
import base64
import random
import string
import ast 
from timeit import default_timer as timer

def aes_enc() : 
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    message = input("Enter your secret message : \n")
    start = timer()
    encrypted = cipher.encrypt(pad(message.encode("utf-8"),16))
    print("\nCypher : ")
    print(encrypted)
    print("\nSecret key :")
    print(key)
    return start 

def aes_dec():
    key=input("Enter the  key : \n")
    key = ast.literal_eval("b'" + key + "'")
    print(key)
    encrypted=input("Enter the  cypher : \n")
    start = timer()
    encrypted = ast.literal_eval("b'" + encrypted + "'")
    print(encrypted)
    decipher = AES.new(key, AES.MODE_ECB)
    message = decipher.decrypt(encrypted)
    print((unpad(message,16)).decode("utf-8"))
    return start 
   
choice=0
while choice != 1 and choice!=2:
    choice = int(input("Enter 1 for Encryption or 2 for Decryption\n"))
    if choice != 1 and choice!=2:
        input("Invalid input")
if choice == 1 :
    start=aes_enc()
else : 
    start=aes_dec()
end = timer()
print("Time : "+ str(end - start))

    

    
