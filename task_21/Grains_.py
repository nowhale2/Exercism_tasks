def square(number):
    result = 0
    if 1 <= number <= 64:
        if number == 1:
            result = 1
        else:
            result = 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")
    return result
            
def total():
    return 2**64 - 1
