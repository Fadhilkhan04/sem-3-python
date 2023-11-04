def contains_only_357(number):

    allowed_digits={'3','5','7'}
    return all(digit in allowed_digits for digit in number)

while True:

    user_input = input("Enter a number containing only 3,5, or 7:")

    if contains_only_357(user_input):
        break

    else:
        print("Invalid input. Please enter a number containing only 3,5, or 7.")

number=int(user_input)

if number%3==0:

    print("3 is a divisor. This is your lucky number!")

elif number%5==0:

    print("5 is a divisor. This is your lucky number!")

elif number%7==0:

    print("7 is a divisor. This is your lucky number!")

else:
  
    print("This number is not divisble by 3,5, or 7.")
    