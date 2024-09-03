first_name = "ada"
last_name = "lovelace"

print(first_name.title())  # title method capitalizes first letter of every word

print(first_name + last_name)  # using a + between varible or strings adds no space
print(first_name, last_name)   #using a comma between them adds a space

print("Hello", first_name, last_name + ", how are you?")  # used + after 2nd varible, if used comma would get a space
print(f"Hello {first_name} {last_name}, how are you?")  # accomplish same as lines above with an f string

full_name = f"{first_name} {last_name}"  # fstring is used to add variables and space to new variable
message = f"Hello, {full_name.title()}!"
print(message)
