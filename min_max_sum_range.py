digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
value = min(digits)
print(value)
value = max(digits)
print(value)
value = sum(digits)
print(value)

digits = [13, 42, 15, 8, 19, 11, 12]
value = min(digits)
print(value)
value = max(digits)
print(value)
value = sum(digits)
print(value)

# make a list from 1 to 1,000,000

lot_of_numbers = list(range(1, 1000001))
print(lot_of_numbers)
value_sum = sum(lot_of_numbers)
value_min = min(lot_of_numbers)
value_max = max(lot_of_numbers)
print(f"Minimum = {value_min}, Maximum = {value_max} and Sum = {value_sum}.")
