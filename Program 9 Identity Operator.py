# These two values are identical. 'a' and 'b' connect to the *same* value of 3.
a = 3
b = a

# These two values are NOT identical. They have the same values, but they are seperate lists.
northItems = ["Raincoat", "Snowboots"]
eastItems = ["Raincoat", "Snowboots"]

print (northItems == eastItems)
print (northItems is eastItems)
print (northItems is not eastItems)

print (a == b)
print (a is b)