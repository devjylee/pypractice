python = "Python is Amazing"
print(python.upper())
print(python.lower())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java")) #-1
#print(python.index("Java")) error

print(python.count("n"))