import json
import os

FILENAME = r"E:\Codes and data\Python Vs code\Projects\expense-Tracker.json"

if os.path.exists(FILENAME):
  with open(FILENAME, "r") as f:
    tasks = json.load(f)
else:
  tasks = []

while True:
  total = 0
  print("\n---Expense Tracker---")
  print("1. Add Expenses")
  print("2. View expenses")
  print("3. Exit")
  c=int(input("Give your choice(1-3): "))

  if c == 1:
    category = input("Category: ")
    desc = input("Description: ")
    amt = int(input("Amount: "))
    tasks.append({"Category": category,"Description": desc, "Amount": amt})
    print("Expenses are added.")
  
  elif c == 2:
    if not tasks:
      print("No Expenses yet...")
    else:
      print("--Your Expenses--")

      for key, val in enumerate(tasks, start=1):
        print(f"{key}. Category: {val["Category"]}\n   Description: {val["Description"]}\n   Amount: {val["Amount"]}")
        total += val["Amount"]
        print(f"The total expense is: {total}")
  
  elif c == 3:
    print("Control your expenses wisely. Bye!")
    break

  else:
    print("Invalid choice, choose again...")

with open(FILENAME, "w") as f:
  json.dump(tasks, f, indent=4)
