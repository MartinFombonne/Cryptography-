from importlib.resources import path
from Crypto.PublicKey import ECC
from Crypto import Random
from os.path import exists
from Crypto.Cipher import PKCS1_OAEP
from timeit import default_timer as timer
import ast 



def GenKey(path_keys_pub,path_keys_priv):
    key = ECC.generate(curve='P-256')
    key_priv = key.export_key(format='PEM')
    key_pub = key.public_key().export_key(format='PEM')
    print(key_pub)
    print(key_priv)
    with open(path_keys_priv, 'w') as file:
        file.write(key_priv)
    file.close()
    with open(path_keys_pub, 'w') as file:
        file.write(key_pub)
    return 

def Encryption(plaintext_file,path_keys_pub,name):
    with open(plaintext_file, 'r') as file:
        plaintext = file.read()
    file.close
    with open(path_keys_pub, 'rb') as file:
        key_pub = file.read()
    file.close

    key_pub = ECC.import_key(key_pub)
    print(key_pub)
    cypher = PKCS1_OAEP.new(key_pub)
    print('---')


    encrypted = cypher.encrypt(plaintext)
    encrypted_file_name = "Encrypted_"+name+"_File"
    with open(encrypted_file_name,'wb') as file:
        file.write(encrypted)
    file.close
    return

def Decryption(path_keys_priv,name):
    encrypted_file_name = "Encrypted_"+name+"_File"
    with open(encrypted_file_name, 'rb') as file:
        encrypted = file.read()
    file.close
    with open(path_keys_priv, 'rb') as file:
        key_priv = file.read()
    file.close
    key_priv = RSA.importKey(key_priv)
    cypher = PKCS1_OAEP.new(key_priv)
    encrypted = cypher.decrypt(encrypted)
    print(encrypted)
    decrypted_file_name = "Decrypted_"+name+"_File"
    with open(decrypted_file_name,'wb') as file:
        file.write(encrypted)
    file.close

choice=0
start=0
while choice != 1 and choice!=2:
    choice = int(input("Enter 1 for Encryption or 2 for Decryption\n"))
    if choice != 1 and choice!=2:
        input("Invalid input")
name = input("\nName of the person who originated the message you want to encrypt/decrypt : ")
file_pub = str(name) + "_Public_Key"
file_priv = str(name) + "_Private_Key"
path_keys_pub= './Keys/' + str(file_pub)
path_keys_priv= './Keys/' + str(file_priv)
if choice == 1 :
    if not (exists(path_keys_pub) and exists(path_keys_priv))  :
        GenKey(path_keys_pub,path_keys_priv)
    plaintext_file=input("\nEnter the name of the file you want to encrypt : ")
    start = timer()
    Encryption(plaintext_file,path_keys_pub,name)
else : 
    if exists(path_keys_priv):
        start = timer()
        Decryption(path_keys_priv,name)
    else : 
        print("You don't have the key to decrypt "+ name+"'s file")

if start !=0:
    end = timer()
    print("Time : "+ str(end - start))

