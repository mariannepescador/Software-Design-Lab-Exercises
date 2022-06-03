class Rational(object):
    def __init__(self, numer, denom) :
        self.numer = numer
        self.denom = denom
        self._reduce()

    def numerator(self):
        return self.numer

    def denominator(self):
        return self.denom

    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)

    def _reduce(self):
        divisor = self._gcd(self.numer, self.denom)
        self.numer = self.numer // divisor
        self.denom = self.denom // divisor

    def _gcd(self, a, b):
        (a, b) = (max(a, b), min(a, b))
        while b > 0:
             (a, b) = (b, a % b)
        return a