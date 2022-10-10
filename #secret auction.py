dictionary={}
biders = False
while not biders:
    k = input("what is your name? ")
    value = int(input("what's your bid? $"))
    dictionary[k] = value
    choice = input("are there any other biders? ")
    if choice == "no":
        biders = True
max_bid = max(dictionary, key = dictionary.get)
print("maximum bider is:",max_bid)
