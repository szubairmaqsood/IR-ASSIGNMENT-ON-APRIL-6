import urllib
from bs4 import BeautifulSoup
import nltk
from nltk.stem import PorterStemmer
import string
from SingleObjectInFile import SingleRecode

'''def puncCheck(List):
    punc = string.punctuation
    for i in List :
        if i not in punc:
            return False
    return True'''


zubi=0                      # a verible that do b=nothing but used as nessity
punc = string.punctuation   # string containling only punction characters
print('Punction List')
print(punc)
StopWordsList=[]           #  LIST TO COntain stop words list
List=[]                    # All terms read from a file
CleanDataList=[]           #Final clean result
porter = PorterStemmer()   #Object  to do stemming
#allowed_chars = set(punc)


# Read data from file of html and stop words from other list
html=open('corpus1/1/clueweb12-0000tw-13-04988').read()
stopWordFile=open('stoplist.txt')
StopWordsList =stopWordFile.read().splitlines()

#Creating soup object
soup = BeautifulSoup(html,'html.parser')


# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.find('body').get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

#Making our text to lower case
text=text.lower()

#Tokenize text
List=nltk.word_tokenize(text)

print('Terms after tokenization ')
print(List)
print('Stop Word List ')
print(StopWordsList)

for i in range(len(List)):
    if List[i] in StopWordsList or List[i] in punc: #if a token is in stop word list of only one character and in punction list ignore it
        zubi=0

    else:
        if ((len(List[i]))<3):   # if a string length is less than 3 than ignore it as it usually does not give any meaning
           zubi=0
        else:
            CleanDataList.append(porter.stem(List[i]))         #else add term to clean data after doing stemming


print('\n\n\nClean DATA AFTER STEMMING AND LOWER CASE AND MOST OF PUNCTION REMOVAL ')
print(CleanDataList)

thisdict ={}                # dictionary

'''
index=0
for term in CleanDataList:
    key=term
    if key not in thisdict:
        thisdict[key]=[]
        thisdict[key].append(key)
        thisdict[key].append(0)
        thisdict[key][1]=thisdict[key][1]+1
        #I STILL HAVE TO MANAGE DOC ID AND TERM FREQUNACY AS WELL
        thisdict[key].append(index)
    else:
        thisdict[key].append(index)
    index=index+1
print(thisdict)
'''

index=0
DOCID='corpus1/1/clueweb12-0000tw-13-04988'
for term in CleanDataList:

    key=term
    if key not in thisdict:
        thisdict[key]=SingleRecode(term)  #Documant frequnacy on this line is zero
        #UPDATED DOCUMANT FREQUANCY
        thisdict[key].IncreaseDocumantFrequnacy(DOCID) #update this line to id of current documant so in this case set to 1
        thisdict[key].addDocumantID(DOCID)             #added documant ID

        #update last documant id and term frequancy to 1
        thisdict[key].updateLastDocumantID(DOCID)
        thisdict[key].IncreaseTermFrequnacy()

        # added position
        thisdict[key].addPosition(index)

    else: #if bucket is already present
         # No no need to add new object
        # UPDATED DOCUMANT FREQUANCY
        thisdict[key].IncreaseDocumantFrequnacy(DOCID)  # update this line to id of current documant so in this case set to 1
        thisdict[key].addDocumantID(DOCID)  # added documant ID

        # update last documant id and term frequancy to 1
        thisdict[key].updateLastDocumantID(DOCID)    #if a new documant
        thisdict[key].IncreaseTermFrequnacy()

        # added position
        thisdict[key].addPosition(index)
    index=index+1

KeysOFTerms = thisdict.keys()
for x in KeysOFTerms:
 thisdict[x].PrintList()
