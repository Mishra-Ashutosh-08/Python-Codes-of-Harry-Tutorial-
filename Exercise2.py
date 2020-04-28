# Faulty Calculator
# Design a calculator which will correctly solve all the problems except the following ones
# 45 * 3 = 555 , 56 + 9 = 77 , 56 / 6 = 4

print("Enter 1st number")
num1 = int(input())
print("Enter 2nd number")
num2 = int(input())
print("Enter your choice (+,-,*,/,%)")
op = input()
if num1 == 45 and num2 == 3 and op == '*':
    print('555')
elif num1 == 56 and num2 == 9 and op == '+':
    print('77')
elif num1 == 56 and num2 == 6 and op == '/':
    print('4')
elif op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
elif op == '%':
    print(num1%num2)
else:
    print("Error! Please check your input.")