games = ["Bug Fables", "Hollow Knight", "Katana Zero", "Hotline Miami 2", "Dead Cells"]

for game in games:
    print(game)

print()
games.append("Risk of Rain 2")
games.remove("Dead Cells")
games.sort()

for game in games:
    print(game)