file = open("student.txt","w")
file.write("Sharmada K \n BSc CS with CyberSecurity")
file.close()

file = open("student.txt")
print(file.read())
file.close()