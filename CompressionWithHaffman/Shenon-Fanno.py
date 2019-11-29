
result=[]

#a - элемент [значение,частота встречаемости]
def sf(a,code):
    p1=[]
    p1_probability=0
    p2=[]
    p2_probability=0
    a2=[]
    a2.extend(a)
    while(len(a2)!=0):
        if(p1_probability<=p2_probability):
            p1.append(a2.pop(0))
            p1_probability+=p1[len(p1)-1][1]
        else:
            p2.append(a2.pop())
            p2_probability+=p2[len(p2)-1][1]
    if(len(p1)>1):
        sf(p1,code+'0')
    else:
        result.append([p1[0][0],"bitecode"])
    if(len(p2)>1):
        sf(p2,code+'1')
    else:
        result.append([p2[0][0],"bitecode"])


#Получили массив a[n]
a =input().split()

for i in range(len(a)):
    a[i]=[int(a[i])
sf()
#array result =[]
