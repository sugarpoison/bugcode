price = 550
item = 3
msg=("The price for an item is{price: .2f}")
print(msg.format(price=550))
print(f"I have {item} in stock right now.")

# bonus because im BORED

buy = ""

buy = input("Want one? ")
if buy == "Yes":
    print(f"There you go. I only have {item - 1} left now.")
if buy == "No":
    print("That's your choice. They might not be here tomorrow.")
if buy != "Yes" and buy != "No":
    print("..?")


    



