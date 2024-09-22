message = "Hello"
message2 = "James"

print("Hello James")  # outputs the the text inside quotes
print('I said "Hello" James')  # use single quotes when you want to include double quotes inside text
print("Where is James's car") # use double quotes when you want to include a single quote inside text
print(message)  # outputs the text inside the message variable
print(message, message2)  # outputs text of combined variables (has a space between output by default)
print(message + message2)  # same as above but omits the space between them
print(message + " there " + message2)  # adds a string in the middle
print(f"{message} there {message2}")  # same as above with f string
print(message.lower())  # outputs lowercase
print(message.upper())  # outputs uppercase
print(message2.title())  # Uses title case (first letter in each word capitalized)
print(message2[2])  # prints the 3th character of message2 (left most character is index position 0)
print(message2[1:3])  # prints starting at 1st index position and stopping "before" index 3 position
print(len(message))  # shows length of characters in variable text
print() #prints a blank line by default



# print can be spread out over lines. Close the quotes on the first line and indent the second to continue printing
print("the quick brown fox "
      "jumps over the lazy dog")

print()


# sep= determines what's between the different items in a print statement, default is a space
# end= determines how the print statement ends, default is /n (newline)
print('My name is', 'James')
print('My name is', 'James', sep='\t')  # tab character
print('My name is', 'James', sep='')
print('My name is', 'James', sep='\n')  # newline character
print('My name is', 'James', sep=' | ')
print()
print('the sly brown fox')
print('jumped over the fence')
print()
print('the sly brown fox', end='...') #end="..." changes default newline to ...
print('jumped over the fence')
print()
# f strings let you include variables inside your strings
my_name = 'james'
print(my_name)
print(f'My name is {my_name.title()} and I am happy to meet you')
print()

# different methods can be used on what's printed.
some_name = 'john quincy adams'
print(some_name.upper(), some_name.lower(), some_name.title(), sep=', ')
padded_words='   this has spaces   '
print(padded_words,padded_words.lstrip(), padded_words.rstrip(),padded_words.strip(), sep=',', end='?\n')
print()

print(dir(message))  # Shows available modifiers