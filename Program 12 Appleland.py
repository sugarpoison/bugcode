# Once upon a time in Appleland, Jake had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

jake = 3
mary = 5
adam = 6

print("Jake has", jake, "apples, Mary has", mary, "apples, Adam has", adam, "apples.")

total_apples = (jake + mary + adam)
print(total_apples)

print("If the three wanted to share their apples, each would have", int(total_apples / 3, ),".")
print("They would have", (total_apples % 3), "remaining.")

# They also collect cards :)

jakeCard = ["White Eyes Blue Dragon", "Pocketchu", "Supreme Crab", "Forsaken Magician"]
maryCard = ["Fredrick Fear Bear", "Vase of Gluttony", "Crazy Hamburger", "USB Stick of Power"]
adamCard = ["Python Python", "Animated House", "Goblin 4", "Cat that is Evil"]

print("Jake owns:", jakeCard)
print("Mary owns", maryCard)
print("And Adam owns:", adamCard)

print("Mary wants to trade wit Adam, so she will take his,", adamCard[0], "in exchange for her", maryCard[2])