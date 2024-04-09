# There are six modes in file handling: read, write, append, create, text, binary
# Its syntax is: f = open('file_name','r'). You can use r/w/a/x/t/b

f = open('/Users/kyringe/Desktop/DADDY BALLZ/Python/CWH/049_myfile.txt','r')
text = f.read()
print(text)
f.close()

# With statement: Using this you need not close the file after every statement
with open('/Users/kyringe/Desktop/DADDY BALLZ/Python/CWH/049_myfile.txt', 'a') as f:
    f.write(" .Laand ka dost")