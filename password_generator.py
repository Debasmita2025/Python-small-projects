import random
import string
from colorama import Fore

def generate_password(min_len, numbers = True, special_char = True):
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation

  characters =letters
  if numbers:
    characters += digits
  if special_char:
    characters += special
  
  pwd = ""
  meets_criteria = False
  has_num = False
  has_special = False

  while not meets_criteria or len(pwd) < min_len:
    new_char = random.choice(characters)
    pwd += new_char

    if new_char in digits:
      has_num = True
    elif new_char in special:
      has_special = True

    meets_criteria = True

    if numbers:
      meets_criteria = has_num
    if special_char:
      meets_criteria = meets_criteria and has_special

  return pwd



def main():
  min_len = int(input(f"{Fore.YELLOW}Enter the minimum length of the passord: "))
  has_num = input(f"{Fore.YELLOW}Do you want to include numbers(y/n): ").lower() == "y"
  has_special = input(f"{Fore.YELLOW}Do you want to include special char(y/n): ").lower() == "y"


  pwd = generate_password(min_len, has_num, has_special)
  print(f"{Fore.BLUE}Your generated password is {Fore.GREEN}{pwd}")


if __name__ == "__main__":
  main()