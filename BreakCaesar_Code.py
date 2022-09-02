from ast import While
from pickle import TRUE
from timeit import default_timer as timer


def shift(c):
    if ord(c)!=63 and ord(c)!=46 and ord(c)!=45 and ord(c)!=32:
        c=int(ord(c))+int(k)
        if c > 90:
            c=c-26
        elif c < 65:
            c=c+26
        return chr(c)
    return c


message=list(input("Enter the cypher\n"))
start = timer()
for k in range(26):
    cypher= map(shift,message)
    print("\nFor K = "+ str(k))
    print(''.join(list(cypher)))
end = timer()
print("Time : "+ str(end - start))