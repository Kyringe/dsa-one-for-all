# WAP to translate a message into secret code language. Use the rules below to translate normal
# English into secret code language

# Coding:
# If the word contains atleast 3 characters, remove the first letter and append it at the end.
# Now append three random characters at the starting and the end.
# Else: Simply reverse the string

# Decoding:
# If the word contains less than 3 characters, reverse it
# Else: Remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

st = input("Enter the message: ")
words = st.split(" ")
coding = True #Use coding = False for decoding
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "abc"
            r2 = "xyz"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1]) #Method to reverse the string
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1]) #Method to reverse the string
print(" ".join(nwords))