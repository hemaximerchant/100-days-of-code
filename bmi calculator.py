height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI= weight / (height*height)
print("your BMI is ",BMI)
if BMI < 18.5:
  print("You're underweight")
elif 18.5 < BMI < 25:
  print("You're normal weight")
elif 25 < BMI < 30:
  print("You're overweight")
elif BMI > 30:
  print("You're obese")
