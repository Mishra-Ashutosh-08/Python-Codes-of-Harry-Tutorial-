# Age and Drive relation

print("What is your age?")
age = int(input())
if 6 < age < 18:
    print("You can not drive")
elif age == 18:
    print("We will think about you")
elif 18 < age < 80:
    print("You can drive")
else:
    print("You gave a invalid age")