print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice_1= input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")
if choice_1 == 'left':
  choice_2= input("You're come to a lake. There is and island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
  if choice_2 == 'wait':
    choice_3= input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose? ")
    if choice_3 == 'red':
      print("It's a room full of fire. Game Over!")
    if choice_3 == 'yellow':
      print("You found the treasure! You Win!")
    if choice_3 == 'blue':
      print("You enter a room of beasts. Game Over!")
  if choice_2 == 'swim':
    print("You get attacked by an angry crocodile! Game Over!")
if choice_1 == 'right':
    print("You fell into a hole. Game Over!")
