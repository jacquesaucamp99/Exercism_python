def is_armstrong_number(number):

    # split number into a list of digits
    digits = [int(d) for d in str(number)]

    # loop through the list and find the sum
    digit_sum = 0
    for digit in digits:
        digit_sum += pow( digit, len( digits ) )

    if digit_sum == number:
        return True

    return False
        
    
        
