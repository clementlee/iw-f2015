from sage.all import *

class FastPolyEval:

    #preprocesses the polynomial
    def __init__(self, f):
        ring = f.parent()
        self.q = ring.modulus()
        self.n = f.degree()
        self.origf = f

        #calculates the phi mapping to get the value of f
        self.phi(self.n, 1)

    def phi(self, h, l):
        coeffs = list(reversed(self.origf.list()))
        #print coeffs
        maxlen = len(str(l))
        yss = ['y'+str(i).zfill(maxlen) for i in xrange(l)]
        self.ring = PolynomialRing(Integers(self.q), yss)
        ys = [self.ring.gen(n = i) for i in xrange(l)]
        print yss
        print ys

        self.f = 0
        for a in xrange(len(coeffs)):
            print "hi"
            #base = list(reversed(Integer(a).digits(h)))
            base = Integer(a).digits(h)
            print base
            m = 1
            for j in xrange(len(base)):
                if j >= l:
                    break
                print ys[j]
                print base[j]
                m *= ys[j]**base[j]
            print "endloop"
            print coeffs[a]
            print m
            print coeffs[a]*m
            self.f += coeffs[a]*m
        print "asdf"
        print self.f
        print "asdf"





    #evaluates it at a point $a$
    def ev(self, a):
        pass

if __name__ == '__main__':
    x = PolynomialRing(Integers(10), 'x').gen()
    f = x**2 + 3
    a = FastPolyEval(f)
