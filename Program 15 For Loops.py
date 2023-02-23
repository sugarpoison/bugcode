vipList = ["Micah", "William", "Chris", "Janette", "Rosie", "Molly", "Kat", "Cyrus", "Robin", "Amanda" ]

# Range generates a list of values between the given ones, except for the last one.
# "For" will address every value in a list one time.
for allowed in vipList:
    if allowed == "Rosie" or allowed == "Molly" or allowed == "Kat" or allowed == "Cyrus":
        print("Access granted.")
        continue
    else:
        print("Access denied.")