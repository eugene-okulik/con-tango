str_1 = "результат операции: 42"
str_2 = "результат операции: 514"
str_3 = "результат работы программы: 9"

index_1 = str_1.find(":") + 2
print(int(str_1[index_1:]) + 10)

index_2 = str_2.find(":") + 2
print(int(str_2[index_2:]) + 10)

index_3 = str_3.find(":") + 2
print(int(str_3[index_3:]) + 10)
