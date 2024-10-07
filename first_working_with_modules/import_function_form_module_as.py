# import a specific function from a module:            from first_module import make_pizza
# and then assign function an alias name with "as":    from first_module import make_pizza as toppings


from first_module import make_pizza as toppings

toppings('jalapenos', 'cheese')
toppings('cheese')
toppings('cheese', 'peppers', 'ham')
