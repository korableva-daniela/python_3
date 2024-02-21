#Реализовать функцию, которая будет проверять, является ли
#введенная строка номером кредитной карты, возвращаемое значение true или
#False. Дополнительно реализовать функцию, которая выбрасывает исключение
#о некорректном аргументе, иначе возвращает номер кредитной карты.
import re
s = input("Введите строку")

def credit_card(s):
    if(re.findall(r'\s\d{4} \d{4} \d{4} \d{4}\s', s)):
        return True
    else: return False
print(credit_card(s))


def check_credit_card(s):
    try:
        if credit_card(s):
            print(s)
        else:
            raise Exception('The credit card number is entered incorrectly in the line')
    except Exception:
        print(' Необходимо ввести номер кредитной карты по правилам!' ,s, 'не подходит:',"\n",
              'До и после номера кредитной карты должны быть пробелы.',"\n",
              'В самом номере каждые 4 цифры должны быть разграничены пробелами.')
check_credit_card(s)