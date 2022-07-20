def gcd(a, b):
    '''
    INPUT: int, int
    OUTPUT: int

    Return the greatest common divisor of the two integers given.
    '''
    while a != 0:
        c = a
        a = b % a
        b = c
    return b


class Fraction(object):
    '''
    A fraction class.
    '''

    def __init__(self, num, denom):
        '''
        Initialize a fraction with the given numerator and denominator.
        '''
        self.num = num
        self.denom = denom
        self._reduce()

    def _reduce(self):
        '''
        Put the fraction in reduced form.
        '''
        if self.num == 0:
            self.denom = 1
        else:
            d = gcd(self.num, self.denom)
            if (self.denom / d) < 0: 
                d = -1 * d
            self.num = self.num // d
            self.denom = self.denom // d
        return self

    def __add__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return a fraction that is the sum of this fraction and other.
        '''
        return Fraction(self.num * other.denom + other.num * self.denom,
                        self.denom * other.denom)

    def __sub__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return a fraction that is the difference of this fraction and other.
        '''
        return Fraction(self.num * other.denom - other.num * self.denom,
                        self.denom * other.denom)

    def __mul__(self, other):
        '''
        INTPUT:
            - other: Fraction or int
        Return a fraction that is the product of this fraction and other.
        '''
        if isinstance(other, int):
            return Fraction(self.num * other, self.denom)
        return Fraction(self.num * other.num, self.denom * other.denom)

    def __eq__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return True if self == other, False if self != other
        '''
        return (self - other).num ==  0

    def __lt__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return True if self < other, False if self >= other
        '''
        return (self - other).num < 0

    def __gt__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return True if self > other, False if self <= other
        '''
        return (self - other).num > 0

#    def __repr__(self):
#        '''
#        Return a string representation of the fraction.
#        '''
#        return "{0}/{1}".format(self.num, self.denom)
#
if __name__ == '__main__':
    num_1 = 1
    denom_1 = 2
    
    num_2 = 1
    denom_2 = 4
    
    fraction_1 = Fraction(num_1, denom_1)
    print("Fraction 1: {}".format(fraction_1)) 
    fraction_2 = Fraction(num_2, denom_2)
    print("Fraction 2: {}".format(fraction_2))
    
    fraction_added = fraction_1 + fraction_2
    print("Fractions added: {}".format(fraction_added))

    print("\nFraction 1 > Fraction 2?")
    print(fraction_1 > fraction_2)



