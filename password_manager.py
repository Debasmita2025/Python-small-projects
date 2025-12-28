from colorama import init, Fore, Back, Style 
import os
from cryptography.fernet import Fernet

init()

def write_key():
  key = Fernet.generate_key()
  with open(r"E:\Codes and data\Python Vs code\Projects\key.key", 'wb') as key_file:
    key_file.write(key)

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def view():
  with open(r'E:\Codes and data\Python Vs code\Projects\passwords.txt', 'r') as f:
    for line in f.readlines():
      data = line.rstrip()
      name, psd = data.split("|")
      print(f"name: {name} and pwd: {psd}")


def add():
  nm = input(f"{Fore.BLUE}Account name: ")
  pwd = input(f"{Fore.BLUE}Password: ")

  with open(r"E:\Codes and data\Python Vs code\Projects\passwords.txt", 'a') as f:
    f.write(nm + "|" + pwd + "\n")

def main():
  clear_screen()
  mas_pwd = input(f"{Fore.CYAN}Enter the master password: ")

  write_key()

  while True:
    mode = int(input(f"{Fore.YELLOW}1. Add New Password\n2.View Existing Password\n3.Quit\nEnter your choice(1 or 2 or 3):  "))

    if mode == 3:
       break

    if mode == 2:
      view()
      break
    elif mode == 1:
      add()
      break
    else:
      print(f"{Fore.RED}Invalid mode!")

if __name__ == "__main__":
    main()