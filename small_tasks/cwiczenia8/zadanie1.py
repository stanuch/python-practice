import re

alfabet = {"a", "b", "c", "d", "e", "f"}
ciągi = ("abcddddddff acdeeddedddeff aceedeff abbceeddeeddff abbbbceeeeeeff")

pattern = "ab*c[de]*ff"

result = re.findall(pattern, ciągi)

print(result)