#Найти сумму непростых делителей числа.
#x=int(input("Введите число: "))
def f_1(x):
    sum=0
    for i in range(1,x):
        k=0
        if(x%i==0):
            for j in range(1,i):
                if(i%j==0):
                   k+=1
            if k>1:
                sum=sum+i
    return sum

#print(f_1(x))
#Найти количество цифр числа, меньших 3
#x=int(input("Введите число: "))
def f_2(x):
    k=0
    while x>1:
        if(x%10<3):
            k+=1
        x=x/10
    return k
#print(f_2(x))
#Найти количество чисел, не являющихся делителями
#исходного числа, не взамнопростых с ним и взаимно простых с суммой
#простых цифр этого числа.
#x=int(input("Введите число: "))
def f_31(x):
    k=0
    s = 0
    m = x
    while m > 1:
        z = int(m % 10)
        g = 0
        for q in range(1, z):
            if (z % q == 0):
                g += 1
        if (g == 1):
            s += z
        m = (m // 10)
    for i in range(1,x):
        if(x%i!=0):
            h=0
            for j in range(1,i):
                if (x%j==0 and i%j==0):
                   h+=1
            if (h>1):
                if(i>s):
                    y=0
                    for d in range(1, s):
                        if (s % d == 0 and i % d == 0):
                            y+=1
                    if(y==1):
                        k+=1
                    else:
                        y = 0
                        for d in range(1, x):
                            if (s % d == 0 and i % d == 0):
                                y += 1
                        if (y == 1):
                                k += 1


    return k
#print(f_31(x))
#Дана строка в которой записаны слова через пробел. Необходимо
#перемешать в каждом слове все символы в случайном порядке кроме первого
#и последнего.
import random
#x= str(input("Введите строку: "))
def func_s_2(x):
    s = x.split()
    for i in range(0, len(s)):

      if len(s[i]) > 2:
        e1 = s[i]
        e2 = list(e1[1:len(e1) - 1])
        random.shuffle(e2)
        e2 = "".join(e2)
        e1 = s[i][0] + e2 + s[i][len(s[i]) - 1]
        s[i] = "".join(e1)
    s = " ".join(s)
    return(s)



#print(func_s_2(x))
import random
#Дана строка в которой содержатся цифры и буквы. Необходимо
#расположить все цифры в начале строки, а буквы – в конце.
#s= str(input("Введите строку: "))
def func_s_3(s):
 length =len(s)

 i=0
 while i<length:
  s_int = ''
  s_str = ''
  while i<length:
     if ('0'<=s[i]<='9'):
      s_int +=s[i]
     else: s_str +=s[i]
     i+=1
  i+=1
  str1=s_int+s_str

 return str1

#print(func_s_3(s))

#Дана строка в которой записаны слова через пробел. Необходимо
#перемешать все слова в случайном порядке (спонсор задачи Мастер Йода).
#s= str(input("Введите строку: "))
def func_s_4(s):
 words = s.split(" ")
 random.shuffle(words)
 words1 = ''.join(words)
 return (words1)

#print(func_s_4(s))
