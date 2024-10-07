# global variables and function parameters can have same name and be different
# The scope can be global or local and the same name can exist as both, yet they are independent items


model_number = 7  # this variable has global scope


def models(model_number):  # this parameter has local scope even though it has same name as above
    print(model_number)  # prints local scope value
    model_number = 5  # local scope variable value changed
    print(model_number)  # prints local scope value


models(model_number)  # calls models function and passes value to it's local scope parameter
print(model_number)  # prints global scope variable value
