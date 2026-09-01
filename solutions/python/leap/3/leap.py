def leap_year(year):
    # if the year is divisible by 4
    if year % 4 == 0:
        # if the year is not divisible by 100
        if year % 100 == 0:
            
            # if the year is also divisble by 400 then it is a leap year
            if year % 400 == 0:
                print ("{year} was a leap year!")
                return True

            # If the year is divisble by 4 AND 100 but not 400.
            print ("{year} was not a leap year as it is not divisble by 400.")
            return False
            
        # If the year is divisible by 4 and NOT 100
        print ("{year} was a leap year!")
        return True

    # If the year is NOT divisible by 4
    print ("{year} was not a leap year as it is not divisble by 4")
    return False