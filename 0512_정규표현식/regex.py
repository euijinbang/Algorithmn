import re

data = ["euijin.bang@gmail.com", "ej.bb@@gmail.com", "euijin@gmail.com", "euijin123naver.com"]
mail = re.compile(r"(\w+\.)*\w+@(\w+\.)+[A-Za-z]+")
result = []
for d in data:
    if mail.match(d):
        result.append(d)
print(result)

print('-'*100)


p = re.compile(r"\d{3}")

# 1. match
# returns the substring that was matched by the RE
m = p.match("123456")
print(m.group())
print(m.start(), m.end())
print(m.span())

print('-'*100)


# 2. search
# Scan through a string, looking for any location where this RE matches.
m1 = p.search("123456")
print(m1.group())

print('-'*100)


# 3. findall
# Find all substrings where the RE matches, and returns them as a list.
m2 = p.findall("123456")
print(m2)

print('-'*100)


# 4. finditer
# Find all substrings where the RE matches, and returns them as an iterator.
m3 = p.finditer("123456")
for mm in m3:
    print(mm.group())



