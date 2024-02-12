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

#Дана строка. Необходимо подсчитать количество чисел в этой строке,
#значение которых больше 5
#s= str(input("Введите строку: "))
def func_s2_1(s):
    length =len(s)
    i=0
    k=0
    while i<length:
       if '6'<=s[i]<='9':
           k+=1
       i+=1
    return k
#print(func_s2_1(s))
#Дана строка. Необходимо найти те символы кириллицы, которые не
#задействованы в данной строке.
#s= str(input("Введите строку: "))
def func_s2_2(s):
 cyr= 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
 string=''
 length =len(s)

 s=set(s)
 s={a.lower() for a in s}
 for a in cyr:
     if a not in s:
         string+=a

 return string
#print(func_s2_2(s))

#s= str(input("Введите строку: "))
#Дана строка. Необходимо найти максимальное из имеющихся в ней
#натуральных чисел.
def func_s2_3(s):
   number = s.split(" ")
   mas=[]
   for i,num in enumerate(number):
       if num.isdigit():
           mas.append(int(num))
   max=0
   for i in range(0,len(mas)):
       if mas[i]>=max: max=mas[i]
   return max
#print(func_s2_3(s))

#Дана строка. Необходимо найти все даты, которые описаны в виде "31 февраля 2007"

str = input("Введите строку")
import re
print(re.findall(r'\d{1,2} \w{3,8} \d\d\d\d', str))

# Прочитать список строк с клавиатуры. Упорядочить по длине строки.
n=int(input())
list=[]
for i in range(0,n):
  x=input()
  list.append(x)
n = int(input("Введите количество строк "))
input_str = []

for i in range(n):
    input_str.append(input("Введите строку: "))
print(sorted(input_str, key=len))

# Дан список строк с клавиатуры. Упорядочить по количеству слов в строке.
n = int(input("Введите количество строк "))
input_str = []

for i in range(n):
    input_str.append(input("Введите строку: "))
for i in range(n):
    input_str[i]=input_str[i].split(' ')
input_str = sorted(input_str, key=len)
for i in range(n):
    input_str[i]=' '.join(input_str[i])
print(input_str)

#Дан целочисленный массив. Необходимо осуществить циклический
#сдвиг элементов массива влево на три позиции.

#n=int(input("размерность массива:"))
#mas=[]
#for i in range(0,n):
 # x= x=int(input("Введите элемент массива:"))
 # mas.append(x)
def func_s5_1(mas):
    steps =3
    for i in range(steps):
        mas.append(mas.pop(0))
    return mas
#print(func_s5_1(mas))

#Дан целочисленный массив. Необходимо расположенные перед первым минимальным.
#n=int(input("размерность массива:"))
#mas=[]
#for i in range(0,n):
 # x= x=int(input("Введите элемент массива:"))
 # mas.append(x)
def func_s5_2(mas):
    min = mas[0]
    j=0
    for i in range(len(mas)):
        if mas[i]<min:
            min=mas[i]
            j=i
    if j==0:
     return -1
    else:
        return mas[j-1]
#print(func_s5_2(mas))

#Дан целочисленный массив и натуральный индекс (число, меньшее размера массива). Необходимо определить является ли элемент по указанному
#индексу локальным максимумом.
#n=int(input("размерность массива:"))
#mas=[]
#for i in range(0,n):
 #  x=int(input("Введите элемент массива:"))
 # mas.append(x)
#l=int(input())
def func_s5_3(mas,l):
    str1="элемент локальный максимум"
    str2 = "элемент не локальный максимум"
    if l!=0 and l!=mas[len(mas)-1]:
      if(mas[l-1]<mas[l] and mas[l+1]<mas[l]):
          return str1
      else:
          return str2
    elif l==0:
        if(mas[0]>mas[1]):
            return str1
        else:
            return str2
    elif l==mas[len(mas)]:
        if(mas[l]>mas[l-1]):
            return str1
        else:
            return str2

#print(func_s5_3(mas,l))
#Дан целочисленный массив. Найти все элементы, которые меньше
#среднего арифметического элементов массива.
#n=int(input("размерность массива:"))
#mas=[]
#for i in range(0,n):
 # x=int(input("Введите элемент массива:"))
 # mas.append(x)
def func_s5_4(mas):
    sum=0
    for i in range(len(mas)):
        sum+=mas[i]
    srar=sum/len(mas)
    mas2=[]
    for i in range(len(mas)):
        if(mas[i]<srar):
            mas2.append(mas[i])
    return mas2
#print(func_s5_4(mas))

#Для введенного списка построить список из элементов, встречающихся в исходном более трех раз.
#n=int(input("размерность :"))
#list=[]
#for i in range(0,n):
 # x=input("Введите элемент:")
 # list.append(x)
def func_s5_5(list):
    list2=[]
    for i in range(len(list)-1):
        k=0
        for j in range(len(list)-1):
          if  type(list[i])==type(list[j]):
             if list[i]==list[j]:
              k+=1
        if k>3:
            m=0
            for l in range(len(list2)):
                if type(list[i]) == type(list2[l]):
                    if list[i] == list2[l]:
                        m+=1
            if m==0:
             list2.append(list[i])

    return list2
#print(func_s5_5(list))

#В порядке увеличения квадратичного отклонения между средним
#весом ASCII-кода символа в строке и максимально среднего ASCII-кода
#тройки подряд идущих символов в строке.
#n = int(input("Введите количество строк "))
#s = []
#for i in range(n):
 #   s.append(input("Введите строку: "))

def weight(s):
    sum = 0
    for i in range(len(s)):
        sum += ord(s[i])
    return sum

def func_s4_3(s,n):
        mas = []
        for i in range(n):
            wi = weight(s[i])
            max_w = 0
            for j in range(len(s[i])-2):
                if (ord(s[i][j]) + ord(s[i][j+1]) + ord(s[i][j+2]))>max_w:
                    max_w = ord(s[i][j]) + ord(s[i][j+1]) + ord(s[i][j+2])
            mas.append([(wi / len(s[i]) - max_w / 3) ** 2, s[i]])
        mas = sorted(mas)
        return mas
#print(func_s4_3(s, n))

#В порядке увеличения медианного значения выборки строк (прошлое
#медианное значение удаляется из выборки и производится поиск нового
#медианного значения).
#n = int(input("Введите количество строк "))
#s = []
#for i in range(n):
#   s.append(input("Введите строку: "))
def func_s4_2(s, n):
    mas = []
    si=[]
    mas2=[]
    for i in range(n):
        si = sorted(s[i])

        if int(len(si[i])%2)==0:
            med=(si[(len(si))/2]+si[(len(si))/2-1])/2
        else:
            med = (si[int((len(si) - 1) / 2)])
        mas.append([med,s[i]])
    mas=sorted(mas)
    return mas


#print(func_s4_2(s, n))

#В порядке увеличение квадратичного отклонения частоты
#встречаемости самого распространенного символа в наборе строк от частоты
#его встречаемости в данной строке.
#n = int(input("Введите количество строк "))
#s = []
#for i in range(n):
 #  s.append(input("Введите строку: "))
def func_sa_3(s, n):
    res=[]
    s1=""
    mas=[]
    for q in range(n):
      s1+=s[q]
    dlin=len(s1)
    t = ([(s1.count(i), i) for i in s1])
    g = sorted(set(t))[::-1][:1]
    for l in range(n):
      kol=0
      dlini=len(s[l])
      for a in range(len(s[l])):
          if s[l][a]==g[0][1]:
           kol+=1
      mas.append([(g[0][0] / dlin - kol /dlini)** 2, s[l]])
    mas = sorted(mas)

    return mas
#print(func_sa_3(s, n))

#В порядке увеличения разницы между частотой наиболее часто
#встречаемого символа в строке и частотой его появления в алфавите.
#n = int(input("Введите количество строк "))
#s = []
#for i in range(n):
#   s.append(input("Введите строку: "))
def func_sa_2(s, n):
    frequency = dict(
        {'e': 0.130, 't': 0.105, 'a': 0.081, 'o': 0.079, 'n': 0.071, 'r': 0.068, 'i': 0.63, 's': 0.061, 'h': 0.052,
         'd': 0.038, 'l': 0.034, 'f': 0.029, 'c': 0.027, 'm': 0.025, 'u': 0.024, 'g': 0.020, 'y': 0.019, 'p': 0.019,
         'w': 0.014, 'v': 0.009, 'k': 0.0015, 'j': 0.0013, 'q': 0.0011, 'z': 0.0007})
    res=[]
    for l in range(n):
      h=[]
      t = ([(s[l].count(i), i) for i in s[l]])
      g=sorted(set(t))[::-1][:1]
      kol = g[0][0]
      element = g[0][1]
      x=frequency.get(element)
      res.append(kol-x)
    mas=[]
    for j in range(n):
     mas.append([res[j],s[j]])
    mas = sorted(mas)

    return mas
#print(func_sa_2(s, n))