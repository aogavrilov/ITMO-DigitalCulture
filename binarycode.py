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
power=0;
#print(chars)
while(len(chars)>=pow(2,power)):
    power+=1
#print(power)
result=[]
def binarycode(code,power1):
    if(power1 == power):
        if(len(result)<len(chars)):
            result.append(code+'0')
            return result.append(code+'1')
    else:
        binarycode(code+'0',power1+1)
        binarycode(code + '1', power1 + 1)

tmppower=0

binarycode('',0)
#---------------вывод кода------------
chars1 = dict()
tmpi=0
for x in chars:
    chars1[x] = result[tmpi]
    tmpi+=1
for x in line:
    print(chars1[x], end='')
#print(result)

