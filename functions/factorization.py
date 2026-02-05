from typing import List

def get_factors(num: int, prime: bool = False) -> List[int]:
    """
    Returns a list of factors for the provided integer
    
    Args: 
        num(int): the number for which we want factors
        prime(bool): whether to return only prime factor 
        or all factors
        
    Return:
        List[int]: list of factors
    """
    if type(num) is not int:
        raise TypeError("num must be an int")
    if num <= 0:
        raise ValueError("num must be greater than 0")
    
    factors: List[int] = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
            
    if prime:
        factors = [
            f for f in factors 
            if len(get_factors(f, prime=False))== 2]
    return factors 

get_factors(1778294, prime=True)        