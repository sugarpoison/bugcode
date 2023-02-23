#Program 27 runtime errors
a = float(input("Enter a number "))
b = float(input("Enter a number to divide by "))

try:
    print(f"The answer is {a/b}. ")
except:
    print("Don't divide by zero.")