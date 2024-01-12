str_1 = "результат операции: 42"
str_2 = "результат операции: 514"
str_3 = "результат работы программы: 9"
str_4 = "результат: 2"


def add_ten(my_string):
    print(int(my_string[my_string.find(":") + 2 :]) + 10)


add_ten(str_1)
add_ten(str_2)
add_ten(str_3)
add_ten(str_4)
