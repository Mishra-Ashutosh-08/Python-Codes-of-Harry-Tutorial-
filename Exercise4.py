# Pattern Printing
# Input =Interger n
# Boolean = True or False
# n = number of rows
# True n=4
# *
# **
# ***
# ****
# False n=4
# ****
# ***
# **
# *

print("Pattern printing")
num = int(input("Enter the number of rows\n"))
print("Enter 0 or 1")
bool = input("1 for True or 0 for False\n")
print("The star pattern is")
if bool == "1":
    for i in range(1,num+1):
        print("*"*i)
elif bool == "0":
    for i in range(num,0,-1):
        print("*"*i)