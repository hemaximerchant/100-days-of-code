def prime_checker(number):
  is_prime=True
  for i in range(2,number):
    if number%i==0:
      is_prime=False
  if is_prime:
    print(number,"is a prime number!")
  else:
    print(number,"is a composite number!")
no = int(input("Check this number: "))
prime_checker(number=no)
