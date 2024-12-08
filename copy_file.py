fobject = open("users.csv", "r")

result = fobject.read()

# write this result into another file
fobject_write = open("users-copy.csv", "w")

fobject_write.write(result)

## close the file objects
fobject.close()
fobject_write.close()