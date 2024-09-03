name = "ada lovelace"
print (name.title())   #title method capitalizes first letter of every word


first_name = "ada"
last_name = "lovelace"
print (first_name + " " + last_name)
print (f"{first_name} {last_name}")   #accomplish same as line above

full_name = f"{first_name} {last_name}"   #f is used to add variables and space to new variable
message = f"Hello, {full_name.title()}!"
print (message)