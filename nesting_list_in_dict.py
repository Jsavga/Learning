pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}  # nest list inside a dictionary

print(f"you ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

favorite_languages = {'jen': ['python', 'rust'], 'sarah': 'c', 'edward': ['rust', 'go'],
                      'phil': ['python', 'haskell']}  # another nest of list inside dictionary
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        sentence_choice = "languages are"
    else:
        sentence_choice = "language is"
    print(f"\n{name.title()}'s favorite {sentence_choice}:")


    for language in languages:
        print(f"\t{language.title()}")
