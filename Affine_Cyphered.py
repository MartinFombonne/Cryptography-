def affine_enc(c):
    if ord(c)!=63 and ord(c)!=46 and ord(c)!=45 and ord(c)!=32:
        c=int(a)*ord(c)+int(b) 
        while c > 90 or c < 65:
            if c > 90:
                c=c-26
            elif c < 65:
                c=c+26
        return chr(c)
        
    return c

def affine_dec(c):
    if ord(c)!=63 and ord(c)!=46 and ord(c)!=45 and ord(c)!=32:
        c=(pow(a, -1, 26))*(int(ord(c))-int(b)) % 26
        while c > 90 or c < 65:
            if c > 90:
                c=c-26
            elif c < 65:
                c=c+26
        return chr(c)
    return c

choice=0
a = int(input("Enter a value : \n"))
b = int(input("Enter b value : \n"))


while choice != 1 and choice!=2:
    choice = int(input("Enter 1 for Encryption or 2 for Decryption\n"))
    if choice != 1 and choice!=2:
        input("Invalid input")

if choice == 1 :
    message=list(input("Enter the message for encryption\n"))
    print(message)
    cypher=map(affine_enc,message)
elif choice == 2 : 
    message=list(input("Enter the message for decryption\n"))
    cypher= map(affine_dec,message)
print(''.join(list(cypher)))

