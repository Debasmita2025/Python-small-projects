from colorama import init, Fore, Back, Style
import os
import random 


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1 

ROWS = 3
COLS = 3

symbol_count = {
  "A": 2, 
  "B": 4, 
  "C": 6, 
  "D": 8
}

symbol_value = {
  "A": 5, 
  "B": 4, 
  "C": 3, 
  "D": 2
}


init()

def check_winnings(cols, lines, bet, vals):
  win = 0
  win_lines = []
  for line in range(lines):
    sym = cols[0][line]
    for column in cols:
      sym_to_check = column[line]
      if sym != sym_to_check:
        break
    else:
      win += vals[sym] * bet
      win_lines.append(line+1)
  
  return win, win_lines


def get_slot_machine_spin(r, c, sym):
  all_sym = []
  for syms, symbol_count in sym.items():
    for _ in range(symbol_count):
      all_sym.append(syms)

  columns = []
  for _ in range(c):
    column = []
    cur_sym = all_sym[:]
    for _ in range(r):
      val = random.choice(cur_sym)
      cur_sym.remove(val)
      column.append(val)
    columns.append(column)

  return columns


def print_slot_machine(cols):
  for row in range(len(cols[0])):
    for i, column in enumerate(cols):
      if i != len(cols) - 1:
        print(f"{Fore.CYAN}{column[row]}", end=" | ")
      else:
        print(f"{Fore.CYAN}{column[row]}")



def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
 
def deposit():
  while True:
    amt = input(f"{Fore.YELLOW}What would you like to deposit? $")
    
    if amt.isdigit():
      amt = int(amt)
      if amt > 0:
        break
      else:
        print(f"{Fore.RED}Amount must be greater than 0")
    else:
      print(f"{Fore.LIGHTYELLOW_EX}please enter a number")

  return amt

def get_number_line():
  while True:
    lines = input(f"{Fore.YELLOW}Enter the lines to bet on(1 - {MAX_LINES}): ")
    
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print(f"{Fore.RED}Enter valid number of lines")
    else:
      print(f"{Fore.LIGHTYELLOW_EX}Please enter a number")

  return lines

def get_bet():
  while True:
    amt = input(f"{Fore.YELLOW}What would you like to bet on each lines? $")
    
    if amt.isdigit():
      amt = int(amt)
      if MIN_BET <= amt <= MAX_BET:
        break
      else:
        print(f"{Fore.RED}Amount must be in between {MIN_BET} and {MAX_BET}")
    else:
      print(f"{Fore.LIGHTYELLOW_EX}please enter a number")

  return amt

def spin(bal):
  lines = get_number_line()
  while True:
      bet = get_bet()
      t_bet = lines * bet
      if t_bet > bal:
          print(f"{Fore.RED}Insufficient funds (${bal})")
          continue
      break
  
  print(f"{Fore.BLUE}Balance: ${bal} | Lines: {lines} | Bet: ${bet} | Total: ${t_bet}")
  
  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  
  win, win_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f"{Fore.GREEN}You won ${win}! Lines: {win_lines}{Style.RESET_ALL}")
  
  new_balance = bal - t_bet + win
  print(f"{Fore.YELLOW}New balance: ${new_balance}{Style.RESET_ALL}")
  return new_balance


def main():
  clear_screen()
  print(f"{Fore.CYAN}🎰 CASINO SLOT MACHINE 🎰{Style.RESET_ALL}")
  bal = deposit()
  
  while True:
    clear_screen()
    print(f"{Fore.LIGHTBLUE_EX}💰 Balance: ${bal}{Style.RESET_ALL}")
    ans = input("Press 's' to SPIN (q to quit): ").lower()
    
    if ans == 'q':
      print(f"{Fore.YELLOW}Thanks for playing! Final balance: ${bal}{Style.RESET_ALL}")
      break
    
    if ans == 's':
      bal = spin(bal)
      if bal <= 0:
          print(f"{Fore.RED}Game Over - Out of money!{Style.RESET_ALL}")
          break
    input(f"{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

  


if __name__ == "__main__":
  main()
