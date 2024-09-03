# removing whitespace with lstrip, rstrip and strip methods
# removing prefix with .removeprefix

favorite_language = "python "  # has extra space at end of string
print(favorite_language)  # This has an extra space at end even if you can't see it

# let's temporarily strip the whitespace from the end of the favoroite_launguage varibable
print(favorite_language.rstrip() + "programming language")
print(favorite_language + "programming language")  # change was only temp
print()

# to make the change permanent, you have to redefine the varible
favorite_language = favorite_language.rstrip()
print(favorite_language + "programming language")
print()

favorite_language = " Python "
print(favorite_language + "programming language")
print(favorite_language.lstrip() + "programming language")  # lstrip to remove left whitespace
print(favorite_language.rstrip() + "programming language")  # rstrip to remove right whitespace
print(favorite_language.strip() + "programming language")  # strip to remove both ends whitespace
print()

# removeprefix method removes a defined part at beginning of string
# removesuffix method removes a defined part at end of string
my_url = "https://my.home.com"
my_name = "Mr. James"
print(my_url, "- before removing prefix")
print(my_url.removeprefix("https://"), "- after removing prefix")  # use .removeprefix method
print(my_url.removesuffix(".com"), "- after removing suffix")  #use .removesuffix method
print()

print(my_url)
my_url = my_url.removeprefix("https://")  # Reassign variable after using removeprefix on it
print(my_url)
print()

print(my_name)
print(my_name.removeprefix("Mr.").lstrip())  # Removes prefix then strips left whitespace. Multiple method on one line
