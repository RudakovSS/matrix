def add_everything_up(a, b):

    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(23, 'df'))
print(add_everything_up('tree', 34444))
