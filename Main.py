import PreProcessing as PP
import IndexMerging as IdxMerge

# PreProcessing each directory again make to 4
'''
uniqueID=1 #starting id of document is 1
for i in range(1,4):
 uniqueID=PP.PreProcessing('corpus1/'+ str(i)+'/',uniqueID)
 print("Completed")
 '''


#Start merging Index
IdxMerge.IndexMerging('index_1.txt','index_2.txt','Index1And2')
IdxMerge.IndexMerging('Index1And2','index_3.txt','inverted_index.txt')




