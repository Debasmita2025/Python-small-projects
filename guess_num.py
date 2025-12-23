import random
import os
from colorama import init, Fore, Back, Style  # pip install colorama

init()  # Initialize colorama for cross-platform support [web:31]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print(f"{Fore.CYAN}{Back.BLACK}🎯 GUESS THE NUMBER 🎯{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}🤞 Computer picks 1-100. Guess fast! Good luck! 🤞{Style.RESET_ALL}\n")
    
    while True:  # Replay loop
        difficulty = input(f"{Fore.GREEN}Choose: (e)asy(1-50)/ (n)ormal(1-100)/ (h)ard(1-200): {Style.RESET_ALL}").lower()
        if difficulty == 'e': range_end = 50
        elif difficulty == 'h': range_end = 200
        else: range_end = 100
        
        k = random.sample(range(1, range_end + 1), 1)
        c = 0
        max_attempts = 8 if range_end == 200 else 10
        
        print(f"{Fore.MAGENTA}Target: 1-{range_end} | Max: {max_attempts} tries{Style.RESET_ALL}\n")
        
        while c < max_attempts:
            try:
                n = int(input(f"{Fore.WHITE}Guess {c+1}/{max_attempts}: {Style.RESET_ALL}"))
                c += 1
                
                if k[0] > n:
                    print(f"{Fore.RED}📉 Too low!{Style.RESET_ALL}")
                elif k[0] < n:
                    print(f"{Fore.YELLOW}📈 Too high!{Style.RESET_ALL}")
                else:
                    print(f"\n{Fore.GREEN}🎉 Congrats! Got it in {c}/{max_attempts} attempts! 🎉{Style.RESET_ALL}")
                    break
                if c == max_attempts:
                    print(f"{Fore.RED}💀 Game Over! It was {k[0]}{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Enter a number!{Style.RESET_ALL}")
                c -= 1  # Don't count invalid inputs
        
        if input(f"\n{Fore.CYAN}Play again? (y/n): {Style.RESET_ALL}").lower() != 'y':
            print(f"{Fore.BLUE}Thanks for playing! 👋{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()
