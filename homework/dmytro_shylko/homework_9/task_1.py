# pylint: disable=missing-module-docstring

import datetime

my_time = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(my_time, "%b %d, %Y - %H:%M:%S")
month = python_date.strftime("%B")

print(month)

new_format_date = python_date.strftime("%d.%m.%Y, %H:%M")
print(new_format_date)
