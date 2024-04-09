# WAP to understand string methods

a = "!!!Bunny Ayush Ankur!!!!!"
print(a)
print(len(a))
print(a.upper()) #Uppercase
print(a.lower()) #Lowercase
print(a.rstrip("!")) #Deletes all the leading ! not the trailing
print(a.replace("Bunny",'Ayush')) 
print(a.split(" "))
print(a.count("a")) #Count method is case sensitive
print(a.count("A"))

b="introduction to python"
print("\n",b.capitalize()) #Auto capitalize the first letter
print(b.endswith("on")) #Gives bool answer
print(b.endswith("duc", 3, 8))
print(b.startswith("intr"))

c="Welcome to console"
print("\n",c)
print(c.center(50)) #Alligns the string to center as per parameters
print(len(c))
print(len(c.center(50)))

d="Hes name is Ayush He is an honest man"
print("\n",d.find("is")) #Gives first occurence of "is"
print(d.find("issh")) 
print(d.isalnum()) #Returns True only if the entire string consists of A-Z,a-z,0-9, otherwise returns false. If there are spaces in the string it still returns False.
print(d.isalpha()) #Returns True only if the entire string consists of A-z,a-z. If there are spaces in the string it still returns False.
print(d.islower()) #Returns True of all the characters are in lowercase, otherwise False.
print(d.isupper()) #Returns True of all the characters are in uppercase, otherwise False.

e="We wish you a happy new year \n"
print("\n",e.isprintable()) #Returns False as \n is an escape sequence character and is not printable.
print(e.isspace()) #Returns True if the string only contains whitespace, otherwise returns False.
print(e.swapcase()) #Swaps uppercase characters with lowercase characters.
print(e.title()) #Capitalizes all the first letters of each word.
print(e.istitle()) #Returns True only if first letter of each word of the string is capitalized, else it returns False.