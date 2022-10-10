print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_names= name1 + name2
lower_case_cn= str.lower(combine_names)

t= lower_case_cn.count("t")
r= lower_case_cn.count("r")
u= lower_case_cn.count("u")
e= lower_case_cn.count("e")
first_digit= t + r + u + e

l= lower_case_cn.count("l")
o= lower_case_cn.count("o")
v= lower_case_cn.count("v")
e= lower_case_cn.count("e")
second_digit= l + o + v + e

score= int(str(first_digit) + str(second_digit))

if 10 > score or score > 90:
  print("Your score is ",score,", you go together like coke and mentos!")
elif 40 < score < 50:
  print("Your score is ",score,", you are alright together.")
else:
  print("Your score is ",score)
