from tkinter import *
import random



root = Tk()
root.title("Number guessing game")
root.configure(bg="#262626")
root.geometry("850x750")
root.iconbitmap("01.ico")

    
def gameover():
    root.configure(bg="black")
    gg2 = Label(root, text="Game Over", fg="red", bg="black", font=("Comic Sans MS", 75))
    gg = Label(root, text="You lost", fg="red", bg="black", font=("Comic Sans MS", 50))
    def quitting():
        gg2.destroy()
        gg.destroy()
        returnbutton.destroy()
        rage_quit.destroy()
        imagine = Label(root, text="imagine rage quitting lol", bg="black", fg="blue", font=("Comic Sans MS", 20))
        imagine.place(x=50, y=300)
        root.after(1000, lambda:imagine.config(text="ez noob loser"))
        root.after(2000, lambda:imagine.config(text="can't win a number guessing game ? 😂"))
        root.after(5000, lambda:imagine.config(text="made by yassen cuz his better than u haha"))
        root.after(6000, lambda:root.destroy())
    rage_quit = Button(root, text="Quit", bg="black", fg="white", font=("Comic Sans MS", 20), command=quitting)
    gg2.place(x=175, y=150)
    gg.place(x=300, y=300)
    rage_quit.place(x=250, y=600)
    def returning():
        gg.destroy()
        gg2.destroy()
        returnbutton.destroy()
        quit_game.destroy()
        rage_quit.destroy()
        menu()
    returnbutton = Button(root, text="Return to main menu", bg="black", fg="white", font=("Comic sans", 20), command=returning)
    returnbutton.place(x=450, y=600)
    

def easy():
    menuclear()
    root.configure(bg="#1fba00")
    root.title("Number guessing game | Easy level 1")
    number = random.randint(1,10)
    attempts = 8
    
    
    def clear():
        easy_explain.destroy()
        easy_explain2.destroy()
        easy_explain3.destroy()
        easy_explain4.destroy()
        easy_explain5.destroy()
        guess_input.destroy()
        guess_check.destroy()
        attempts_left.destroy()
    
    easy_explain = Label(root, text="Welcome to easy difficulty", bg="black", fg="white", font=("Segoe Print", 15))
    easy_explain2 = Label(root, text="A random number was generated ranged from 1 to 10", bg="black", fg="white", font=("Segoe Print", 15))
    easy_explain3 = Label(root, text="You have 8 attempts to guess that number", bg="black", fg="white", font=("Segoe Print", 15))
    easy_explain4 = Label(root, text="If you guess the number incorrectly 8 times you lose", bg="black", fg="white", font=("Segoe Print", 15))
    easy_explain5 = Label(root, text="But if you manage to guess it correctly in 8 attempts or less you complete the level", bg="black", fg="white", font=("Segoe Print", 15))
    guess_input = Entry(root, font=("Segoe Print", 15))
    attempts_left = Label(root, text=f"Attempts left : {attempts}", fg="blue", bg="#1fba00", font=("Comic Sans MS", 20))
     

    def check(): #checks the guessed number
        guess = int(guess_input.get())
        if guess == number: #checks if the guess is correct
            clear()
            easy2()
        else: #now its confirmed the guess was incorrect because there can't be other possibilities
            nonlocal attempts
            attempts = attempts - 1
            attempts_left.config(text=f"Attempts left : {attempts}")
            if attempts == 0: #checks if that was your last attempt
                clear()
                gameover()
            else: #now its confirmed you still have attempts left
                if guess > number: #checks if the guess was bigger than the correct number so we can make sure the hint is correct
                    hint = "Lower"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#1fba00", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

                elif guess < number: #checks if the guess was less than the correct number so we can make sure the hint is correct
                    hint = "Higher"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#1fba00", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())
            
    guess_check = Button(root, text="Guess", bg="#00b3ff", font=("Segoe Print", 15), command=check) #checks your guess weither its the correct answer or incorrect
    guess_check.place(x=650, y=310)
    easy_explain.place(x=300, y=0)
    easy_explain2.place(x=160, y=40)
    easy_explain3.place(x=200, y=80)
    easy_explain4.place(x=175, y=120)
    easy_explain5.place(x=1, y=160)
    guess_input.place(x=300, y=320)
    attempts_left.place(x=330, y=400)



def easy2(): 
    root.configure(bg="#189100")
    root.title("Number guessing game | Easy level 2")
    attempts = 6
    number = random.randint(1,10)


    def clear():
        guess_check.destroy()
        guess_input.destroy()
        easy_explain.destroy()
        easy_explain2.destroy()
        easy_explain3.destroy()
        attempts_left.destroy()
    easy_explain = Label(root, text="Congrats ! you beat the first level", bg="black", fg="white", font=("Segoe Print", 15))
    easy_explain2 = Label(root, text="Welcome to level 2, this time you only have 6 attempts", bg="black", fg="white", font=("Segoe Print", 15))
    easy_explain3 = Label(root, text="The new generated number still has a chance to be the same number too", bg="black", fg="white", font=("Segoe Print", 15))
    guess_input = Entry(root, font=("Segoe Print", 15))
    attempts_left = Label(root, text=f"Attempts left : {attempts}", fg="blue", bg="#189100", font=("Comic Sans MS", 20))

    
    def check():
        guess = int(guess_input.get())
        if guess == number: #checks if the guess is correct
            clear()
            easy3()
        else: #now its confirmed the guess was incorrect because there can't be other possibilities
            nonlocal attempts
            attempts = attempts - 1
            attempts_left.config(text=f"Attempts left : {attempts}")
            if attempts == 0: #checks if that was your last attempt
                clear()
                gameover()
            else: #now its confirmed you still have attempts left
                if guess > number: #checks if the guess was bigger than the correct number so we can make sure the hint is correct
                    hint = "Lower"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#189100", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

                elif guess < number: #checks if the guess was less than the correct number so we can make sure the hint is correct
                    hint = "Higher"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#189100", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())
    
    guess_check = Button(root, text="Guess", bg="#00b3ff", font=("Segoe Print", 15), command=check) 


    guess_check.place(x=650, y=310)
    easy_explain.place(x=250, y=0)
    easy_explain2.place(x=165, y=40)
    easy_explain3.place(x=50, y=80)
    guess_input.place(x=300, y=320)
    attempts_left.place(x=330, y=400)


def easy3(): 
    root.configure(bg="#0b4500")
    root.title("Number guessing game | Easy level 3")
    attempts = 4
    number = random.randint(1,10)

    def clear():
        guess_check.destroy()
        guess_input.destroy()
        easy_explain.destroy()
        easy_explain2.destroy()
        easy_explain3.destroy()
        attempts_left.destroy()

    easy_explain = Label(root, text="Awesome you beat the second level", bg="black", fg="white", font=("Segoe Print", 15))
    easy_explain2 = Label(root, text="Welcome to level 3 the last level of easy difficulity", bg="black", fg="white", font=("Segoe Print", 15))
    easy_explain3 = Label(root, text="If you pass this you win, this time you have 4 attempts only !", bg="black", fg="white", font=("Segoe Print", 15))
    guess_input = Entry(root, font=("Segoe Print", 15))
    attempts_left = Label(root, text=f"Attempts left : {attempts}", fg="blue", bg="#0b4500", font=("Comic Sans MS", 20))

    def check():
        guess = int(guess_input.get())
        if guess == number: #checks if the guess is correct
            clear()
            easywin()
        else: #now its confirmed the guess was incorrect because there can't be other possibilities
            nonlocal attempts
            attempts = attempts - 1
            attempts_left.config(text=f"Attempts left : {attempts}")
            if attempts == 0: #checks if that was your last attempt
                clear()
                gameover()
            else: #now its confirmed you still have attempts left
                if guess > number: #checks if the guess was bigger than the correct number so we can make sure the hint is correct
                    hint = "Lower"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#0b4500", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

                elif guess < number: #checks if the guess was less than the correct number so we can make sure the hint is correct
                    hint = "Higher"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#0b4500", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())


    guess_check = Button(root, text="Guess", bg="#00b3ff", font=("Segoe Print", 15), command=check)
    guess_check.place(x=650, y=310)
    easy_explain.place(x=250, y=0)
    easy_explain2.place(x=165, y=40)
    easy_explain3.place(x=100, y=80)
    guess_input.place(x=300, y=320)
    attempts_left.place(x=330, y=400)

def easywin(): #win screen for easy difficulity
    root.configure(bg="#3e8230")
    root.title("Number guessing game")
    congrats = Label(root, text="Congrats you won !", bg="#3e8230", fg="#583082", font=("Segoe Print", 50))
    congrats.place(x=50, y=300)
    def returning():
        congrats.destroy()
        return_button.destroy()
        rage_quit.destroy()
        menu()
    
    return_button = Button(root, text="Return to main menu", bg="black", fg="white", font=("Comic Sans MS", 20), command=returning)
    rage_quit = Button(root, text="Quit", bg="black", fg="white", font=("Comic Sans MS", 20), command=destroy_game)
    return_button.place(x=450, y=600)
    rage_quit.place(x=250, y=600)

def normal():
    menuclear()
    root.configure(bg="#ffe600")
    root.title("Number guessing game | Normal level 1")
    attempts = 10
    number = random.randint(1,100)
    def clear():
        normal_explain.destroy()
        normal_explain2.destroy()
        normal_explain3.destroy()
        normal_explain4.destroy()
        guess_input.destroy()
        attempts_left.destroy()
        guess_check.destroy()

    def check():
        guess = int(guess_input.get())
        if guess == number: #checks if the guess is correct
            clear()
            normal2()
        else: #now its confirmed the guess was incorrect because there can't be other possibilities
            nonlocal attempts
            attempts = attempts - 1
            attempts_left.config(text=f"Attempts left : {attempts}")
            if attempts == 0: #checks if that was your last attempt
                clear()
                gameover()
            else: #now its confirmed you still have attempts left
                if guess > number: #checks if the guess was bigger than the correct number so we can make sure the hint is correct
                    hint = "Lower"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#ffe600", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

                elif guess < number: #checks if the guess was less than the correct number so we can make sure the hint is correct
                    hint = "Higher"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#ffe600", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

    
    normal_explain = Label(root, text="Welcome to normal difficulity", font=("Segoe Print", 15), bg="black", fg="white")
    normal_explain2 = Label(root, text="A random number was generated from 1 to 100", font=("Segoe Print", 15), bg="black", fg="white")
    normal_explain3 = Label(root, text="You have 10 attempts to guess it right to get to the next level", font=("Segoe Print", 15), bg="black", fg="white")
    normal_explain4 = Label(root, text="But if you run out of attempts you lose", font=("Segoe Print", 15), bg="black", fg="white")
    guess_input = Entry(root, font=("Segoe Print", 15))
    guess_check = Button(root, text="Guess", bg="#00b3ff", font=("Segoe Print", 15), command=check)
    attempts_left = Label(root, text=f"Attempts left : {attempts}", fg="blue", bg="#ffe600", font=("Comic Sans MS", 20))

    guess_check.place(x=650, y=310)
    normal_explain.place(x=300, y=0)
    normal_explain2.place(x=200, y=40)
    normal_explain3.place(x=150, y=80)
    normal_explain4.place(x=250, y=120)
    guess_input.place(x=300, y=320)
    attempts_left.place(x=330, y=400)
    




def normal2(): 
    root.configure(bg="#ffbb00")
    root.title("Number guessing game | Normal level 2")
    attempts = 8
    number = random.randint(1,100)

    def clear():
        normal_explain.destroy()
        normal_explain2.destroy()
        normal_explain3.destroy()
        normal_explain4.destroy()
        guess_input.destroy()
        attempts_left.destroy()
        guess_check.destroy()

    def check():
        guess = int(guess_input.get())
        if guess == number: #checks if the guess is correct
            clear()
            normal3()
        else: #now its confirmed the guess was incorrect because there can't be other possibilities
            nonlocal attempts
            attempts = attempts - 1
            attempts_left.config(text=f"Attempts left : {attempts}")
            if attempts == 0: #checks if that was your last attempt
                clear()
                gameover()
            else: #now its confirmed you still have attempts left
                if guess > number: #checks if the guess was bigger than the correct number so we can make sure the hint is correct
                    hint = "Lower"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#ffbb00", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

                elif guess < number: #checks if the guess was less than the correct number so we can make sure the hint is correct
                    hint = "Higher"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#ffbb00", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

    
    normal_explain = Label(root, text="Congrats on beating level 1 !", font=("Segoe Print", 15), bg="black", fg="white")
    normal_explain2 = Label(root, text="This is level 2, So you only have 8 attempts this time", font=("Segoe Print", 15), bg="black", fg="white")
    normal_explain3 = Label(root, text="The same number from level 1 has 1/100 chance to be the same in this level", font=("Segoe Print", 15), bg="black", fg="white")
    normal_explain4 = Label(root, text="Have fun and good luck", font=("Segoe Print", 15), bg="black", fg="white")
    guess_input = Entry(root, font=("Segoe Print", 15))
    guess_check = Button(root, text="Guess", bg="#00b3ff", font=("Segoe Print", 15), command=check)
    attempts_left = Label(root, text=f"Attempts left : {attempts}", fg="blue", bg="#ffbb00", font=("Comic Sans MS", 20))

    guess_check.place(x=650, y=310)
    normal_explain.place(x=300, y=0)
    normal_explain2.place(x=200, y=40)
    normal_explain3.place(x=50, y=80)
    normal_explain4.place(x=325, y=120)
    guess_input.place(x=300, y=320)
    attempts_left.place(x=330, y=400)

def normal3(): 
    root.configure(bg="#ff8c00")
    root.title("Number guessing game | Normal level 3")
    attempts = 5
    number = random.randint(1,100)

    def clear():
        normal_explain.destroy()
        normal_explain2.destroy()
        normal_explain3.destroy()
        normal_explain4.destroy()
        guess_input.destroy()
        attempts_left.destroy()
        guess_check.destroy()

    def check():
        guess = int(guess_input.get())
        if guess == number: #checks if the guess is correct
            clear()
            normalwin()
        else: #now its confirmed the guess was incorrect because there can't be other possibilities
            nonlocal attempts
            attempts = attempts - 1
            attempts_left.config(text=f"Attempts left : {attempts}")
            if attempts == 0: #checks if that was your last attempt
                clear()
                gameover()
            else: #now its confirmed you still have attempts left
                if guess > number: #checks if the guess was bigger than the correct number so we can make sure the hint is correct
                    hint = "Lower"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#ff8c00", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

                elif guess < number: #checks if the guess was less than the correct number so we can make sure the hint is correct
                    hint = "Higher"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#ff8c00", fg="red", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

    
    normal_explain = Label(root, text="Level 2 done, impressive skills", font=("Segoe Print", 15), bg="black", fg="white")
    normal_explain2 = Label(root, text="But this time you have only 5 attempts to guess the number correctly", font=("Segoe Print", 15), bg="black", fg="white")
    normal_explain3 = Label(root, text="If you beat this level you win, But if you run out of attempts you lose", font=("Segoe Print", 15), bg="black", fg="white")
    normal_explain4 = Label(root, text="Have fun and good luck", font=("Segoe Print", 15), bg="black", fg="white")
    guess_input = Entry(root, font=("Segoe Print", 15))
    guess_check = Button(root, text="Guess", bg="#00b3ff", font=("Segoe Print", 15), command=check)
    attempts_left = Label(root, text=f"Attempts left : {attempts}", fg="blue", bg="#ff8c00", font=("Comic Sans MS", 20))

    guess_check.place(x=650, y=310)
    normal_explain.place(x=300, y=0)
    normal_explain2.place(x=50, y=40)
    normal_explain3.place(x=70, y=80)
    normal_explain4.place(x=310, y=120)
    guess_input.place(x=300, y=320)
    attempts_left.place(x=330, y=400)

def normalwin(): #win screen for normal difficulity
    root.configure(bg="#ffb04f")
    root.title("Number guessing game")
    congrats = Label(root, text="Congrats you won !", bg="#ffb04f", fg="#583082", font=("Segoe Print", 50))
    congrats.place(x=50, y=300)
    def returning():
        congrats.destroy()
        return_button.destroy()
        rage_quit.destroy()
        menu()
    
    return_button = Button(root, text="Return to main menu", bg="black", fg="white", font=("Comic Sans MS", 20), command=returning)
    rage_quit = Button(root, text="Quit", bg="black", fg="white", font=("Comic Sans MS", 20), command=destroy_game)
    return_button.place(x=450, y=600)
    rage_quit.place(x=250, y=600)

def hard(): #ayo
    menuclear()
    root.configure(bg="#ff0000")
    root.title("Number guessing game | Hard level 1")
    attempts = 15
    def clear():
        hard_explain.destroy()
        hard_explain2.destroy()
        hard_explain3.destroy()
        hard_explain4.destroy()
        hard_explain5.destroy()
        hard_explain6.destroy()
        guess_input.destroy()
        guess_check.destroy()
        attempts_left.destroy()
        
    def check():
        guess = int(guess_input.get())
        if guess == number: #checks if the guess is correct
            clear()
            hard2()
        else: #now its confirmed the guess was incorrect because there can't be other possibilities
            nonlocal attempts
            attempts = attempts - 1
            attempts_left.config(text=f"Attempts left : {attempts}")
            if attempts == 0: #checks if that was your last attempt
                clear()
                gameover()
            else: #now its confirmed you still have attempts left
                if guess > number: #checks if the guess was bigger than the correct number so we can make sure the hint is correct
                    hint = "Lower"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#ff0000", fg="#ffd1d1", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

                elif guess < number: #checks if the guess was less than the correct number so we can make sure the hint is correct
                    hint = "Higher"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#ff0000", fg="#ffd1d1", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())
    
    number = random.randint(1,1000)
    hard_explain = Label(root, text="Welcome to hard difficulity", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain2 = Label(root, text="Its recommended to try the easy or normal difficulity first", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain3 = Label(root, text="But anyways, a random number was generated from 1 to 1000", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain4 = Label(root, text="You have to guess that number in 15 attempts or less to complete the level", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain5 = Label(root, text="So if you just started this game i don't recommend this difficulity", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain6 = Label(root, text="If you guess incorrectly 15 times you lose, Good luck", bg="black", fg="white", font=("Segoe Print", 15))
    guess_input = Entry(root, font=("Segoe Print", 15))
    guess_check = Button(root, text="Guess", bg="#00b3ff", font=("Segoe Print", 15), command=check)
    attempts_left = Label(root, text=f"Attempts left : {attempts}", fg="blue", bg="#ff0000", font=("Comic Sans MS", 20))

    guess_check.place(x=650, y=310)
    guess_input.place(x=300, y=320)
    attempts_left.place(x=330, y=400)
    hard_explain.place(x=300, y=0)
    hard_explain2.place(x=150, y=40)
    hard_explain3.place(x=125, y=80)
    hard_explain4.place(x=70, y=120)
    hard_explain5.place(x=130, y=160)
    hard_explain6.place(x=200, y=200)


def hard2(): 
    root.configure(bg="#bf0000")
    root.title("Number guessing game | Hard level 2")
    attempts = 10
    number = random.randint(1,1000)
    def clear():
        hard_explain.destroy()
        hard_explain2.destroy()
        hard_explain3.destroy()
        hard_explain4.destroy()
        guess_input.destroy()
        guess_check.destroy()
        attempts_left.destroy()
        
    def check():
        guess = int(guess_input.get())
        if guess == number: #checks if the guess is correct
            clear()
            hard3()
        else: #now its confirmed the guess was incorrect because there can't be other possibilities
            nonlocal attempts
            attempts = attempts - 1
            attempts_left.config(text=f"Attempts left : {attempts}")
            if attempts == 0: #checks if that was your last attempt
                clear()
                gameover()
            else: #now its confirmed you still have attempts left
                if guess > number: #checks if the guess was bigger than the correct number so we can make sure the hint is correct
                    hint = "Lower"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#bf0000", fg="#ffd1d1", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

                elif guess < number: #checks if the guess was less than the correct number so we can make sure the hint is correct
                    hint = "Higher"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#bf0000", fg="#ffd1d1", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

    number = random.randint(1,1000)
    hard_explain = Label(root, text="Congrats on beating level 1 !", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain2 = Label(root, text="Now things will get harder, this is a real challenge", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain3 = Label(root, text="You only have 10 attempts to guess the number this time", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain4 = Label(root, text="Good luck", bg="black", fg="white", font=("Segoe Print", 15))
    guess_input = Entry(root, font=("Segoe Print", 15))
    guess_check = Button(root, text="Guess", bg="#00b3ff", font=("Segoe Print", 15), command=check)
    attempts_left = Label(root, text=f"Attempts left : {attempts}", fg="blue", bg="#bf0000", font=("Comic Sans MS", 20))

    guess_check.place(x=650, y=310)
    guess_input.place(x=300, y=320)
    attempts_left.place(x=330, y=400)
    hard_explain.place(x=300, y=0)
    hard_explain2.place(x=200, y=40)
    hard_explain3.place(x=170, y=80)
    hard_explain4.place(x=380, y=120)

def hard3(): #level 3 of the hard difficulity (final level) (this is taking so long)
    root.configure(bg="#780000")
    root.title("Number guessing game | Hard level 3 (the end)")
    attempts = 5
    number = random.randint(1,1000)
    def clear():
        hard_explain.destroy()
        hard_explain2.destroy()
        hard_explain3.destroy()
        hard_explain4.destroy()
        guess_input.destroy()
        guess_check.destroy()
        attempts_left.destroy()
        
    def check():
        guess = int(guess_input.get())
        if guess == number: #checks if the guess is correct
            clear()
            hardwin()
        else: #now its confirmed the guess was incorrect because there can't be other possibilities
            nonlocal attempts
            attempts = attempts - 1
            attempts_left.config(text=f"Attempts left : {attempts}")
            if attempts == 0: #checks if that was your last attempt
                clear()
                gameover()
            else: #now its confirmed you still have attempts left
                if guess > number: #checks if the guess was bigger than the correct number so we can make sure the hint is correct
                    hint = "Lower"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#780000", fg="#ffd1d1", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

                elif guess < number: #checks if the guess was less than the correct number so we can make sure the hint is correct
                    hint = "Higher"
                    incorrect = Label(root, text=f"Incorrect, Hint : the correct number is {hint} than the number you guessed", bg="#780000", fg="#ffd1d1", font=("Comic Sans MS", 16))
                    incorrect.place(x=10, y=550)
                    root.after(2000, lambda:incorrect.destroy())

    number = random.randint(1,1000)
    hard_explain = Label(root, text="You beat level 2 ! Impressive !", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain2 = Label(root, text="Now this is the REAL challenge..", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain3 = Label(root, text="You only have 5 attempts to guess the number", bg="black", fg="white", font=("Segoe Print", 15))
    hard_explain4 = Label(root, text="If you guess this you win the whole game", bg="black", fg="white", font=("Segoe Print", 15))
    guess_input = Entry(root, font=("Segoe Print", 15))
    guess_check = Button(root, text="Guess", bg="#00b3ff", font=("Segoe Print", 15), command=check)
    attempts_left = Label(root, text=f"Attempts left : {attempts}", fg="blue", bg="#780000", font=("Comic Sans MS", 20))

    guess_check.place(x=650, y=310)
    guess_input.place(x=300, y=320)
    attempts_left.place(x=330, y=400)
    hard_explain.place(x=300, y=0)
    hard_explain2.place(x=295, y=40)
    hard_explain3.place(x=230, y=80)
    hard_explain4.place(x=275, y=120)

def hardwin(): #win screen for hard difficulity
    root.configure(bg="#ff5454")
    root.title("Congrats you beat it")
    congrats = Label(root, text="Congrats you beat HARD MODE", bg="#ff5454", fg="#583082", font=("Segoe Print", 35))
    congrats2 = Label(root, text="You won the game", bg="#ff5454", fg="#583082", font=("Segoe Print", 35))
    congrats.place(x=35, y=200)
    congrats2.place(x=200, y=300)

    def returning():
        congrats.destroy()
        return_button.destroy()
        rage_quit.destroy()
        menu()
    
    return_button = Button(root, text="Return to main menu", bg="black", fg="white", font=("Comic Sans MS", 20), command=returning)
    rage_quit = Button(root, text="Quit", bg="black", fg="white", font=("Comic Sans MS", 20), command=destroy_game)
    return_button.place(x=450, y=600)
    rage_quit.place(x=250, y=600)


def destroy_game():
    root.destroy()

def menu(): #main menu function
    root.configure(bg="#262626")
    root.title("Number guessing game")
    global main_menu
    global easy_dif
    global normal_dif
    global hard_dif
    global quit_game
    main_menu = Label(root, text="Welcome to yassen's number guessing game, choose a difficulty :", bg="black", fg="#ffffff", font=("Segoe Print", 15))
    main_menu.grid(padx=100, pady=20)
    easy_dif = Button(root, text="Easy", bg="#1fba00", fg="black", font=("Comic Sans MS", 15), command=easy, width=9, height=2)
    normal_dif = Button(root, text="Normal", bg="#ffea00", fg="black", font=("Comic Sans MS", 15), command=normal, width=9, height=2)
    hard_dif = Button(root, text="Hard", bg="#cc0202", fg="black", font=("Comic Sans MS", 15), command=hard, width=9, height=2)
    quit_game = Button(root, text="Quit", bg="black", fg="white", font=("Comic Sans MS", 15), command=destroy_game, width=9, height=2)
    quit_game.place(x=390, y=600)
    easy_dif.place(x=50, y=500)
    normal_dif.place(x=390, y=500)
    hard_dif.place(x=700, y=500)

def menuclear():

    easy_dif.destroy()
    normal_dif.destroy()
    hard_dif.destroy()
    quit_game.destroy()
    main_menu.destroy()
    
menu()
root.mainloop() 