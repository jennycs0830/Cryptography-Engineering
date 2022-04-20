# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 00:53:37 2022

@author: jenny
"""

def computeIC(ciphertext):
    chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    N=len(ciphertext)-ciphertext.count(" ")-ciphertext.count(",")
    #算出ciphetext的長度
    IC=0
    #用IC先記錄分子
    for char in chars:
        count=0
        count=ciphertext.count(char)
        char_IC=count*(count-1)
        IC+=char_IC
    denominator=N*(N-1)
    IC=IC/denominator
    return IC
f=open("messagex.txt","a")
print("cipher=")
cipher=input()
IC={4:0,5:0,6:0,7:0}
largest_IC=0
for i in range(4,8):
    #print("key length=",i)
    for j in range(1,i):
        index=0
        subcipher=''
        while index<=len(cipher):
            #print("index=",index," cipher=",cipher[index])
            subcipher+=cipher[index]
            index+=i
        IC[i]+=computeIC(subcipher)
    IC[i]=IC[i]/i
    #print("IC[",i,"]=",IC[i])
    if(IC[i]>largest_IC):
        largest_IC=IC[i]
        keyword_len=i
f.write(str(keyword_len))
#print(str(keyword_len))
f.write("\n")
f.close()