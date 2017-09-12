
import random

# 产生一个随机4位数
def gener_key():
    key =[0,0,0,0]
    key[0] = random.randint(1,9)
    key[1] = random.randint(0,9)
    while key[0]==key[1]:
        key[1] = random.randint(0,9)
    key[2] = random.randint(0,9)
    while (key[0]==key[2]) or (key[1]==key[2]):
        key[2] = random.randint(0,9)
    key[3] = random.randint(0,9)
    while (key[0]==key[3]) or (key[1]==key[3]) or (key[2]==key[3]):
        key[3] = random.randint(0,9)

    return key

# 将输入的数字分解成一个列表
def splitdigit(num):
    j = 1000
    digits = [0,0,0,0]
    for i in range(0,4):
        digits[i] = int(num/j)
        num = num%j
        j = j/10 
    return digits

#将输入数字和答案进行逐一比较
def comparedigit(key,digits):
    a = 0
    b = 0
    for i in range(0,4):
        if key[i] == digits[i]:
            a += 1
        else:
            for j in range(0,4):
                if key[i] == digits[j]:
                    b += 1
                    break
    print("%dA%dB"%(a,b))     
    return (a,b)


i = 10

key = gener_key() 
#print("答案是",key)

while True:
    num =input("请输入数字")
    if num.isdigit() != 1:
        print("输入的不是数字，请输入数字")
        continue
    else:
        num = int(num)
        num = splitdigit(num)
        print(num)
        i-=1
        a,b =  comparedigit(key,num)
        if a == 4:
            print("答案完全正确\n结束")
            exit(0)
        else:
            print("答案不正确\n你还有 %d次机会"%i)
 
        if i == 0:
           print("结束")
           exit(0)


    
    






