def subtotal(orderAmt, salesTax = .08):
    subtotal = float(orderAmt) * (1 + float(salesTax))
    return subtotal

def orderMsg():
    print("Thank you for your business.")
    return

totalOne = subtotal(300, .08)
totalTwo = subtotal(400, .06)
amtThree = input("How much was the order? ")
taxThree = input("What is your tax rate? ")
totalThree = subtotal(amtThree, taxThree)
totalFour = subtotal(800)

print("The subtotal for order one is %.2f" %totalOne)
print("The subtotal for order two is %.2f" %totalTwo)
print("The subtotal for order three is %.2f" %totalThree)
print("The subtotal for order four is %.2f" %totalFour)
orderMsg()