def is_armstrong_number(number):

    # split number into a list of digits
    digits = list(map(int, str(number)))

    # loop through the list and find the sum
    sum = 0
    for d in digits:
        sum += pow( d, len( digits ) )

    if sum == number:
        return True

    return False
        
    
        
