def add_everything_up(a, b):
    try:
        return a + b

    except TypeError:
        if isinstance(a, str) == True:
            b = str(b)
            return a + b
        else:
            a = str(a)
            return a + b

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))



