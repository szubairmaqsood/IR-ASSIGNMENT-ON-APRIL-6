import urllib
from bs4 import BeautifulSoup
import nltk
from nltk.stem import PorterStemmer
import string
from SingleObjectInFile import SingleRecode
import os
import html5lib
'''
def visible(element):
    if element.name in ['style', 'script']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

# Get all elments in body and return it
def GetText(filePath):
    data=''
    file=open(filePath)
    soup = bs.BeautifulSoup(file,'html.parser')
    elements=list(soup.find('body').children)
    for x in elements:
        #if x.name!='script':
          # data=data+x.get_text()
      print(x.text)
    return data

'''

def PreProcessing(directory,unique):
    Doc_Mapping=open('docinfo.txt', "a",encoding="utf-8")  #docinfo.txt file opening
    zubi = 0  # a verible that do b=nothing but used as nessity
    punc = string.punctuation  # string containling only punction characters
    print('Punction List')
    print(punc)
    StopWordsList = []  # LIST TO COntain stop words list
    List = []  # All terms read from a file
    CleanDataList = []  # Final clean result

    #--------------This is added to make index--------------------
    thisdict = {}  # dictionary
    #-------------------------------------------------------------
    porter = PorterStemmer()  # Object  to do stemming

    stopWordFile = open('stoplist.txt')
    StopWordsList = stopWordFile.read().splitlines()

    #Loop through all files
    for filename in os.listdir(directory):
        List=[]
        CleanDataList=[]
        #print('File name  ::'+filename)

        html=''
        html = open(directory+filename,encoding="utf-8",errors='ignore').read()


        soup = BeautifulSoup(html, 'html5lib')       #"html5lib  'html.parser'

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        if not soup.find('body'):
            print("didn't find body")
        else:
           text = soup.find('body').get_text()
           # break into lines and remove leading and trailing space on each
           lines = (line.strip() for line in text.splitlines())
           # break multi-headlines into a line each
           chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
           # drop blank lines
           text = '\n'.join(chunk for chunk in chunks if chunk)
            # Making our text to lower case
           text = text.lower()
            # Tokenize text
           List = nltk.word_tokenize(text)
          # print('Terms after tokenization ')
           #print(List)
           #print('Stop Word List ')
           #print(StopWordsList)
           for i in range(len(List)):
             if List[i] in StopWordsList or List[i] in punc:  # if a token is in stop word list of only one character and in punction list ignore it
              zubi =0
             else:
               if ((len(List[i])) < 3):  # if a string length is less than 3 than ignore it as it usually does not give any meaning
                 zubi = 0
               else:
                 CleanDataList.append(porter.stem(List[i]))  # else add term to clean data after doing stemming

           #print('\n\n\nClean DATA AFTER STEMMING AND LOWER CASE AND MOST OF PUNCTION REMOVAL ')
           #print(CleanDataList)
           #-------------------------------------------Lines added for each iteration of clean list so for each documant

           index = 0
           #assinging  unique id and writing to file
           DOCID='Doc'+str(unique)
           Doc_Mapping.write(DOCID)
           Doc_Mapping.write(',')
           Doc_Mapping.write(directory+filename)
           Doc_Mapping.write('\n')
           for term in CleanDataList:        #Get through terms of current file
               key = term                    #Current term will be key
               if key not in thisdict:       #if key is not already present in dictionary
                   thisdict[key] = SingleRecode(term)  # Documant frequnacy on this line is zero and a new object is created
                   # UPDATED DOCUMANT FREQUANCY
                   thisdict[key].IncreaseDocumantFrequnacy(DOCID)  # update this line to id of current documant so in this case set to 1
                   thisdict[key].addDocumantID(DOCID)  # added documant ID

                   # update last documant id and term frequancy to +1
                   thisdict[key].updateLastDocumantID(DOCID)
                   thisdict[key].IncreaseTermFrequnacy()

                   # added position
                   thisdict[key].addPosition(index)   #postion in current index

               else:  # if bucket is already present
                   # No no need to add new object
                   # UPDATED DOCUMANT FREQUANCY
                   thisdict[key].IncreaseDocumantFrequnacy(DOCID)  # update this line to id of current documant so in this case set to 1
                   thisdict[key].addDocumantID(DOCID)  # added documant ID

                   # update last documant id and term frequancy to 1
                   thisdict[key].updateLastDocumantID(DOCID)  # if a new documant it will be checked in class function
                   thisdict[key].IncreaseTermFrequnacy()      #term frequnacy will be added

                   # added position
                   thisdict[key].addPosition(index)          #position will be added
               index = index + 1                             #go to next word in clean data list
               # --------------------------------------------------------------------------------
           del List
           del CleanDataList
           unique=unique+1 #increasing unique docID

    #Write after a whole directory is fully traversed
    KeysOFTerms = thisdict.keys()
    Doc_Mapping.close()

    IndexWriteFileName=''
    # checking which directory passed from main to decide output file name

    if directory=='corpus1/1/':          #directory is argumant name to preprocessing function
       IndexWriteFileName='index_1.txt'
    elif directory=='corpus1/2/':
        IndexWriteFileName = 'index_2.txt'
    elif directory=='corpus1/3/':
        IndexWriteFileName = 'index_3.txt'

    f = open(IndexWriteFileName, "w",encoding="utf-8")
    for x in sorted(KeysOFTerms):
     for i in thisdict[x].getList():
      #f.write(str(i))
      #f.write(',')
     #f.write('\n')
       f.write((str(i)))
       f.write(',')
     f.write('\n')

    f.close()
    return unique
















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

def PreProcessing(directory,unique):
    Doc_Mapping=open('docinfo.txt', "a",encoding="utf-8")  #docinfo.txt file opening
    zubi = 0  # a verible that do b=nothing but used as nessity
    punc = string.punctuation  # string containling only punction characters
    print('Punction List')
    print(punc)
    StopWordsList = []  # LIST TO COntain stop words list
    List = []  # All terms read from a file
    CleanDataList = []  # Final clean result

    #--------------This is added to make index--------------------
    thisdict = {}  # dictionary
    #-------------------------------------------------------------
    porter = PorterStemmer()  # Object  to do stemming

    stopWordFile = open('stoplist.txt')
    StopWordsList = stopWordFile.read().splitlines()

    #Loop through all files
    for filename in os.listdir(directory):
        List=[]
        CleanDataList=[]
        #print('File name  ::'+filename)
        html=''
        html = open(directory+filename,errors='ignore').read()
        soup = BeautifulSoup(html, 'html.parser')
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        if not soup.find('body'):
            print("didn't find body")
        else:
           text = soup.find('body').get_text()
           # break into lines and remove leading and trailing space on each
           lines = (line.strip() for line in text.splitlines())
           # break multi-headlines into a line each
           chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
           # drop blank lines
           text = '\n'.join(chunk for chunk in chunks if chunk)
            # Making our text to lower case
           text = text.lower()
            # Tokenize text
           List = nltk.word_tokenize(text)
          # print('Terms after tokenization ')
           #print(List)
           #print('Stop Word List ')
           #print(StopWordsList)
           for i in range(len(List)):
             if List[i] in StopWordsList or List[i] in punc:  # if a token is in stop word list of only one character and in punction list ignore it
              zubi =0
             else:
               if ((len(List[i])) <= 3) or runer(List[i])==False:  # if a string length is less than 3 than ignore it as it usually does not give any meaning
                 zubi = 0
               else:
                 CleanDataList.append(porter.stem(List[i]))  # else add term to clean data after doing stemming

           #print('\n\n\nClean DATA AFTER STEMMING AND LOWER CASE AND MOST OF PUNCTION REMOVAL ')
           #print(CleanDataList)
           #-------------------------------------------Lines added for each iteration of clean list so for each documant

           index = 0
           #assinging  unique id and writing to file
           DOCID='Doc'+str(unique)
           Doc_Mapping.write(DOCID)
           Doc_Mapping.write(',')
           Doc_Mapping.write(directory+filename)
           Doc_Mapping.write('\n')
           for term in CleanDataList:        #Get through terms of current file
               key = term                    #Current term will be key
               if key not in thisdict:       #if key is not already present in dictionary
                   thisdict[key] = SingleRecode(term)  # Documant frequnacy on this line is zero and a new object is created
                   # UPDATED DOCUMANT FREQUANCY
                   thisdict[key].IncreaseDocumantFrequnacy(DOCID)  # update this line to id of current documant so in this case set to 1
                   thisdict[key].addDocumantID(DOCID)  # added documant ID

                   # update last documant id and term frequancy to +1
                   thisdict[key].updateLastDocumantID(DOCID)
                   thisdict[key].IncreaseTermFrequnacy()

                   # added position
                   thisdict[key].addPosition(index)   #postion in current index

               else:  # if bucket is already present
                   # No no need to add new object
                   # UPDATED DOCUMANT FREQUANCY
                   thisdict[key].IncreaseDocumantFrequnacy(DOCID)  # update this line to id of current documant so in this case set to 1
                   thisdict[key].addDocumantID(DOCID)  # added documant ID

                   # update last documant id and term frequancy to 1
                   thisdict[key].updateLastDocumantID(DOCID)  # if a new documant it will be checked in class function
                   thisdict[key].IncreaseTermFrequnacy()      #term frequnacy will be added

                   # added position
                   thisdict[key].addPosition(index)          #position will be added
               index = index + 1                             #go to next word in clean data list
               # --------------------------------------------------------------------------------
           del List
           del CleanDataList
           unique=unique+1 #increasing unique docID

    #Write after a whole directory is fully traversed
    KeysOFTerms = thisdict.keys()
    Doc_Mapping.close()

    IndexWriteFileName=''
    # checking which directory passed from main to decide output file name

    if directory=='corpus1/1/':          #directory is argumant name to preprocessing function
       IndexWriteFileName='index_1.txt'
    elif directory=='corpus1/2/':
        IndexWriteFileName = 'index_2.txt'
    elif directory=='corpus1/3/':
        IndexWriteFileName = 'index_3.txt'

    f = open(IndexWriteFileName, "w",encoding="utf-8")
    for x in sorted(KeysOFTerms):
     for i in thisdict[x].getList():
      #f.write(str(i))
      #f.write(',')
     #f.write('\n')
       f.write((str(i)))
       f.write(',')
     f.write('\n')

    f.close()
    return unique


































