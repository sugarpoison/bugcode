import os
if os.path.isfile('log.txt'):
    writeFile = open('log.txt', 'a')
else:
    writeFile = open('log.txt', 'w')

toLog = input("The sound of four hundred bees will echo throughout the halls.")
writeFile.write("\n" + toLog)
writeFile.close()
