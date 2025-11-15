import random
import json
import time

FILENAME = r"C:\Users\darke\OneDrive\Desktop\Python Vs code\Projects\quiz_question.json"
with open(FILENAME,"r") as f:
  question = json.load(f)

random.shuffle(question)
TIME_TAKEN = 10;

print("📚WELCOME TO THE QUIZ GAME📚")
print("Answer the following question:-")
print("\nWrite 'EXIT' to exit the game\n")
c = 0
for key, val in enumerate(question, start=1):
  print(f"{key}. {val['question']}")
  for op in val["options"]:
    print(op)
  start_time = time.time()
  a = input("Enter answer: ").upper()
  end_time = time.time()

  if a == "EXIT":
    break
  
  time_taken = end_time - start_time
  if time_taken > TIME_TAKEN:
    print(f"Time's Up ⏳, you've taken {time_taken:.2f} seconds")
    print(f"⏳ Correct answer is {val['answer']}.\n")
    continue
  
  if val["answer"] == a:
    c+=1
    print("✅Correct answer.\n")
  else:
    print(f"❌ Wrong answer. Correct answer is {val['answer']}.\n")
  

print(f"Your final score is: {c}/{len(question)}")