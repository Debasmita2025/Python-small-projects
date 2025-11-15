print("---BASIC CALCULATOR---")
a = int(input("Num1: "))
s = input("Action: ")
b = int(input("Num2: "))
if s == '+':
  print(f"{a} {s} {b} = {a+b}")
elif s == '-':
  print(f"{a} {s} {b} = {a-b}")
elif s == '*':
  print(f"{a} {s} {b} = {a*b}")
elif s == '/':
  print(f"{a} {s} {b} = {a/b}")
else:
  print("Invalid Syntax")
