message = "Hello"
message2 = "James"

print("Hello James")  # outputs the the text inside quotes
print('I said "Hello" James')  # use single quotes when you want to include double quotes in text
print(message)  # outputs the text inside the v_message variable
print(message, message2)  # outputs text of combined variables (has a space between them)
print(message + message2)  # same as above but omits the space between them
print(message + " there " + message2)  # adds a string in the middle
print(f"{message} there {message2}")  # same as above with fstring
print(message.lower())  # outputs lowercase
print(message.upper())  # outputs uppercase
print(message2.title())  # Uses title case (first letter in words capitalized)
print(len(message))  # shows length of characters in variable text
print(message2[2])  # prints the 3th character of message2 (left most character is index position 0)
print(message2[1:3])  # prints starting at 1st index position and stopping "before" index 3 position

print(dir(message))  # Shows available modifiers

# print can be spread out over lines. Close the quotes on the first line and indent the second to continue printing
print("the quick brown fox "
      "jumps over the lazy dog")
