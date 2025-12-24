import random
import json
import time
import os
from colorama import init, Fore, Back, Style  # pip install colorama

init()
FILENAME = r"E:\Codes and data\Python Vs code\Projects\quiz_question.json"
HIGHSCORE_FILE = r"E:\Codes and data\Python Vs code\Projects\highscore.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_questions():
    with open(FILENAME, "r") as f:
        return json.load(f)

def save_highscore(name, score, total):
    data = {"name": name, "score": score, "total": total, "date": time.strftime("%Y-%m-%d")}
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = []
    scores.append(data)
    scores.sort(key=lambda x: x["score"] / x["total"], reverse=True)
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump(scores[:5], f, indent=2)  # Top 5

def load_highscores():
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def main():
    clear_screen()
    print(f"{Fore.CYAN}{Back.BLACK}📚 QUIZ MASTER CHALLENGE 📚{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Sharpen your knowledge! Write 'EXIT' to quit.{Style.RESET_ALL}\n")
    
    while True:
        mode = input(f"{Fore.GREEN}Choose: (e)asy(10Q)/ (n)ormal(20Q)/ (h)ard(all): {Style.RESET_ALL}").lower()
        if mode == 'e': num_questions = 10
        elif mode == 'h': num_questions = None
        else: num_questions = 20
        
        questions = load_questions()
        random.shuffle(questions)
        questions = questions[:num_questions] if num_questions else questions
        
        c = 0
        TIME_LIMIT = 15  # seconds per question
        
        clear_screen()
        print(f"{Fore.MAGENTA}🎯 Mode: {'Easy' if mode=='e' else 'Normal' if mode=='n' else 'Hard'} | Questions: {len(questions)} | Time: {TIME_LIMIT}s{Style.RESET_ALL}\n")
        
        for i, q in enumerate(questions, 1):
            print(f"{Fore.WHITE}Q{i}: {q['question']}{Style.RESET_ALL}")
            for opt in q["options"]:
                print(f"  {Fore.CYAN}{opt}{Style.RESET_ALL}")
            
            start_time = time.time()
            a = input(f"{Fore.YELLOW}Answer (A/B/C/D): {Style.RESET_ALL}").upper().strip()
            
            if a == "EXIT":
                print(f"{Fore.RED}Quiz ended early.{Style.RESET_ALL}")
                break
            
            time_taken = time.time() - start_time
            
            if time_taken > TIME_LIMIT:
                print(f"{Fore.RED}⏰ Time's Up! ({time_taken:.1f}s) Correct: {q['answer']}{Style.RESET_ALL}\n")
                continue
            
            if a == q["answer"]:
                c += 1
                print(f"{Fore.GREEN}✅ Correct! (+{100//len(questions)} pts){Style.RESET_ALL}\n")
            else:
                print(f"{Fore.RED}❌ Wrong! Correct: {q['answer']}{Style.RESET_ALL}\n")
        
        score_pct = (c / len(questions)) * 100
        print(f"{Fore.CYAN}🏆 FINAL SCORE: {c}/{len(questions)} ({score_pct:.1f}%){Style.RESET_ALL}")
        
        # High score check
        highscores = load_highscores()
        if highscores and score_pct > (highscores[0]["score"] / highscores[0]["total"] * 100):
            name = input(f"{Fore.YELLOW}New High Score! Enter name: {Style.RESET_ALL}")
            save_highscore(name, c, len(questions))
            print(f"{Fore.GREEN}🎉 High score saved!{Style.RESET_ALL}")
        
        if input(f"\n{Fore.BLUE}Play again? (y/n): {Style.RESET_ALL}").lower() != 'y':
            print(f"{Fore.BLUE}Thanks for playing! 👋{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()
