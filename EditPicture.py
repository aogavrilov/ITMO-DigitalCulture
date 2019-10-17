import numpy as np
import cv2
img = cv2.imread("key-flat-128x128.png",0)
line = img[64]
chars = set()
chars_count={}
for i in range(len(line)):
    line[i]= line[i]//20*20
for i in range(len(line)):
    if(line[i] in chars):
        chars_count[line[i]]+=1
    else:
        chars_count[line[i]] = 1
        chars.add(line[i])


#==============================================Haffmans's code=========================================================================================#


class charcode(object):#Класс для каждого различного символа, в котором хранится инфа о нем
    frequency=0 #Частота встречаемости в коде
    char_=''#Сам символ
    char_byte=''#Его двоичный код
    left=''#Левый лист при наличии
    right=''#Правый лист при наличии
objs={}#Словарь символов
#---------------------------Записываем элементы из массива в массив объектов-символов
for xkey,xvalue in chars_count.items():
    tmp=charcode()
    tmp.frequency = int(xvalue)
    tmp.char=xkey
    objs[xkey] = tmp

#-----------Дублируем словарь, чтобы был массив для восстановления кода в обратном порядке
objtmp={}
objtmp = objs.copy()
#Идем по графу от листьев к вершинам, записываем значение вершинам
while(len(objs)>1):
    #Находим правый лист
    min1=''
    for x in objs:
        if(min1 ==''): min1=x
        elif(objs[x].frequency<objs[min1].frequency): min1=x
    r=objs.pop(min1)

    #Находим левый лист
    min2=''
    for x in objs:
        if(min2 ==''): min2=x
        elif(objs[x].frequency<objs[min2].frequency): min2=x
    l=objs.pop(min2)
    #Добавляем вершину в массивы
    z=charcode()

    z.frequency = int(l.frequency)+int(r.frequency)
    z.left=l.char
    z.right = r.char
    z.char=str(l.char)+str(r.char)

    objs[z.char] = z
    objtmp[z.char] = z
for x in objs:
    print(objs[x].char,objs[x].frequency,objs[x].left,objs[x].right)
#--------------------Восстановление листьев с кодами-------------------
answers ={}#Массив конечных листьев
while(len(objs)>0):
    xk,xv=objs.popitem()
    if(xv.left!=''):
        tmp=charcode()
        tmp.char_byte=xv.char_byte+'0'
        tmp.char = xv.left
        tmp.left = objtmp[xv.left].left
        tmp.right = objtmp[xv.left].right
        tmp.frequency =  objtmp[xv.left].frequency
        objs[tmp.char] = tmp
       # print(tmp.)
    if(xv.right!=''):
        tmp=charcode()
        tmp.char_byte=xv.char_byte+'1'
        tmp.char = xv.right
        tmp.left = objtmp[xv.right].left
        tmp.right = objtmp[xv.right].right
        tmp.frequency =  objtmp[xv.right].frequency
        objs[tmp.char] =tmp
    if(xv.right=='' and xv.left ==''):
        answers[xk]= xv
for xv in answers.keys():
    print(answers[xv].char, answers[xv].char_byte,answers[xv].frequency)


#===========================================================Shenon-Fanno's code===================================================#
result=[]

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
        result.append([p1[0][0],code+'0'])
    if(len(p2)>1):
        sf(p2,code+'1')
    else:
        result.append([p2[0][0],code+'1'])
array_chars=[]
probability = 0

for char in chars_count.keys():
    probability+=chars_count[char]
for char in chars_count.keys():
    chars_count[char]/=probability
for k,i in chars_count.items():
    array_chars.append([k,i])
array_chars.sort(key = lambda char:char[1], reverse =True )
sf(array_chars,'')

print(result)
#---------------вывод кода------------
chars1 = dict()
tmpi=0
for xv in answers.keys():
    chars1[answers[xv].char] = answers[xv].char_byte
    tmpi+=1
for x in line:
    print(chars1[x], end='')

'''
for xv in answers.keys():
    print(answers[xv].char, answers[xv].char_byte,answers[xv].frequency)

'''
#print(result)
#chars_count[line[i]]
