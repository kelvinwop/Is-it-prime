import time

def is_prime(p, DEBUG = False):
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

    #
    #program dun goofs if witness is greater or equal to p-2 so we need to hardcode in tiny values
    #claim composite for 0, 1, 4
    #
    if p in (0, 1, 4):
        return False

    #
    #claim prime for 2, 3
    #
    if p in (2, 3):
        return True

    #given the integers p, s, d
    #find p - 1 = (2 ^ s) * d, such that s is as large as possible
    d = p - 1
    s = 0
    while d % 2 == 0:
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

    #debugging the crazy
    if DEBUG:
        print(p, d, s)
        print(list(__check_composite(p, d, s, a) for a in a_list if a<p-2))
    return not any (__check_composite(p, d, s, a) for a in a_list if a<p-2)

start_time = time.time()
print([i for i in range(2000000000000,2000000001000) if is_prime(i)])
end_time = time.time()

print("Execution time: " + str(end_time - start_time) + " seconds")

#output
#[2000000000003, 2000000000123, 2000000000137, 2000000000153, 2000000000179, 2000000000197, 
#   2000000000203, 2000000000231, 2000000000237, 2000000000267, 2000000000303, 2000000000381, 
#   2000000000419, 2000000000443, 2000000000447, 2000000000473, 2000000000477, 2000000000483, 
#   2000000000489, 2000000000491, 2000000000527, 2000000000573, 2000000000611, 2000000000617, 
#   2000000000623, 2000000000629, 2000000000633, 2000000000681, 2000000000683, 2000000000707, 
#   2000000000729, 2000000000737, 2000000000759, 2000000000777, 2000000000783, 2000000000809, 
#   2000000000927, 2000000000981, 2000000000983]
#Execution time: 0.026900529861450195 seconds