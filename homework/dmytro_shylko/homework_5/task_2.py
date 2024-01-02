"""Module providing a function printing python version."""

str_1 = "результат операции: 42"
str_2 = "результат операции: 514"
str_3 = "результат работы программы: 9"

index_1 = str_1.find("42")
number_1 = int(str_1[index_1:]) + 10
print(number_1)

index_2 = str_2.find("514")
number_2 = int(str_2[index_2:]) + 10
print(number_2)

index_3 = str_3.find("9")
number_3 = int(str_3[index_3:]) + 10
print(number_3)
