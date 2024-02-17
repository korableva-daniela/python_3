n=int(input("Введите количество строк "))
line=[]
for i in range(n):
    x=str(input("Введите строкy "))
    line.append(x)
#Дан текст: в первой строке записано число строк, далее идут сами
#строки. Определите, сколько различных слов содержится в этом тексте.
#Словом считается последовательность непробельных символов идущих
#подряд, слова разделены одним или большим числом пробелов или символами
#конца строки.


def num_of_words(line,n):
  words=set()
  for i in range(n):
      words.update(line[i].split())
  return words
#print(num_of_words(line,n))

#Дан текст: в первой строке записано количество строк в тексте, а затем
#сами строки. Выведите все слова, встречающиеся в тексте, по одному на
#каждую строку. Слова должны быть отсортированы по убыванию их
#количества появления в тексте, а при одинаковой частоте появления – в
#лексикографическом порядке.
def frequency_of_words(line,n):
 slov ={}
 mas=[]

 for i in range(n):
     words=line[i].split()
     for j in words :
       slov[j]=slov.get(j,0)+1
 for l in sorted(slov.items(), key=lambda x:(-x[1],x[0])):
    mas.append(l[0])
 text='\n'.join(mas)
 return text

print(frequency_of_words(line,n))