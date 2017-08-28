from os import listdir
path="C:\\Users\\barghav\\Desktop\\Project-CSPP"
listoffiles=[x for x in listdir(path) if x.endswith(".txt")]
##print(listoffiles)

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
##    print(a)
    res=[]
    for i in a:
        res.append(i.strip("\n"))
##    print(res)
    b=[]
    for i in res:
##        print(i)
        j=i.split(' ')
##        print(j)
        for a in j:
            a.strip('')
            if(len(a)!=0):
                b.append(a)
##                print(b)
    res=[]
    for i in b:
        c=removing(i)
        res.append(c)
##    print(res)
    dic={}
    for i in res:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
##    print(dic)
    x=0
    for i in dic.values():
        x+=i*i
        
    x=x**0.5
    return(dic,x)
def percentsimilar(x,y):    
    (a,b)=filehandling(x)
    (c,d)=filehandling(y)
    ##print(a,b,c,d)
    pro=0
    for i in a:
        for j in c:
            if(i==j):
                pro+=(int(a[i])*int(c[j]))
    if(b==0 or d==0):
        return ("One or more files is empty")
    else:
        return((pro/(b*d))*100)

##print("Hey",percentsimilar("Bhargav1.txt","Bhargav3.txt"))
a=[0 for x in range(len(listoffiles))]
a=[a for x in range(len(listoffiles))]

for i in range(len(listoffiles)):
    for j in range(i,len(listoffiles)):
        x=percentsimilar(listoffiles[i],listoffiles[j])
        
        print("Match between files ",listoffiles[i],listoffiles[j]," is",x)



