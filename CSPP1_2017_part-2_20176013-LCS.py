class exceptioncustom(Exception):
    pass

from os import listdir
path="C:\\Users\\barghav\\Desktop\\Project-CSPP"
listoffiles=[x for x in listdir(path) if x.endswith(".txt")]
def similar(x,y,i,j):
    count=0
    while(i<len(x)and j<len(y)):
        if(x[i].lower()==y[j].lower()):
            count+=len(x[i])                   
        i+=1
        j+=1        
    return(count)  


def getwords(filename):
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
def lcs(list1,list2):
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
                    (count)=similar(list1,list2,i,j)
                    if(count>c):
                        c=count
                j+=1
            i+=1


        return((2*c/(co1+co2))*100)
    except exceptioncustom as a:
##        print("The file is empty")
        return ("Can not compare as one or more files is empty")

##print(getwords("Bhargav1.txt"),getwords("Bhargav2.txt"))
##print(lcs(getwords("Bhargav1.txt"),getwords("Bhargav2.txt")))
length=len(listoffiles)
##result=[0 for i in range(length)]
##result=[result for i in range(length)]
for i in range(len(listoffiles)):
    for j in range(i,len(listoffiles)):
        print("Match between ",listoffiles[i],"and",listoffiles[j]," is",lcs(getwords(listoffiles[i]),getwords(listoffiles[j])))
    
    
