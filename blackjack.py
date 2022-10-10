import random
end = False
logo = """
 .------.          
|A     |.         
|( \/ )| .-----.    
| \  / |K /\  |     
|  \/  |  /  \ |            
 `-----' |  \  / |     
          |   \/K|                                      
            `------'
\t ROUND 1
"""   

while not end:
    print(logo)
    print()
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #user score
    user = [random.choice(cards),random.choice(cards)]
    user_score = user[0] + user[-1]
    print("your cards:",user)
    user_tot=print("current score:",user_score)

    #computer score
    comp = [random.choice(cards),random.choice(cards)]
    comp_score = comp[0] + comp[1]
    print("computer's first card:",comp[0])

    #take another card
    choice = input("Type 'y' to take another card, type 'n' to pass:")

    if choice == 'y':
        print()
        print("\t" "ROUND 2")
        new_card = random.choice(cards)
        user.append(new_card)
        user_score += new_card
        print("your final cards:",user)
        print("your final hand:",user_score)
        new_comp_card = random.choice(cards)
        comp.append(new_card)
        comp_score += new_comp_card
        print("computer's final hand:",comp_score)
        
    elif choice == 'n':
        print("computer's final hand:",comp_score)
        
    if user_score > 21:
        print("USER BUSTED!")
        
    elif 21 >= user_score > comp_score:
        print("USER WINS!")
        
    elif user_score < comp_score <= 21:
        print("USER BUSTED!")
        
    elif comp_score > 21:
        print("USER WINS!")

    elif comp_score == user_score:
        print("DRAW!")
    print()
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if restart == "no":
        end = True
        print("the end!")
