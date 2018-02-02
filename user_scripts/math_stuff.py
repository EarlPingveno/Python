def cross_sum(number):
    """
    Calculating the cross sum of a number
    """
    if number < 0:
        return False
    print "LOG: function cross_sum has been called with value:", number
    result = 0
    while number:
        result += number % 10
        number //= 10
    return result
