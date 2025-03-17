import re

date1 = "2023-12-12"
date2 = "23-12-12"
date3 = "2024-2-12"

def checkdate(date):
    pattern = "[0-9]{4}-[0-9]{2}-[0-9]{2}"
    result = re.findall(pattern, date)
    if len(result) == 1:
        return True
    else:
        return False

print(checkdate(date1))
print(checkdate(date2))
print(checkdate(date3))
