# pylint: disable=missing-module-docstring

temperatures = [
    20,
    15,
    32,
    34,
    21,
    19,
    25,
    27,
    30,
    32,
    34,
    30,
    29,
    25,
    27,
    22,
    22,
    23,
    25,
    29,
    29,
    31,
    33,
    31,
    30,
    32,
    30,
    28,
    24,
    23,
]

hot_temperatures = filter(lambda x: x > 28, temperatures)

# print(hot_temperatures)
hots_list = list(hot_temperatures)

print(max(hots_list))
print(min(hots_list))
print(round(sum(hots_list) / len(hots_list)))
