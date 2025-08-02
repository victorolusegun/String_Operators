sentence = 'what is your name??'
word = 'VICTOR'
new = '.#345ui'
anum = 'Victor2006'
dec = '101'
tab = 'D\te\tm\to'
space = ' '
title = sentence.title()
rem = '   I like twitter, improv and movies'
rem_format = rem.lstrip()
note = 'His name is Victor, he likes to code, he hates reading and he likes movies '
str_list = 'Chelsea, Marvel, DC, TBBT'
#.capitalize: Makes the first letter of the first word uppercase
sentence_0 = sentence.capitalize()
print(sentence_0)

#.casefold(): Makes all words in sentence lowercase
print(sentence_0.casefold())

#.center(): Used to align a string centrally
print(word.center(10))

#.count(): Used to search for a specific value and count the number of time it appears
print(sentence.count('a'))

#.endswith(): Used to check if a string ends with a specific value
print(sentence.endswith('t', 1,4))

#.expandtabs(): Used to expand tabs. note the default ta size is 8
print(tab.expandtabs(2))

#.find(): Used to check for the occurence of a specific letter
print(sentence_0.find('name'))

#.index(): Used to find the index of a specific element
print(sentence.index('o'))

#.isalnum(): Used to check if a string is alphanumeric
print(anum.isalnum())

#.isalpha(): Check if a string is alphabetic
print(word.isalpha())

#.isascii(): To check if a string contains elements that are part of the standard ASCII set
print(new.isascii())

#.isdecimal(): To check if a string is decimal(0-9)
print(dec.isdecimal())

#.isdigit(): To check if a string is made up of digits
print(word.isdigit())

#.isidentifier(): To check if a string is an identifier
print(new.isidentifier())

#.islower(): To check if all letters are lowercase
print(word.islower())

#.isnumeric(): To check if a string is numeric
print(dec.isnumeric())

#.isprintable(): To check if every elements in a string are printable(character like \n, \t aren't)
print(tab.isprintable())

#.isspace(): To check if a string contains only whitespaces
print(space.isspace())

#.istitle(): To check if a string
print(title.istitle())

#.isupper(): To check if all characters in the string are uppercase
print(word.isupper())

#.join(): Used to join iterable elements to the end of a string
listed = {'Hulk', 'Thor', 'Zatanna', 'Constantine'}
print(space.join(listed))

#.lower: Changes all elements to lowercase
print(word.lower())

#.lstrip(): Used to remove characters from the left of the string, default is whitespace
print(rem.lstrip())

#.replace():Used to replace one value with another
print(rem_format.replace('twitter', 'X'))

#.rfind(): Used to find the rightmost(last) occurence of a substring in a string
print(note.rfind('he'))

#.rindex(): Used to get the index of the last occurence of a specifc value
print(note.rindex('he'))

#.rjust(): used to align charcters to the right and fill characters in the left
print(word.rjust(7, 'A'))

#.rsplit(): Used to split a string from the right
print(str_list.rsplit(',', 1))

#.rstrip(): Used to remove charcters from the right of string
strip = 'A boys'
print(strip.rstrip('s'))

#.split(): Used to split a string
print(str_list.split(',', 1))

#.splitlines(): Used to split a string into a list
print(str_list.splitlines())

#startswith(): Used to check if a string begins with a particular method
print(sentence.startswith('yo', 8,16))

#.strip(): Used to remove whitespaces
print(rem.strip())

#.swapcase(): Used to swap the case of a string to another
print(sentence.swapcase())

#.title(): Converts the first letter of every word to uppercase. Reference initialization of title var
print(title)

#.upper(): COnverts all letters to uppercase
print(sentence.upper())

#.zfill(): Used to fill zeroes at the beginning of a string
print(space.zfill(7))