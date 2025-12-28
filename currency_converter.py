import requests
import json
from colorama import init, Fore, Style
import os

init()
HISTORY_FILE = r"E:\Codes and data\Python Vs code\Projects\currency_history.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history[-10:], f, indent=2)  # Last 10 conversions

def get_rates(base_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except:
        return None

def currency_converter():
    clear_screen()
    print(f"{Fore.CYAN}💱 CURRENCY CONVERTER PRO 💱{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Supported: USD, EUR, INR, GBP, JPY, AUD, CAD, CHF{Style.RESET_ALL}")
    
    print(f"\n{Fore.GREEN}🔥 POPULAR:{Style.RESET_ALL}")
    print("1. USD → INR  2. EUR → USD  3. INR → USD")
    
    base_currency = input(f"\n{Fore.YELLOW}Base currency: {Style.RESET_ALL}").upper().strip()
    target_currency = input(f"{Fore.YELLOW}Target currency: {Style.RESET_ALL}").upper().strip()
    amount = float(input(f"{Fore.YELLOW}Amount: {Style.RESET_ALL}"))
    
    rates = get_rates(base_currency)
    if not rates or "rates" not in rates:
        print(f"{Fore.RED}❌ Invalid currency or API error{Style.RESET_ALL}")
        return
    
    if target_currency in rates["rates"]:
        rate = rates["rates"][target_currency]
        converted = amount * rate
        
        print(f"\n{Fore.GREEN}💰 RESULT{Style.RESET_ALL}")
        print(f"{Fore.CYAN}1 {base_currency} = {rate:.4f} {target_currency}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}💱 {amount:,.2f} {base_currency} = {converted:,.2f} {target_currency}{Style.RESET_ALL}")
        
        history = load_history()
        history.append({
            "base": base_currency, "target": target_currency, 
            "amount": amount, "converted": converted, "rate": rate,
            "date": os.popen('date').read().strip()
        })
        save_history(history)
        
    else:
        print(f"{Fore.RED}❌ {target_currency} not supported{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Available: {', '.join(list(rates['rates'].keys())[:10])}...{Style.RESET_ALL}")

def show_history():
    history = load_history()
    if not history:
        print(f"{Fore.YELLOW}No conversions yet!{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.CYAN}📜 RECENT CONVERSIONS (Last 5){Style.RESET_ALL}")
    for i, conv in enumerate(history[-5:], 1):
        print(f"{i}. {conv['amount']:.0f} {conv['base']} → {conv['converted']:.0f} {conv['target']} | {conv['date']}")

def main():
    while True:
        clear_screen()
        print(f"{Fore.CYAN}{'='*40}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}🌍 CURRENCY CONVERTER PRO 🌍{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*40}{Style.RESET_ALL}")
        print("1. 💱 Convert Currency")
        print("2. 📜 View History") 
        print("3. ❌ Exit")
        
        choice = input(f"\n{Fore.YELLOW}Choose (1-3): {Style.RESET_ALL}").strip()
        
        if choice == "1":
            currency_converter()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print(f"{Fore.BLUE}👋 Thanks for using Currency Converter!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")
        
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
