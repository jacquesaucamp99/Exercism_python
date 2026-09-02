def steps(number):
    number_of_steps = 0

    if number > 0:
        while number > 1:
            # If it is an even number divide by 2
            if number % 2 == 0:
                number /= 2
            # if it is an odd number, multiply by 3 and add 1
            else:
                number *= 3
                number += 1

            number_of_steps += 1

        return number_of_steps
    else:
        raise ValueError("Only positive integers are allowed")
        
        
