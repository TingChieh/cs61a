def shift(k, f):
    """Return a function of x that returns f(x+k).
    
    >>> square = lambda x: x * x
    >>> g = shift(2, square)
    >>> g(3)    # square(3 + 2)
    25
    """
    # def shifted(one):
    #     return f(k + one)
    # return shifted -> return lambda x: f(x + k)
    return compose(f, lambda x: x + k)

def compose(f, g):
    """Return a function that takes x and calls f on g of x."""
    return lambda x: f(g(x))

def summation(n, term):
    """Sum the first n terms of a sequence: term(1) + term(2) + ... + term(n).
    >>> summation(5, lambda x: x*x) # 1*1 + 2*2 + 3*3 + 4*4 + 5*5
    55
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_range(p, q, term):
    """Sum terms p through q of a sequence: term(p) + term(p+1) + ... + term(q).
    >>> sum_range(1, 5, lambda x: x*x) # 1*1 + 2*2 + 3*3 + 4*4 + 5*5
    55
    >>> sum_range(4, 5, lambda x: x*x) # 4*4 + 5*5
    41
    >>> sum_range(5, 5, lambda x: x*x) # 5*5
    25
    """
    assert p <= q
    return summation(q - p + 1, shift(p - 1, term))