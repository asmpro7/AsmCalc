# AsmCalc Script
# made by asmpro
# date: 18/2/2023
# TG:@asmprotk

from math import sqrt
print("1:sum\t\t2:sub\n3:multi\t\t4:divide\n5:power\t\t6:cube\n7:sqroot\t8:number condition")
operator = input("choose the operation: ")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


def num_cond(num1, num2):
    if num1 == num2:
        return "first number equal second number"
    elif num1 > num2:
        return "first number bigger than second number"
    elif num1 < num2:
        return "second number bigger than first number"


def float_pow(num1, num2):
    result = pow(num1, num2)
    return f"{result:.2f}"


def float_sqrt(num1):
    result = sqrt(num1)
    return f"{result:.2f}"


if operator == "1":
    print(f"{num1 + num2:.2f}")
elif operator == "2":
    print(f"{num1 - num2:.2f}")
elif operator == "3":
    print(f"{num1 * num2:.2f}")
elif operator == "4":
    print(f"{num1 / num2:.2f}")
elif operator == "5":
    print(float_pow(num1, num2))
elif operator == "6":
    print(f"{num1 * num1 * num1:.2f}")
elif operator == "7":
    print(float_sqrt(num1))
elif operator == "8":
    print(num_cond(num1, num2))
else:
    print("Please select the number opposite the operation you want")
