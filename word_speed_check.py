import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

FILENAME = r"E:\Codes and data\Python Vs code\Projects\word_speed_sentences.txt"

def load_text():
    with open(FILENAME, "r", encoding="utf-8") as f:
        return random.choice([line.strip() for line in f if line.strip()])

def colored_diff(target, typed):
    
    out = []
    for i in range(max(len(target), len(typed))):
        t_char = target[i] if i < len(target) else ""
        u_char = typed[i] if i < len(typed) else ""

        if u_char == "":
            out.append(Fore.YELLOW + t_char)
        elif t_char == "":
            out.append(Fore.RED + u_char)
        elif u_char == t_char:
            out.append(Fore.GREEN + u_char)
        else:
            out.append(Fore.RED + u_char)
    return "".join(out) + Style.RESET_ALL

def typing_test():
    target = load_text()
    print(Fore.CYAN + "\nWelcome to the Speed Typing Test!" + Style.RESET_ALL)
    print("\nType this sentence:\n")
    print(Fore.YELLOW + target + Style.RESET_ALL)
    input("\nPress Enter when you are ready...")

    start = time.time()
    typed = input("\nStart typing:\n")
    end = time.time()

    elapsed = max(end - start, 1e-6)
    wpm = round((len(typed) / 5) / (elapsed / 60))

    correct = sum(1 for a, b in zip(target, typed) if a == b)
    accuracy = (correct / len(target)) * 100 if target else 0

    print("\n" + Fore.MAGENTA + "=== RESULTS ===" + Style.RESET_ALL)
    print(f"Time     : {elapsed:.2f} s")
    print(f"WPM      : {Fore.GREEN}{wpm}{Style.RESET_ALL}")
    print(f"Accuracy : {Fore.GREEN if accuracy>=90 else Fore.RED}{accuracy:.1f}%{Style.RESET_ALL}")

    print("\nYour typing vs target:")
    print(colored_diff(target, typed))

if __name__ == "__main__":
    while True:
        typing_test()
        again = input("\nRun again? (y/n): ").lower()
        if again != "y":
            print(Fore.CYAN + "Goodbye!" + Style.RESET_ALL)
            break
