workFile = open ('jackets.txt', "r")
workFileContents = workFile.read()
print(workFileContents)
workFile.close()
print("File has been closed")



workFile = open ('jackets.txt', "r")
workFileFirstLine = workFile.readline()
print(workFileFirstLine)
workFileSecondLine = workFile.readline()
print(workFileSecondLine)
workFile.close()
print("File has been closed")
