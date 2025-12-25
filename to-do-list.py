import json
import os
from datetime import datetime
from colorama import init, Fore, Style

init()
FILENAME = r"E:\Codes and data\Python Vs code\Projects\to-do-list.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

def print_tasks(tasks):
    if not tasks:
        print(f"{Fore.YELLOW}📭 No tasks yet!{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.CYAN}📋 YOUR TASKS ({len(tasks)} total){Style.RESET_ALL}")
    pending = sum(1 for t in tasks if not t["done"])
    print(f"{Fore.YELLOW}⏳ Pending: {pending} | ✅ Done: {len(tasks)-pending}{Style.RESET_ALL}")
    
    for i, task in enumerate(tasks, 1):
        status = f"{Fore.GREEN}✅{Style.RESET_ALL}" if task["done"] else f"{Fore.RED}⏳{Style.RESET_ALL}"
        priority = f" {Fore.RED}[HIGH]{Style.RESET_ALL}" if task.get("priority") == "high" else ""
        due = f" | {Fore.MAGENTA}Due: {task.get('due', 'None')}{Style.RESET_ALL}" if task.get("due") else ""
        
        print(f"{Fore.BLUE}{i:2d}.{Style.RESET_ALL} {status} {task['task']}{priority}{due}")

def add_task(tasks):
    task = input(f"{Fore.YELLOW}Enter task: {Style.RESET_ALL}").strip()
    if not task:
        print(f"{Fore.RED}Task cannot be empty!{Style.RESET_ALL}")
        return
    
    priority = input(f"{Fore.YELLOW}Priority (h=high/n=normal): {Style.RESET_ALL}").lower().strip()
    priority = "high" if priority == 'h' else "normal"
    
    due = input(f"{Fore.YELLOW}Due date (YYYY-MM-DD or Enter to skip): {Style.RESET_ALL}").strip()
    
    tasks.append({
        "task": task,
        "done": False,
        "priority": priority,
        "due": due if due else None,
        "created": datetime.now().strftime("%Y-%m-%d")
    })
    print(f"{Fore.GREEN}✅ Task added!{Style.RESET_ALL}")

def mark_done(tasks):
    if not tasks:
        print(f"{Fore.RED}No tasks!{Style.RESET_ALL}")
        return
    
    print_tasks(tasks)
    try:
        num = int(input(f"{Fore.YELLOW}Task number to mark done: {Style.RESET_ALL}"))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print(f"{Fore.GREEN}✅ Task marked done!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid number!{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Enter a valid number!{Style.RESET_ALL}")

def delete_task(tasks):
    if not tasks:
        print(f"{Fore.RED}No tasks!{Style.RESET_ALL}")
        return
    
    print_tasks(tasks)
    try:
        num = int(input(f"{Fore.YELLOW}Task number to delete: {Style.RESET_ALL}"))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"{Fore.GREEN}🗑️ '{removed['task']}' deleted!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid number!{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Enter a valid number!{Style.RESET_ALL}")

def search_tasks(tasks):
    query = input(f"{Fore.YELLOW}Search tasks: {Style.RESET_ALL}").lower().strip()
    if not query:
        return
    
    matches = [t for t in tasks if query in t["task"].lower()]
    if matches:
        print(f"\n{Fore.CYAN}🔍 SEARCH RESULTS ({len(matches)}){Style.RESET_ALL}")
        for i, task in enumerate(matches, 1):
            status = f"{Fore.GREEN}✅{Style.RESET_ALL}" if task["done"] else f"{Fore.RED}⏳{Style.RESET_ALL}"
            print(f"{i}. {status} {task['task']}")
    else:
        print(f"{Fore.YELLOW}No matching tasks{Style.RESET_ALL}")

def main():
    tasks = load_tasks()
    
    while True:
        clear_screen()
        print(f"{Fore.CYAN}{'='*40}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}📝 SMART TO-DO LIST 📝{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*40}{Style.RESET_ALL}")
        print("1. ➕ Add Task")
        print("2. 📋 View All")
        print("3. ✅ Mark Done")
        print("4. 🗑️ Delete Task")
        print("5. 🔍 Search")
        print("6. ❌ Exit")
        
        choice = input(f"\n{Fore.YELLOW}Choose (1-6): {Style.RESET_ALL}").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            print_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            search_tasks(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print(f"{Fore.BLUE}💾 Tasks saved! Goodbye 👋{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}❌ Invalid choice (1-6)!{Style.RESET_ALL}")
        
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
