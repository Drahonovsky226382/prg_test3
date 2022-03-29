def is_natural_number(number):
    if number % 1 == 0 and number > 0:
        return True
    return False


def is_even_number(number):
    if number % 2 == 0:
        return True
    return False

def is_natural_number():
    for my_number in my_numbers:
        print(my_number)



my_numbers = [2, 4, 8, 9, 10]
print(is_natural_number(my_numbers))
print(is_even_number(my_numbers))
