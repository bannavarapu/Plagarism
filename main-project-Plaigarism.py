import logging
import time


class exceptioncustom(Exception):
    pass

from os import listdir
path="C:\\Users\\barghav\\Desktop\\Project-CSPP"
listoffiles=[x for x in listdir(path) if x.endswith(".txt") and x!="logs.txt"]
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
logfile=open("logs.txt",'a+')

logfile.write(time.ctime())
logfile.write('\n')
logfile.write("Using LCS method"+'\n')
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
        return ("Can not compare as one or more files is empty")

length=len(listoffiles)

for i in range(len(listoffiles)):
    for j in range(i,len(listoffiles)):
        print("Match between ",listoffiles[i],"and",listoffiles[j]," is",lcs(getwords(listoffiles[i]),getwords(listoffiles[j])))
        logfile.write("Match between "+listoffiles[i]+" and "+listoffiles[j]+" is "+str(lcs(getwords(listoffiles[i]),getwords(listoffiles[j]))))
        logfile.write("\n")
def removing(i):
    st='qwertyuiopasdfghjklzxcvbnm0123456789_'
    i.lower()
    b=""
    for x in i:
        if x in st:
            b+=x
    return b        
            



def filehandling(filename):
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
        c=removing(i)
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
def percentsimilar(x,y):    
    (a,b)=filehandling(x)
    (c,d)=filehandling(y)
    
    pro=0
    for i in a:
        for j in c:
            if(i==j):
                pro+=(int(a[i])*int(c[j]))
    if(b==0 or d==0):
        return ("One or more files is empty")
    else:
        return((pro/(b*d))*100)

logfile.write('\n')
logfile.write("Using bag of words method"+'\n')
for i in range(len(listoffiles)):
    for j in range(i,len(listoffiles)):
        x=percentsimilar(listoffiles[i],listoffiles[j])
        logfile.write("Match between files "+str(listoffiles[i])+str(listoffiles[j])+" is "+str(x)+'\n')
        print("Match between files ",listoffiles[i],listoffiles[j]," is",x)
logfile.close()
logfile.write('\n'+'\n')


