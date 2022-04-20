import hashlib
import binascii

def hashMD5(input):
    hashVal=hashlib.md5(bytes.fromhex(input))
    return hashVal.hexdigest()[:4]

    

input='c606196ea460a3a53ac3e81c614b990b'
hashvalue=hashMD5(input)


val=28791503795108462015798155635410261561612

while(1):
    val=hex(val)[2:]
    if hashvalue==hashMD5(val):
        print(hashvalue,val)
        break
    
    val=int(val,16)
    val+=1



