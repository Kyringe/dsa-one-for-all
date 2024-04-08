# Seek function allows you to move the current position within afile to a specific point

with open ('/Users/kyringe/Desktop/DADDY BALLZ/Python/CWH/051_myfile.txt', 'r') as f:
    f.seek(9)
    print(f.tell()) #Tell function returns the current position within the file, in bytes
    data=f.read(5)
    print(data)


# Truncate method allows you to read only those many bytes that you wish

with open('/Users/kyringe/Desktop/DADDY BALLZ/Python/CWH/051_myfile2.txt', 'w') as f:
    f.write("Bhosad chodau")
    f.truncate(6)
with open ('/Users/kyringe/Desktop/DADDY BALLZ/Python/CWH/051_myfile2.txt', 'r') as f:
    print(f.read())