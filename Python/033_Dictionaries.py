# WAP to print a basic dictionary

dict = {
    "Name": "Bunny",
    "Sex": "Male"
}
print(dict["Name"]) #Dictionary are ordered and sets are unordered
print("\n")

# Accessing dictionary items

print(dict)
print(dict['Name']) #This throws an error if the key is not present in the dictionary
print(dict.get("Sex")) #This does not throw an error if the key is not present in the dictionary

print(dict.keys()) #Prints all the keys in the dictionary

for key, value in dict.items():
    print(f"The value to the key {key} is {value}")