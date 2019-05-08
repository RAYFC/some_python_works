#collaborators: Ruifeng Chen #1473869 Hao Liu #1475938

import re
import sys
alphabet='abcdefghijklmnopqrstuvwxyz'

def checkword(regex):
    reslist=[]
    wordFile=open('wordlist.txt')
    for line in wordFile:
        if re.match(regex,line[:-1]):
            reslist.append(line[:-1])
        if len(line[:-1]) % 2==1:
            if re.match(regex,line[:-1]+'.'):
                reslist.append(line[:-1])
    return reslist
def bigramFreq(text):
    biCount={}
    for i in range(len(text)-2):
        bigram=text[i]+text[i+1]
        biCount[bigram] = biCount.get(bigram,0)+1
    return biCount
def topBigram(text):
    text=text.lower()
    nonletters=removeMatches(text,alphabet)
    nonletters=removeDupes(nonletters)
    text=removeMatches(text,nonletters)
    d=bigramFreq(text)
    l=list(d.items())
    l.sort(key=getFreq,reverse=True)
    return l
def getFreq(item):
    return item[1]
def removeMatches(mystr,removestr):
    newstr=''
    for ch in mystr:
        if ch not in removestr:
            newstr+=ch
    return newstr
def removeDupes(mystr):
    newstr=''
    for ch in mystr:
        if ch not in newstr:
            newstr+=ch
    return newstr
def getplayfair(Filename):
    string=open(Filename,'r').read().lower()
    return string
def getthecode(text):
    code=[]
    for i in range(len(text)):
        if i % 2 == 0:
            m=text[i]+text[i+1]
            code.append(m)
    return code
def checkthecode(codes,Bi,n):
    string=''
    keys=[]
    for i in range(n):
        keys.append(Bi[i][0])
    for code in codes:
        if code in keys:
            string+=code
            
        else:string+='..'
    return string,keys
def changethestring(codes,dic,n,Bi):
    newstr=''
    newdic=[]
    for i in range(n):
        newdic.append(dic[i][0])
    for i in range(len(codes)):
        if i % 2 ==0:
            m=codes[i]+codes[i+1]
            if m !='..':
                index=Bi.index(m)
                newstr+=newdic[index]
            else:
                newstr+='..'
    return newstr       
def main():
    Filename=sys.argv[1]
    word=sys.argv[2]
    n=3
    if len(sys.argv)==4:
        n=sys.argv[3]
    n=int(n)
    word=word.lower()
    text=getplayfair(Filename)
    Bi=topBigram(text)
    codes=getthecode(word)
    codes,lst=checkthecode(codes,Bi,n)
    dictname='wells.txt'
    dictionary=open(dictname,'r').read()
    dic=topBigram(dictionary)
    newcode=changethestring(codes,dic,n,lst)
    print(newcode)
    print(checkword('^'+newcode+'$'))
main()
    
    
