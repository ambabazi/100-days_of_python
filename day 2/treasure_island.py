print('''
                             _                      
                            | |                     
  __ _ _ __   ___   ___ __ _| |_   _ _ __  ___  ___ 
 / _` | '_ \ / _ \ / __/ _` | | | | | '_ \/ __|/ _ \| (_| | |_) | (_) | (_| (_| | | |_| | |_) \__ \  __/
 \__,_| .__/ \___/ \___\__,_|_|\__, | .__/|___/\___|
      | |                       __/ | |             
      |_|                      |___/|_|    
 ''')

print("Welcome to Treasure Island.\n "
      "Your mission is to find the treasure.")
direction = input("You are in the middle of the railway.\n"
                  " Where do you choose to go?\n "
                  "Type left or right\n").lower()
# if direction == "right":
#     print("You were killed by a train.Game Over!")
if direction == "left":
    print("You continue to the next level")

    door = input("you are in front of a door.\n Enter or Wait\n")
    if door == "Wait":
        print("You continue to the next level")

        card = input("Which card are you choosing.\n"
                     " Red, Yellow, Blue\n")
        if card == "Red":
            print("Poisoned. Game Over!")
        elif card == "Yellow":
            print("Congratulationsss!!!!!!!!!!!\n "
                  "You Wiiiin!!!!!!")
        elif card == "Blue":
            print("Burned by a blue flame.\n Game Over!")
        else:
            print("Game Over!")
    elif door == "Enter":
        print("Attacked by zombies.\n Game Over!")
    else:
        print("Invalid choice")
else:
    print("You were killed by a train.\n Game Over!")
