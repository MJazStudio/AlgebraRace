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
    player_data = {}
    try:
        with open("high_score.txt", "r") as file:
            for line in file:
                name, best_score = line.strip().split(",")
                player_data[name] = int(best_score)
            
            
            high_scr_plyr = max(player_data, key=player_data.get)
            print(f"\nPlayer with the highest score: {high_scr_plyr} ({player_data[high_scr_plyr]})")
    except FileNotFoundError:
        pass
    
    player_name = input("Enter your name: ").upper()
    
    if player_name not in player_data:
        player_data[player_name] = 0

    hs_curnt_plyr=player_data[player_name]
    print("Your best score is ",hs_curnt_plyr)
    
    score = 0
    start_time = time.time()
    end_time = start_time + 60
    
    while time.time() < end_time:
        if qst():
            score += 1
    
    print("Time's up!")
    print("Final Score:", score)
    
    if score > player_data[player_name]:
        player_data[player_name] = score
        print("New personal best score achieved!")
    
    with open("high_score.txt", "w") as file:
        for name, best_score in player_data.items():
            file.write(f"{name},{best_score}\n")

control = "y"
while control.lower() == "y":
    main()
    control = input("Do you wish to continue (y/n): ")
