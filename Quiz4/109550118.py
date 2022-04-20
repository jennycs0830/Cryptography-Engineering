# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:04:10 2022

@author: jenny
"""

train='WITHM ALICE TOWAR DNONE WITHC HARIT YFORA LLWIT\
HFIRM NESSI NTHER IGHTA SGODG IVESU STOSE ETHER\
IGHTL ETUSS TRIVE ONTOF INISH THEWO RKWEA REINT\
OBIND UPTHE NATIO NSWOU NDSTO CAREF ORHIM WHOSH\
ALLHA VEBOR NETHE BATTL EANDF ORHIS WIDOW ANDHI\
SORPH ANTOD OALLW HICHM AYACH IEVEA NDCHE RISHA\
JUSTA NDLAS TINGP EACEA MONGO URSEL VESAN DWITH\
ALLNA TIONS GREEC EANNO UNCED YESTE RDAYT HEAGR\
AGREE MENTW ITHTR UKEYE NDTHE CYPRU STHAT THEGR\
EEKAN DTURK ISHCO NTING ENTSW HICHA RETOP ARTIC\
IPATE INTHE TRIPA RTITE HEADQ UARTE RSSHA LLCOM\
PRISE RESPE CTIVE LYGRE EKOFF ICERS NONCO MMISS\
IONED OFFIC ERSAN DMENA NDTUR KISHO FFICE RSNON\
COMMI SSION EDOFF ICERS ANDME NTHEP RESID ENTAN\
DVICE PRESI DENTO FTHER EPUBL ICOFC YPRUS ACTIN\
GINAG REEME NTMAY REQUE STTHE GREEK ANDTU RKISH\
GOVER NMENT STOIN CREAS EORRE DUCET HEGRE EKAND\
TURKI SHCON TINGE NTSIT ISAGR EEDTH ATTHE SITES\
OFTHE CANTO NMENT SFORT HEGRE EKAND TURKI SHCON\
TINGE NTSPA RTICI PATIN GINTH ETRIP ARTIT EHEAD\
QUART ERSTH EIRJU RIDIC ALSTA TUSFA CILIT IESAN\
DEXEM PTION SINRE SPECT OFCUS TOMSA NDTAX ESASW\
ELLAS OTHER IMMUN ITIES ANDPR IVILE GESAN DANYO\
THERM ILITA RYAND TECHN ICALQ UESTI ONSCO NCERN\
INGTH EORGA NIZAT IONAN DOPER ATION OFTHE HEADQ\
UARTE RSMEN TIONE DABOV ESHAL LBEDE TERMI NEDBY\
ASPEC IALCO NVENT IONWH ICHSH ALLCO MEINT OFORC\
ENOTL ATERT HANTH ETREA TYOFA LLIAN CE'

train=train.replace(" ","")
dict_3={}
for i in range(len(train)-2):
    substr=train[i:i+3]
    if substr not in dict_3:
        dict_3[substr]=train.count(substr)
dict_2={}
for i in range(len(train)-1):
    substr=train[i:i+2]
    if substr not in dict_2:
        dict_2[substr]=train.count(substr)

vowel='AEIOU'
chars=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cipher='EOEYE GTRNP SECEH HETYH SNGND DDDET OCRAE RAEMH\
TECSE USIAR WKDRI RNYAR ANUEY ICNTT CEIET US'
cipher=cipher.replace(" ","")

#7*11反轉成11*7(11個一組)
standard1=11*0.4
Diff1=0
for i in range(int(len(cipher)/11)):
    substr=cipher[i*11:(i*11)+11]
    #將cipher分成11個一組
    count=0
    for char in vowel:
        count+=substr.count(char)
        #算每個substr裡有幾個母音
    difference=abs(standard1-count)
    Diff1+=difference 
    #算Diff總和

#11*7反轉成7*11(7個一組)
standard2=7*0.4
Diff2=0
for i in range(int(len(cipher)/7)):
    substr=cipher[i*7:(i*7)+7]
    count=0
    for char in vowel:
        count+=substr.count(char)
    difference=abs(standard2-count)
    Diff2+=difference

if(Diff1<Diff2):
    element=7
else:
    element=11

Cipher=['']*element
j=0
for i in cipher:
    Cipher[int(j/11)]+=i
    j+=1

ans=[0]*7#紀錄row的每個element對應到哪個column
used=[False]*7#紀錄每個column排過了沒
ans[0]=2
ans[1]=5
used[2]=True
used[5]=True

for i in range(5):
    max=0 #用來記錄最大的conditional probability
    next_index=0 #用來記錄最後要排進ans的下個column對應的column index
    for column in range(7):
        num=0 #用來記錄每個column的conditional probability
        plain=Cipher[ans[i]][0]+Cipher[ans[i+1]][0] #bigram word
        if plain in dict_2:
            base=dict_2[plain] #bigram frequency
        else:
            base=0
        for index in range(11):
            if base!=0: #確保分母不為0
                if used[column]==False: #確定column沒有被排過
                    plain+=Cipher[column][index] #trigram word
                    if plain in dict_3:
                        pf=dict_3[plain] #trigram frequency
                        num+=(pf/base) #conditional probability
                    if index!=10: 
                        plain=Cipher[ans[i]][index+1]+Cipher[ans[i+1]][index+1] #換下一row的前兩個字
                        if plain in dict_2:
                            base=dict_2[plain]
                        else:
                            base=0
        if max<num: 
            next_index=column
            max=num
    ans[i+2]=next_index #記錄下個ans
    used[next_index]=True #確保不會再排到此column

if element==7:
    index=11 #反轉後的index
else:
    index=7
ciph=['']*index
for i in range(index):
    for order in ans:
        ciph[i]+=Cipher[order][i] #將Cipher的column轉成row的形式
for i in range(index):
    for word in ciph[i]:
        print(word,end='')
    print('\n')
                    

