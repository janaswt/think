from oop_digging.gcd import gcd
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def get_num(self): 
        return self.num
    def get_den(self):
        return self.den
    def simplify(self):
        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common
    def add(self, other_fraction):
        new_num = self.num * other_fraction.get_den() + self.den * other_fraction.get_num()
        new_den = self.den * other_fraction.get_den()
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.get_den() + self.den * other_fraction.get_num()
        new_den = self.den * other_fraction.get_den()
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
   
my_fraction = Fraction(15, 12)
print(my_fraction)
print(my_fraction.get_num())
print(my_fraction.get_den())
my_fraction.simplify()
print(my_fraction)
f1 = Fraction(3, 4)
f2 = Fraction(2, 5)

f3 = f1 + f2
print(f3)

