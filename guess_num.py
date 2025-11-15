import random
print("Guess the number...")

k = random.sample(range(1,101), 1)
c = 0

while True:
  n = int(input("Enter a number between 1-100 : "))
  c+=1
  if k[0] > n:
    print("It's low try again!")
  elif k[0] < n:
    print("It's high try again!")
  else:
    print(f"Congrats you've got it rigth in {c} attemps")
    break