import turtle
import time
import random

WIDTH, HEIGHT = 800, 500
COLORS = ['red', 'orange', 'yellow', 'green', 'cyan',
          'blue', 'purple', 'pink', 'black', 'brown']

def get_number_of_racers():
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Number not in range 2–10. Try again!")
        else:
            print("Input is not numeric. Try again!")

def init_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("🏁 Turtle Racing Game 🏁")
    screen.bgcolor("lightgrey")
    return screen

def draw_finish_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.speed(0)
    line.penup()

    y = HEIGHT // 2 - 30
    line.goto(-WIDTH // 2 + 20, y)
    line.pendown()
    line.color("black")
    line.pensize(3)
    line.forward(WIDTH - 40)              # horizontal line across the track

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.shapesize(1.5)
        racer.left(90)
        racer.penup()
        start_x = -WIDTH // 2 + (i + 1) * spacingx
        start_y = -HEIGHT // 2 + 40
        racer.goto(start_x, start_y)
        racer.pendown()
        turtles.append(racer)
    return turtles

def countdown():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(0, HEIGHT // 2 - 90)
    pen.color("black")
    for num in ["3", "2", "1", "GO!"]:
        pen.clear()
        pen.write(num, align="center", font=("Arial", 32, "bold"))
        time.sleep(0.7)
    pen.clear()

def race(colors):
    turtles = create_turtles(colors)
    finish_y = HEIGHT // 2 - 30

    while True:
        for racer in turtles:
            dist = random.randint(1, 20)
            racer.forward(dist)
            _, y = racer.pos()
            if y >= finish_y:
                winner_color = racer.pencolor()
                highlight_winner(racer)
                return winner_color

def highlight_winner(racer):
    racer.shapesize(2.5)
    racer.pensize(5)
    for _ in range(10):
        racer.right(36)

def main():
    while True:
        racers = get_number_of_racers()
        screen = init_screen()
        draw_finish_line()
        random.shuffle(COLORS)
        colors = COLORS[:racers]

        countdown()
        winner = race(colors)
        print(f"Hurray! {winner.upper()} turtle is the winner 🏆")

        msg = turtle.Turtle()
        msg.hideturtle()
        msg.penup()
        msg.goto(0, 0)
        msg.write(f"{winner.upper()} WINS! 🏆",
                  align="center", font=("Arial", 24, "bold"))

        again = screen.textinput("Play again?", "Run another race? (y/n): ")
        if not again or again.lower() != "y":
            break
        turtle.clearscreen()

    turtle.bye()

if __name__ == "__main__":
    main()
