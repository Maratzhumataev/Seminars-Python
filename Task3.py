# В некоторой школе решили набрать три новых математических класса 
# и оборудовать кабинеты для них новыми партами. За каждой партой 
# может сидеть два учащихся. Известно количество учащихся в каждом из 
# трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

class1 = 1
class2 = 2
class3 = 3
res1 = abs(-class1 // 2)
res2 = abs(-class2 // 2)
res3 = abs(-class3 // 2)
print(f"{res1}+{res2}+{res3}")
