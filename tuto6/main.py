"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""
file = open("bio.txt","a")
file.write("Hobby : Play Games")
file.close()

file = open("bio.txt","r")
print(file.read())
file.close()