#removing whitespace with lstrip, rstrip and strip methods
from idlelib.debugobj import myrepr

favorite_language = "python " #has extra space inside of string
print (favorite_language)   #extra space is not noticed, but it's there
print (favorite_language + "programming language")

# let's temparily strip the whitespace from the end of the favoroite_launguage varibable
print (favorite_language.rstrip() + "programming language")
print (favorite_language + "programming language")

# to make the change permanent, you have to redefine the varible
favorite_language = favorite_language.rstrip()
print (favorite_language + "programming language")

favorite_language = " Python "
print (favorite_language + "programming language")
print (favorite_language.lstrip() + "programming language") #lstrip to remove left whitespace
print (favorite_language.strip() + "programming language") #strip to remove both ends whitespace


# Remove prefix removes part of a string temporarily just the the .string methods do

my_url = "https://my.home.com"
my_name = "Mr. James"
print (my_url)
print (my_url.removeprefix("https://"))    #use .removeprefix method
print (my_url)
my_url = my_url.removeprefix("https://")    #Reassign variable after using removeprefix on it
print (my_url)
print (my_name)
print (my_name.removeprefix("Mr.").lstrip())   #Removes prefix then strips left whitespace. Multiple method on one line
