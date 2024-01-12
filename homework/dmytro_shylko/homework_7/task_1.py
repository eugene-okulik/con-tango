a = 5

guess = int(input("Enter number: "))

while guess != a:
    print("попробуйте снова")
    guess = int(input("Enter number: "))
    if guess == a:
        print("Поздравляю! Вы угадали!")
