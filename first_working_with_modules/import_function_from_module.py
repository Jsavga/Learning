# import a specific function from a module:            from first_module import make_pizza
# this is useful if you have more than one function in a module but only need a specific function


from first_module import make_pizza

make_pizza('jalapenos', 'cheese')
make_pizza('cheese')
make_pizza('cheese', 'peppers', 'ham')
