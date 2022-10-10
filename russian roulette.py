import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length=len(names)
print(names)
random_index = random.randint(0,length-1)
print(names[random_index])
