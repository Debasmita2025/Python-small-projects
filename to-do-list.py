import json
import os
FILENAME = r"E:\Codes and data\Python Vs code\Projects\to-do-list.json"
if os.path.exists(FILENAME):
  with open(FILENAME, "r") as f:
    tasks = json.load(f)
else:
  tasks = []

while True:
  print("---TO-DO-LIST---")
  print("1. Add Task")
  print("2. View Task")
  print("3. Mark as done")
  print("4. Delete Task")
  print("5. Exit")

  c = input("Enter your choice: ")

  if c == '1':
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")
  
  elif c == '2':
    if not tasks:
      print("No task to show")
    else:
      print("\nTasks:")
      for i, t in enumerate(tasks, start=1):
        status = "✅ Done" if t["done"] else "⏳ Pending"
        print(f"{i}. {t['task']} - {status}")
  
  elif c == '3':
    if not tasks:
      print("No tasks to mark!")
    else:
      num = int(input("Enter task number to mark as done: "))
      if 1 <= num <= len(tasks):
        tasks[num - 1]["done"] = True
        print("Task marked as done!")
      else:
        print("Invalid task number.")
  
  elif c == '4':
    if not task:
      print("No task to delete.")
    else:
      num = int(input("Enter task number to delete: "))
      if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("Task is deleted.")
      else:
        print("Invalid task number.")
  
  elif c == '5':
    print("Goodbye, See you later")
    break

  else:
    print("Invalid choice, choice between 1 to 5")


with open(FILENAME, "w") as f:
  json.dump(tasks, f, indent=4)