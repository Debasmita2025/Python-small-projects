from colorama import Fore
import random

CONS = ["B", "Y", "R", "G", "O", "W"]

def generate_code():
  return random.choices(CONS, k=4)

def get_feedback(secret, guess):
  correct_pos = sum(1 for i in range(4) if guess[i] == secret[i])
  
  total_matches = sum(min(guess.count(c), secret.count(c)) for c in set(guess + secret))
  incorrect_pos = total_matches - correct_pos
  
  return correct_pos, incorrect_pos

def play_game():
  secret = generate_code()
  attempts = 10 
  
  print(f"{Fore.YELLOW}Welcome to mastermind. Attempt to guess the 4 digit code... You have 10 tries.{Fore.RESET}")
  print(f"{Fore.WHITE}The colors that could make: {' '.join(CONS)}{Fore.RESET}")
  
  for attempt in range(1, attempts + 1):
    print(f"{Fore.WHITE}Guess (space separated): {Fore.RESET}", end="")
    while True:
      guess_input = input().strip().upper().split()
      if len(guess_input) == 4 and all(c in CONS for c in guess_input):
          guess = guess_input
          break
      print(f"{Fore.RED}Invalid input!{Fore.RESET}")
    
    correct_pos, incorrect_pos = get_feedback(secret, guess)
    print(f"Correct Position: {correct_pos} | Incorrect Position: {incorrect_pos}")
    
    if correct_pos == 4:
      print(f"{Fore.GREEN}You guessed the code in {attempt} tries{Fore.RESET}, Hurray!")
      return
  
  print(f"{Fore.RED}Game Over! Secret was: {' '.join(secret)}{Fore.RESET}")

if __name__ == "__main__":
    play_game()
