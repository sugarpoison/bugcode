location = ""
while location != "Home" and location != "District Alpha" and location != "District Beta":
    location = input("Enter Home, District Alpha, or District Beta for a location ")
if location == "Home":
    print("Welcome", location)
else:
    print("Welcome to", location)

