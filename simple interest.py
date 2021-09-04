p = float(input('enter principal P: '))
t = float(input('enter time period: '))
r = float(input('enter rate of interest R: '))


def simple_int(p,t,r):
    si = (p*t*r)/100

    print('the simple interest is', si)
    return si


simple_int(p,t,r)


# COMPOUND INTEREST
print('###################')


def interest(p,r,t):
    ci = p * (pow((1+ r/100), t))
    print('compound interest is:' ,ci)


interest(p,t,r)


print('############# Area if the circle#########################################')
r = 2

def findArea(r):
    PI = 3.142
    return PI * (r * r);


# Driver method
print("Area is %.2f" % findArea(r));






