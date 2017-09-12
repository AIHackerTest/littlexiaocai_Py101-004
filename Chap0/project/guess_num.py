
import random
key = random.randint(0,20)

i = 10
while True:
    num =input("请输入数字")
    if num.isdigit() != 1:
        print("输入的不是数字，请输入数字")
        continue
    else:
        num = int(num)
        i-=1
        if num == key:
            print("答案正确，答案就是%d\n结束"%key) 
            exit(0)
        elif num > key:
            print("比正确答案大了\n你还有 %d次机会"%i)
        elif num < key:
            print("比正确答案小了\n你还有%d次机会"%i)
    
        if i == 0:
            print("结束")
            exit(0)
    
    






