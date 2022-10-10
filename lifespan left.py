age = input("What is your current age?")

age_int= int(age)

years_remaining= 90-age_int
days_remaining= 365 * years_remaining
weeks_remaining= 52 * years_remaining
months_remaining= 12 * years_remaining

print("years remaining-",years_remaining)
print("days remaining-",days_remaining)
print("weeks remaining-",weeks_remaining)
print("months remaining-",months_remaining)
