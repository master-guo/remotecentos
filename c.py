#!/usr/bin/python3
#coding:utf-8
import re,random
sentence = input('input a sentence: ')
listSentence = re.split('\s+',sentence)
setSentence = set(listSentence)
lastClearSentence = list(setSentence)
for i in range(len(setSentence)):
    print('%s : %d'%((lastClearSentence[i]),listSentence.count(lastClearSentence[i])))

m = 1000
blankList = []
while m >0 :
    blankList.append(random.randint(20,100))
    m-=1
blankList.sort()
blankSet = set(blankList)
lastBlankList = list(blankSet)
for n in range(len(blankSet)):
    print('%s : %d'%(lastBlankList[n],blankList.count(lastBlankList[n])))