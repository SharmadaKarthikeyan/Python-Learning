file = open("student.txt","r")

data = file.read()
words = data.split()

print("Total Number of Words: ",len(words))

file.close()

