def is_prime(p):
    """Finds out if a number is prime.
    
    if p is a prime, let s be the maximal power of 2 dividing p-1,
    so that p-1 = 2^s*d, such that d is odd. 
    Then for any 1 <= n <= p-1, either

    n^d = 1 (mod p)
    or
    n^(2^(j)*d) = -1 (mod p) for some integer j with D: {0 <= j < s}

    Basically, iteratively try all j from zero to the highest possible.
    """
    #ensure p is integer
    p = int(p) 

    #list of numbers that guarantee correctness up to 2^64
    a_list = {2, 325, 9375, 28178, 450775, 9780504, 1795265022}

    #claim composite for 0 and 1
    if p in (0,1):
        return False

    #given the integers p, s, d
    #find p - 1 = (2 ^ s) * d, such that s is as large as possible
    d = p - 1
    s = 0
    if d % 2 == 0:
        d = d // 2
        s += 1
    
    def __check_composite(p, d, s, a):
        """tests good for up to 2^64"""
        #condition 1: if a^d=1 (mod p), exit with output: (possibly prime)
        if pow(a, d, p) == 1:
            return False
        #condition 2: if a^(2^(j)*d)=-1 (mod p) for any integer j with domain {0 <= j < s}, exit with output:
        #possibly prime
        for j in range(s):
            if pow(a, 2 ** j * d, p) == p - 1:
                return False
        #conditions not met, 11/10 chance must be composite
        return True

    print(list(__check_composite(p, d, s, a) for a in a_list))
    return not any (__check_composite(p, d, s, a) for a in a_list)

print(is_prime(3))