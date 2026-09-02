def check_eligibility(sides):
    if sides[0] + sides[1] >= sides[2]:
        if sides[1] + sides[2] >= sides[0]:
            if sides[0] + sides[2] >= sides[1]:
                return True
    return False

def equilateral(sides):

    if check_eligibility(sides):
        if sides[0] == sides[1]:
            if sides[1] == sides[2]:
                if sides[0] != 0:
                    return True

    return False


def isosceles(sides):

    if check_eligibility(sides):
        if sides[0] == sides[1]:
            return True
        elif sides[0] == sides[2]:
            return True
        elif sides[1] == sides[2]:
            return True

    return False

def scalene(sides):

    if check_eligibility(sides):
        if sides[0] != sides[1]:
            if sides[1] != sides[2]:
                if sides[0] != sides[2]:
                    return True
            
    return False
