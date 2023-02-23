a= float(input("Give me a number "))
b= float(input("What would you like to divide by? "))

try:
    print(f"The quotient is {a/b}.")
except:
    print("That didn't work out.")
else:
    print("Wow! You did it! ")
finally:
    print("Thanks for doing that.")