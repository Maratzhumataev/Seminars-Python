# Найдите сумму цифр трехзначного числа.

number = int(input("Введите трехзначное число"))
if number > 0:
    summa = (number % 10) + ((number//10)%10) + (number // 100)
    print(summa)