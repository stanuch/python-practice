import re

txt = "kot 123-435-265 kanarek +48-654-235-542 rybki 321 432 543"

pattern = "\+48-[0-9]{3}-[0-9]{3}-[0-9]{3}|[0-9]{3}[ -][0-9]{3}[ -][0-9]{3}"

result = re.findall(pattern, txt)

print(result)