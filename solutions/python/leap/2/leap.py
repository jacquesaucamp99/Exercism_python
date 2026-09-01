def leap_year(year):
    # if the year is divisible by 4
    if year % 4 == 0:
        # if the year is not divisible by 100
        if year % 100 == 0:
            # if the year is also divisble by 400 then it is a leap year
            if year % 400 == 0:
                print ("{year} was a leap year!")
                return True
            else :
                print ("{year} was not a leap year as it is not divisble by 400.")
                return False
        
        print ("{year} was a leap year!")
        return True
    else :
        print ("{year} was not a leap year as it is not divisble by 4")
        return False
        
        
    


