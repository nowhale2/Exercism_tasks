def classify(number):
    """ A perfect number equals the sum of its positive divisors.
 
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    summa = 0
    result = ""
    for i in range(1, number):
        if number % i == 0:
            summa += i
    if summa > number:
        result = "abundant"
    if summa == number:
        result = "perfect"
    if summa < number:
        result = "deficient"
    return result
