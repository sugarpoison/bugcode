

writeFile = open("log.txt", "w")
toLog = input("I'm at the Pizza Hut, I'm at the Taco Bell, I'm at the combination Pizza Hut and Taco Bell.")
writeFile.write(toLog)
writeFile.close()

writeFile = open("log.txt", "r")
print(writeFile.read())
writeFile.close()
