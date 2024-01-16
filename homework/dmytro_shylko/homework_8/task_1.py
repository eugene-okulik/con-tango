import random

salary = int(input("Enter your salary: "))
bonus = random.choice([True, False])
random_bonus = int(random.random() * 100)

if bonus:
    final_salary = salary + random_bonus
else:
    final_salary = salary

print(f"{salary}, {bonus} - '${final_salary}'")
