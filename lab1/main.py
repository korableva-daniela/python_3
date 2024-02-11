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

