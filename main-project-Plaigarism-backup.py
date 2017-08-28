'''
This library helps us importing features of date and time
'''
import time

'''
This is a custom exception created used to raise when the length of bag is zero in case of bag of words
'''
class exceptioncustom(Exception):
    pass

from os import listdir
'''
glob helps us run the program even if the os is changed
'''
import glob

path="C:\\Users\\barghav\\Desktop\\Project-CSPP"
listoffiles=[x for x in listdir(path) if x.endswith(".txt") and x!="logs.txt"]
def isprime(n):
    '''
    This function takes an integer as input and returns true in case of prime and false if it is non prime 
    '''
    if(n%2==0):
        return(False)
    else:
        for i in range(3,int(n**0.5)+1):
            if n%i==0:
                return(False)
        return(True)
    
class plaigarism(object):
    '''
    This is a main class created and all the methods are part of this class
    '''
    '''
    These are functions for finger printing
    '''
    def remove_stop_words(self,filename):
        '''
        This function gets a file as input and then performs the operations like removing the stop words, removing the special characters, spaces
        and then it creates the sub strings for the hash table and then returns that list
        '''
        stop_words=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
        x=open(filename)
        a=(x.readlines())
        res=[]
        for i in a:# i is a line in file
            res.append(i.strip("\n"))#We get all the lines in the file in a single line
        b=[]
        for i in res:
            j=i.split(' ')# we get all the words which are separated by space
            for s in j:
                s.strip('')# we are eliminating null characters 
                if(s!=''):
                    b.append(s)
        main=[]
        for i in b:
            i=i.lower()
            if i not in stop_words:# we remove all the stop words from out list of words
                main.append(i)
        st="qwertyuiopasdfghjklzxcvbnm0123456789_"
        mst=""

        for i in main:# i is a words
            for j in i:# j is a letter in word i
                
                if j in st:# checking if the letter is in required set of characters or not
                    if j!='':# appending all the letters to form a master string mst eliminating nulls
                        mst+=j
        hash_list=[]
        if(len(mst)>5):
            i=0
            while(i<len(mst)-4):# generating sub strings and they are appended in hash list
                substr=mst[i:i+5]
                i+=1
                hash_list.append(substr)
        hash_list_value=[]
        for i in hash_list:
            hash_value=0
            for j in range(5):
                hash_value+=ord(i[j])*(5**(5-j))# generating a hash value for a sub string in hash list
                hash_list_value.append(hash_value)           
        return(hash_list_value)
    def hashing_and_comparing(self,x,y):
        '''
        This function gets 2 lists which are returned from other function, then it chooses a proper denominator, creates a proper hash table and then compares the
        values using a formula similar to bag of words and then returns the percentage match
        '''
        x=self.remove_stop_words(x)
        y=self.remove_stop_words(y)
        if(len(x)!=0 and len(y)!=0):
            l=max(len(x),len(y))
            l=l*100
            while(True):
                q=l+1
                if(isprime(q)):# after getting lengths of hash tables, we find the largest prime number that is just greater than length of hash value*100
                    break
                l=l+1
            hash_list1=[]
            hash_list2=[]
            for i in x:
                mod=i%q #we are obtaining the hash value by dividing with q(largest prime number)
                hash_list1.append(mod)
            for i in y:
                mod=i%q
                hash_list2.append(mod)    
            match=[] # this array stores the matched values from 2 tables
            for i in hash_list1:
                if i in hash_list2:
                    if(i==i):
                        c=min(hash_list1.count(i),hash_list2.count(i))
                        if i not in match:
                            for k in range(c):
                                match.append(i)
                
            return(2*len(match)/(len(x)+len(y)))*100
        else:
            return("These are empty files")   
    '''
    These are functions for bag of words
    '''
    def similar(self,x,y,i,j):
        '''
        This function gets 4 inputs 2 lists and the indexes where an exact match is found, it then checks the whole lists and returns the count of letters of
        matched words and then returns that count
        '''
        count=0
        while(i<len(x)and j<len(y)):
            if(x[i].lower()==y[j].lower()):
                count+=len(x[i])                   
            i+=1
            j+=1        
        return(count)  

    def getwords(self,filename):
        '''
        This funtion gets a filename as input then it reads from the file, extracts all the sentences and then words
        and then operates on it, removes any null characters if present
        '''
        x=open(filename)
        a=(x.readlines())
        res=[]
        for i in a:
            res.append(i.strip("\n"))
        b=[]
        for i in res:
            j=i.split(' ')
            for a in j:
                a.strip('')
                if(len(a)!=0):
                    b.append(a)
        return(b)
    '''
    These are functions for Largest Common String
    '''
    def lcs(self,list1,list2):
        '''
        This function gets 2 lists, then compares the words of the lists to check if there is a match
        if there is a match then calls another function
        It even raises an exception if any of the list is empty
        It then returns the percentage of match between lists
        '''
        co1=0
        co2=0
        for p in list1:
            co1+=len(p)
        for q in list2:
            co2+=len(q)
        try:
            if(co1==0 or co2==0):
                raise exceptioncustom
            
            i=0
            c=0
            while(i<len(list1)):
                j=0
                while(j<len(list2)):
                    if(list1[i]==list2[j]):
                        (count)=self.similar(list1,list2,i,j)
                        if(count>c):
                            c=count
                    j+=1
                i+=1
            return((2*c/(co1+co2))*100)
        except exceptioncustom as a:
            return ("Can not compare as one or more files is empty")

    
    def removing(self,i):
        '''
        This function gets a word as input, then checks the letters of that word, if there are any letters other than alphanumeric along with _
        removes them and returns the modified word
        '''
        st='qwertyuiopasdfghjklzxcvbnm0123456789_'
        i=i.lower()# changing to lower case
        b=""
        for x in i:
            if x in st:
                b+=x
        return b        
    def filehandling(self,filename):
        '''
        This funtion gets a filename as input then it reads from the file, extracts all the sentences and then words
        and then calls a function to remove special characters from that word.
        It then creates a dictionary with unique word as key and number of times that word appeared as value.
        It even returns denominator for the formulae
        '''
        x=open(filename)
        a=(x.readlines())

        res=[]
        for i in a:
            res.append(i.strip("\n"))

        b=[]
        for i in res:

            j=i.split(' ')

            for a in j:
                a.strip('')
                if(len(a)!=0):
                    b.append(a)
        res=[]
        for i in b:
            c=self.removing(i)
            res.append(c)
        dic={}
        for i in res:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        x=0
        for i in dic.values():
            x+=i*i
        x=x**0.5
        return(dic,x)

    def percentsimilar(self,x,y):
        '''
        This function gets 2 inputs which are names of files.
        Then in turn invokes respective functions which yield a dictionary and denominator for the formula
        We then comraes the dictionaries, if there is a match multiplies its values and sums the whole
        It then returns a percent match and if there is an empty file, it returns a string stating file is empty
        '''
        (a,b)=self.filehandling(x)
        (c,d)=self.filehandling(y)
        
        pro=0
        for i in a:
            for j in c:
                if(i==j):
                    pro+=(int(a[i])*int(c[j]))
        if(b==0 or d==0):
            return ("One or more files is empty")
        else:
            return((pro/(b*d))*100)

'''
This is main function
'''

p=plaigarism()
logfile=open("logs.txt",'a+')

logfile.write(time.ctime())
logfile.write('\n')
logfile.write("Using LCS method"+'\n')
length=len(listoffiles)
print("Using bag of words")
for i in range(len(listoffiles)):
    for j in range(i,len(listoffiles)):
        print("Match between ",listoffiles[i],"and",listoffiles[j]," is",p.lcs(p.getwords(listoffiles[i]),p.getwords(listoffiles[j])))
        logfile.write("Match between "+listoffiles[i]+" and "+listoffiles[j]+" is "+str(p.lcs(p.getwords(listoffiles[i]),p.getwords(listoffiles[j]))))
        logfile.write("\n")
print("-------------------------------------------------------------------------------")
logfile.write('\n')
logfile.write("Using bag of words method"+'\n')
print("Using LCS method")
for i in range(len(listoffiles)):
    for j in range(i,len(listoffiles)):
        x=p.percentsimilar(listoffiles[i],listoffiles[j])
        logfile.write("Match between files "+str(listoffiles[i])+str(listoffiles[j])+" is "+str(x)+'\n')
        print("Match between files ",listoffiles[i],listoffiles[j]," is",x)
logfile.write("\n")
print("-------------------------------------------------------------------------------")
for i in range(len(listoffiles)):
    for j in range(i,len(listoffiles)):
        print("Match using fingerprinting between ",listoffiles[i],"and",listoffiles[j]," is",p.hashing_and_comparing(listoffiles[i],listoffiles[j]))
        logfile.write("Match between files "+str(listoffiles[i])+str(listoffiles[j])+" using finger printing is "+str(p.hashing_and_comparing(listoffiles[i],listoffiles[j]))+'\n')
        

logfile.write('\n'+'\n')
logfile.close()



