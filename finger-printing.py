class plaigarism(object):
    def remove_stop_words(self,filename):
        stop_words=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
        x=open(filename)
        a=(x.readlines())
##        print(a)
        res=[]
        for i in a:
            res.append(i.strip("\n"))
##        print(res)
        b=[]
        for i in res:
##            print(i)
            j=i.split(' ')
##            print(j)
            for s in j:
                s.strip('')
                if(s!=''):
                    b.append(s)
##        print(b)
        main=[]
        for i in b:
            if i not in stop_words:
                main.append(i)
        st="qwertyuiopasdfghjklzxcvbnm0123456789_"
        mst=""

        for i in main:
            for j in i:
                
                if j in st:
                    if j!='':
                        mst+=j
##        print(mst)
        hash_list=[]
        if(len(mst)>5):
            i=0
            while(i<len(mst)-4):
                substr=mst[i:i+5]
                i+=1
                hash_list.append(substr)
##        print(hash_list)
        hash_list_value=[]
        for i in hash_list:
            hash_value=0
            for j in range(5):
                hash_value+=ord(i[j])*(5**(5-j))
                hash_list_value.append(hash_value)           
##        print(hash_list_value)
        return(hash_list_value)
    def hashing_and_comparing(self,x,y):
        x=self.remove_stop_words(x)
        y=self.remove_stop_words(y)
        if(len(x)!=0 and len(y)!=0):
            l=max(len(x),len(y))
            l=l*100
            while(True):
                q=l+1
                if(isprime(q)):
                    break
                l=l+1
##            print(q)
            hash_list1=[]
            hash_list2=[]
            for i in x:
                mod=i%q
                hash_list1.append(mod)
            for i in y:
                mod=i%q
                hash_list2.append(mod)    
            match=[]
##            print(hash_list1,hash_list2)
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

        
    
##        l=len(hash_list_value)*100
def isprime(n):
    if(n%2==0):
        return(False)
    else:
        for i in range(3,int(n**0.5)+1):
            if n%i==0:
                return(False)
        return(True)
        
from os import listdir
path="C:\\Users\\barghav\\Desktop\\Project-CSPP"
listoffiles=[x for x in listdir(path) if x.endswith(".txt")]
p=plaigarism()
##p.remove_stop_words("Bhargav1.txt")
##print(p.hashing_and_comparing("Bhargav1.txt","Bhargav2.txt"))
for i in range(len(listoffiles)):
    for j in range(i,len(listoffiles)):
        print("Match between ",listoffiles[i],"and",listoffiles[j]," is",p.hashing_and_comparing(listoffiles[i],listoffiles[j]))
