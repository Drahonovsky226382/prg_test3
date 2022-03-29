def is_whole_number(number):
    if number == int(number):
        vystup = True
    else:
        vystup = False

    return vystup

my_number = 11
print(is_whole_number(my_number))
