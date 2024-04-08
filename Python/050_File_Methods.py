# Readline() method reads a single line from the file. If we want to read multiple lines we can use a loop

f = open('/Users/kyringe/Desktop/DADDY BALLZ/Python/CWH/050_myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# Writelines() methood

f = open('/Users/kyringe/Desktop/DADDY BALLZ/Python/CWH/050_myfile2.txt', 'w')
lines = ['asas\n', 'sqwqd\n']
f.writelines(lines)
f.close()