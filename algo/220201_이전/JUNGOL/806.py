gender, age = input().split()

age = int(age)

if gender == "M":
    if age >= 18:
        print("MAN")
    else:
        print("BOY")
else:
    if age >= 18:
        print("WOMAN")
    else:
        print("GIRL")