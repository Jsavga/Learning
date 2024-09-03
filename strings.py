v_message = "Hello"
v_message2 = "James"

print ("Hello James") #outputs the the text inside quotes
print ('I said "Hello" James') #use single quotes when you want top include double quotes in text
print (v_message) #outputs the text inside the v_message variable
print (v_message + v_message2) #outputs text of combined variables
print (v_message + " there " + v_message2) #same asd above but adds a string in the middle
print (v_message.lower()) #makes lowercase
print (v_message.upper()) #makes uppercase
print (len(v_message)) #shows length of characters in variable text
print (v_message2[4]) #prints the 4th character of message2 (left most character is index position 0)
print (v_message2[1:3])#prints starting at 1st index position and stopping "before" index 3 position

print (dir(v_message)) #Shows available modifiers