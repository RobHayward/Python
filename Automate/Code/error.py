def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Erroe: You tried to divide by zero')
print(div42by(0))
print(div42by(12))
print(div42by(1))