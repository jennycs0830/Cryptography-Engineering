# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 01:17:49 2022

@author: jenny
"""
Freq=[0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
chars=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def countFreq(cipher):
    chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    CipherFreq=[]
    for i in range(26):
        CipherFreq.append(0)
    #print(CipherFreq)
    N=len(cipher)
    index=0
    for char in chars:
        count=0
        count=cipher.count(char)
        CipherFreq[index]=count/N
        index+=1
    #print("CipherFreq=",CipherFreq)
    return CipherFreq

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
print("ciphertext=")
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
keyword=''
for i in range(keyword_len):
    index=i
    subcipher=''
    while index<=(len(cipher)-1):
        #print("index=",index)
        subcipher+=cipher[index]
        index+=keyword_len
    #print(i,"word:",subcipher)
    largest=0
    for shift in range(26):
        match=0
        CipherFreq=countFreq(subcipher)
        #print("CipherFreq=",CipherFreq)
        for j in range(26):
            match+=Freq[j]*CipherFreq[(j+shift)%26]
        #print("shift=",shift," match=",match)
        if(largest<match):
            largest=match
            #print("largest=",largest)
            index=shift
            #print("index=",index)
    keyword+=chars[index]
f.write(str(keyword))
#print(str(keyword))
f.write("\n")
f.close()