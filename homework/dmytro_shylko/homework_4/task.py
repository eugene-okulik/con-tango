"""Module providing a function printing python version."""

my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": [10, 20, 30, 40, 50],
    "dict": {1: "apple", 2: "pea", 3: "plum", 4: "melon", 5: "grape"},
    "set": {100, 200, 300, 400, 500},
}

print(my_dict["tuple"][-1])

my_dict["list"].append(60)
my_dict["list"].pop(1)

my_dict["dict"][('i am a tuple',)] = ("orange", "apricot")
my_dict["dict"].pop(3)

my_dict["set"].add(444)
my_dict["set"].remove(300)

print(my_dict)
