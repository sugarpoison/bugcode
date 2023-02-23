

file1 = open("bugfile.txt", "w")
L = ["This is a wasp \n", "This is a beetle \n", "This is a moth"]
file1.writelines(L)
file1.close()

# Append - adds at the end
file1 = open("bugfile.txt", "a") # the 'a' means append
file1.write("\nDon't forget the spiders!")
file1.close()

file1 = open("bugfile.txt", "r")
print("Output after appending")
print(file1.read())
print()
file1.close()

# Write - Overwrites
file1 = open("bugfile.txt", "w") # the 'w' means write
file1.write("Bug! \n")
file1.close

file1 = open("bugfile.txt", "r")
print("Output after writing")
print(file1.read())
print()
file1.close()
