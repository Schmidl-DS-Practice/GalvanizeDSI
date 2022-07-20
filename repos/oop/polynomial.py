class Polynomial(object):

    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.poly = 0

    # def evaluate(self, x):
    #     for i in range(len(self.coefficients)):
    #         self.poly += self.coefficients[i] * self.x**i
    #
    #    return self.poly


    def __repr__(self):
        return f'Polynomial({self.coefficients})'

    def __add__(self, other):
        poly_lst = []
        for i in range(len(self.coefficients)):
            a = self.coefficients[i] + other.coefficients[i]
            poly_lst.append(a)
        return Polynomial(poly_lst)

if __name__=='__main__':

    coeff_lst = [1, 2, 3]
    coeff_lst2 = [1, 2, 3]
    poly1 = Polynomial(coeff_lst)
    poly2 = Polynomial(coeff_lst2)
    poly3 = poly1 + poly2