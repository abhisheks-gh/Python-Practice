a = float(input())
oper = input()
b = float(input())

if oper == "+":
    result = a + b
elif oper == "-":
    result = a - b
elif oper == "*":
    result = a * b
elif oper == "/":
    result = a / b
else:
    print("Invalid operator")

print(result)