import math 

def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1 * denom2 + denom1 * numer2
    denom = denom1 * denom2
    gcd = math.gcd(numer, denom)
    
    if numer % gcd == 0:
        first = numer/gcd
        second = denom/gcd
        answer=[first, second]
    else:
        answer=[numer, denom]
    return answer