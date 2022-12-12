import math
import os
clear = lambda: os.system('cls')
clear()
def crivolinV1(x1,x2):
    s1=(x2*x2*x2*x2/4+2*x2*x2*x2/3+x2*x2)-(x1*x1*x1*x1/4+2*x1*x1*x1/3+x1*x1)
    return(s1)
def crivolinV2(x1,x2):
    h=int(input('введите шаг:'))
    s2=0
    p=x2-x1
    for i in range(0,h-1):
        j=x1+(p/h)*i
        y=(j*j*j+2*j*j+2*j)*(p/h)
        s2+=y
    return(s2)
def conv():
 x1,x2=map(int,input("введите координаты x1 и x2:").split())
 s1=crivolinV1(x1,x2)
 s2=crivolinV2(x1,x2)
 print('площадь без погрешности равна ',s1)
 print('площадь с погрешностью равна ',s2)
 print("вам нужна оценка погрешности?(1-да,0-нет)")
 choice = input('введите свой выбор:\n')
 choice = int(choice)
 if choice is 1: print(s1-s2)
 print('вы хотите использовать программу ещё раз?(1/0)')
 p=int(input())
 if p==1:
    clear()
    conv()
 else:
    clear()
    print('спасибо воспользовались этой программой')
    input()
conv()
