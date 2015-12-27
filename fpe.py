#fast polynomial evalution

#theorem 5.1, take subcase where R is a field

from sage.all import *
import random
import time

r = 7#6997 #an arbitarily large prime
x = GF(r)['x'].gen()
f = 0
#for i in xrange(5000):
#    f = f + random.randint(0, r) * x**i

f = x**2+2*x+1#3*x**2 + 2*x + 1
print f
n = f.degree()
q = r
rprime = r

if rprime > 2^(2^n):
    d = n
    t = 2
    m = 1
else:
    # d and m depend on a constant? what constant c is there
    d = n
    t = 4
    m = 1

#definition 2.3 only kicks in if m \neq 1 which is not the case for the constants chosen
phi = f

d = n+1 #i think this is the definition required?
#e is fixed to 0 for now
#TODO: make this work for extension rings and not just fields
e = 0
M = d^m*(e*(r-1))**((d-1)*m+1)
rsomething = M**((e-1)*d*m +1) #figure our how this works

fbar = f

#generate primes
l = int(16*log(d*(r-1)**d,2))
print l
print r
p = [2]
cummul = 1
for i in xrange(3, l+1, 2):
    if cummul > r:
        break
    #if i > r:
    #    break
    isPrime = True
    for prime in p:
        if i % prime == 0:
            isPrime = False
            break
    if isPrime:
        p.append(i)
        cummul *= i

fh = []

for prime in p:
    #fh.append(fbar % (x**prime - x))
    fh.append(GF(prime)['x'](fbar.mod(x**prime - x)))


evals = []
for i in xrange(len(fh)):
    func = fh[i]
    prime = p[i]
    ev = []
    for j in xrange(prime):
        ev.append(Integer(func(j)))
    evals.append(ev)

print evals

def evalf(n):
    n = n % r
    lookups = []
    for i in xrange(len(p)):
        prime = p[i]
        modulo = n % prime
        print "%d mod %d = %d with eval %d" % (n, prime, modulo, evals[i][modulo])
        lookups.append(evals[i][modulo])
    num = lookups[0]
    mod = p[0]
    for i in xrange(1, len(lookups)):
        num1 = lookups[i]
        mod1 = p[i]
        print "crt %d\t%d\t%d\t%d\t%d" % (num, num1, mod, mod1, crt(num, num1, mod, mod1))
        num = crt(num, num1, mod, mod1)
        mod = mod*mod1
    return num % r

print evalf(5)
print f(5)
#tests = 10000
#points = [random.randint(0, r) for _ in xrange(0, tests)]
#start = time.clock()
#evalpoints = [f(point) for point in points]
#end = time.clock()
#print end-start
#
#start = time.clock()
#evalpoints1 = [evalf(point) for point in points]
#end = time.clock()
#print end-start
#
#for i in xrange(10):#len(evalpoints)):
#    ev1 = evalpoints[i]
#    ev2 = evalpoints1[i]
#    if ev1 != ev2:
#        print "Error on %d, should be %d but got %d" % (points[i], ev1, ev2)

