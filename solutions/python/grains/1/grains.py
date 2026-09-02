def square(number):
    if 1 <= number <= 64:
        return pow( 2, number - 1 )
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    square_count = 1
    total_grains = 0
    while square_count <= 64:
        total_grains += pow( 2, square_count - 1 )
        square_count += 1

    return total_grains
        
