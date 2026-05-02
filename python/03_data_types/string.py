#Strings are Immutable 

greeting = "Hello"
name = "Alice"
print(f"Greeting: {greeting} {name}")
print(f"Id of greeting: {id(greeting)}") 

#indexing Every letter in string has an index starting from 0
description = "This is a string"
print(f"First character:{description[0:7:1]}") #start:stop:step every nth character

print(f"last word: {description[12:]}") #started from index 12 to end of string
print(f"Reverse string:{description[::-1]}") #gnirts a si sihT

#special characters or symbols
label= "Spècial characters" 
encoded_label = label.encode('utf-8')
print(f"Encoded label: {encoded_label}") #b'Sp\xc3\xa8cial
print(f"Non Encoded label: {label}") #Spècial characters
print(f"Decoded label: {encoded_label.decode('utf-8')}") #Spècial characters

