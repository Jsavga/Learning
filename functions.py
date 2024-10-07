# create a simple function that uses a global variable
# Note that global variables SHOULD NOT be used in functions and it's bad practice

my_name = 'john'  # Global variable


def greet_user():
    """Display a simple greeting with a global variable (bad practice)

       Note that Global variables in functions are bad practice and shouldn't be done
       This exercise just shows that it can be.
       Again, please don't use global variables in functions.
       """

    print(f'Hello {my_name.title()}')


# call that function
greet_user()
# change global variable contents
my_name = 'timmy'
greet_user()
# The above showed how to use a Global variable in a function
# It is bad practice to do so and shouldn't be done if at all possible
# The preferred way is to pass a literal or variable to the function instead of using a global variable





# create a function that passes information through a functional parameter

def greetings(username):
    """Display a simple greeting to a user"""
    print(f'Hello {username}')


user_name = ''
while user_name != 'quit' and user_name != 'exit':
    user_name = input("\nWhat is your username ('quit' to exit): ")
    user_name = "".join(user_name.split()).lower()  # remove all whitespace and make lower-case
    if user_name != 'quit' and user_name != 'exit':
        greetings(user_name)
print()
