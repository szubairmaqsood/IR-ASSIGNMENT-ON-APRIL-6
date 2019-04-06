import urllib
from bs4 import BeautifulSoup
import nltk
from nltk.stem import PorterStemmer
import string
from SingleObjectInFile import SingleRecode
import os
import re

def runer(string): 
    regex = re.compile('[+@_!—›→><#-$%^&*♥★.()<>?•/\|€…}{~:]') 
    if(regex.search(string) == None): 
        return True     
    else: 
        return False

def PreProcessing(text):
    stopWordFile = open('stoplist.txt')
    StopWordsList = stopWordFile.read().splitlines()
    porter = PorterStemmer()  # Object  to do stemming
    List = nltk.word_tokenize(text)
    result=list()
    for i in range(len(List)):
        if List[i] in StopWordsList:  # if a token is in stop word list of only one character and in punction list ignore it
         zubi =0
        else:
         if runer(List[i])==True:
            result.append(porter.stem(List[i]))
    return result

def getFromFile(doc_id): #function to get directory from docID
    f=open('docinfo.txt','r')
    for line in f:
        for word in line.split():
            if doc_id in word:
                d=word.split(',')
                print(d[1])

    f.close()

def searcher(word):   #func to find docIDs in line
    #print(word) print posting list for testing
    for i in range(len(word)):
       if word[i]=='D' and word[i+1]=='o' and word[i+2]=='c':
           j=i+3
           temp=''
           while word[j]!=',':
                temp=temp+str(word[j])
                j=j+1
           getFromFile('Doc'+temp+',')


print('Please enter the query')
query=PreProcessing(input())
print('Finalized Query Words: ')
for i in range (len(query)):
    print(query[i])

f=open('inverted_index.txt','r',encoding='utf-8')
found=False
for line in f:
   for word in line.split():
        for i in range (len(query)):
           if word.find(query[i])>=0: #found in inverted index
             found=True
             print('Term: '+query[i])
             searcher(word)
f.close()
if found==False:
    print('Sorry.No Such Terms Found')






















