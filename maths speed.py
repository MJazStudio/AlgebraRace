import random
import time

def qst():
    a = random.randint(2, 12)
    b = random.randint(2, 12)
    c = a * b
    ans = int(input(str(a) + " * " + str(b) + " = "))
    if ans == c:
        print("Correct")
        return True
    else:
        print("Wrong")
        return False

def main():
    high_score = 0
    try:
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())
            print("High Score is ", high_score)
    except FileNotFoundError:
        pass
    
    score = 0
    start_time = time.time()
    end_time = start_time + 60
    
    while time.time() < end_time:
        if qst():
            score += 1
    
    print("Time's up!")
    print("Final Score:", score)
    
    if score > high_score:
        with open("high_score.txt", "w") as file:
            file.write(str(score))
            print("New high score achieved!")
            
control=input("Are you ready to start(y/n)")
while(control.lower()=="y"):
    main()
    control=input("Do you wish to continue(y/n)")
