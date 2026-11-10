original = open("student.txt","r")

data = original.read()
original.close()

copy = open("student.txt","w")

copy.write(data)
copy.close

print("Data Copied Successfully")
