#Дан файл, содержащий текст на русском языке. Определить,
#сколько раз встречается в нем самое длинное слово.
def num_max_word():
 f= open('new_file.txt', 'r', encoding='utf-8')

 text=f.read().split()

 words = set()
 for i in range(len(text)):
  words.update(text)
 max_words=max(words,key=len)

 return(text.count(max_words))
#По каналу связи передаётся последовательность целых чисел - показания
#прибора. В течение N минут (N – натуральное число) прибор ежеминутно
#регистрирует значение силы тока (в условных единицах) в электрической сети
#и передаёт его на сервер. Определите три таких переданных числа, чтобы
#между моментами передачи любых двух из них прошло не менее К минут, а
#сумма этих чисел была минимально возможной. Запишите в ответе найденную
#сумму.
#print(num_max_word())
import sys
def current_strength():
 f= open('27-165b.txt', 'r', encoding='utf-8')
 line = f.readline().split()
 n=int(line[0])
 k=int(line[1])
 file = f.read().split()
 st = sys.maxsize
 fin =sys.maxsize
 summa =sys.maxsize
 for i in range(2*k,n):
    st = min(st, int(file[i-2*k]))
    fin = min(fin, st + int(file[i-k]))
    summa = min(summa, fin + int(file[i]))
 return(summa)

print(current_strength())

