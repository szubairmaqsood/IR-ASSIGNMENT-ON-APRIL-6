import csv
import io
import os
import string

# It will passed two files names of indexs to Maerge
def IndexMerging(file1,file2,outPutFileName):

    List1=[]
    List2=[]
    List3=[]
    File1Completed=False
    File2Completed=False


    Writer = open(outPutFileName, 'w', encoding="utf-8")
    f1=open(file1, 'r',encoding="utf-8")
    f2=open(file2, 'r',encoding="utf-8")
    Line1=f1.readline()
    Line2=f2.readline()


    List1 = Line1.split(",")
    List2 = Line2.split(",")

    while  True:
      if List1[0]<List2[0]:
        Writer.write(Line1)
        #print(Line1)
        Line1=f1.readline()
        if  not Line1:
         break;
        List1 = Line1.split(",")

      elif List1[0] >List2[0]:
        Writer.write(Line2)
        Line2=f2.readline()
        if  not Line2:
         break;
        List2 = Line2.split(",")




      elif List1[0]==List2[0]:
          #print(Line1)
          #print(Line2)
       try:
         number=int(List1[1])+ int(List2[1])
         List1[1]=str(number)
       except Exception:
           print(" ")
           #print(List1[0])

       del List1[(len(List1))-1]
       del List2[0]
       del List2[0]
       del List2[(len(List2)) - 1]
       '''
       for x in List1:
        List3.append(x)
        for x in List2:
         List3.append(x)
         '''
       List3=List1+List2

       #print("------List 1List2-------")
       for i in range(len(List3)):
        Writer.write(List3[i])
        Writer.write(',')
       Writer.write('\n')
        #Writer.write(str1 + str2 + '\n')
       Line1=f1.readline()
       Line2 =f2.readline()
       if not Line1:
         break;
       List1 = Line1.split(",")
      if not Line2:
          break;
      List2 = Line2.split(",")


    if File1Completed:
     while True:
        Writer.write(Line2)
        Line2 = f2.readline()
        if not Line2:
          break;
        List2 = Line2.split(",")

    else:
        while True:
         Writer.write(Line2)
         Line2 = f2.readline()
         if not Line2:
          break;
         List2 = Line2.split(",")






