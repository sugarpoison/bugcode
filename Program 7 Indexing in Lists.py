# The first element is 0, then 1, then 2, etc. 
#             0               1                2              3                 4
games = ["Bug Fables", "Hollow Knight", "Katana Zero", "Hotline Miami 2", "Dead Cells"]
#       0  1  2  3  4
rank = [2, 1, 3, 4, 5]
#               0         1        2        3         4
characters = ["Leif", "Hornet", "Zero", "Jacket", "Beheaded"]

print("Game:",games[1],"\tRank: ",rank[0])
print("Game:",games[-1],"\tRank: ",rank[-1])
# This replaces an element in a list.
characters[2] = "Fifteen"

for character in characters:
    print(character)



