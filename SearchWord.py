file = open("student.txt","r")

data = file.read()
word = input("Enter a word: ")

if word in data:
    print("Word Found")
else:
    print("Word Not Found")

file.close()
