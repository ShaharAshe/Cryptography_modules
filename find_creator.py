from math import sqrt


def gcd(num_1:int, num_2:int)->int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


def factor(n:int) -> list:
    temp_n = n
    factors = []
    while temp_n != 1:
        for i in range(2,int(sqrt(temp_n))):
            if temp_n % i == 0:
                if i not in factors:
                    factors.append(i)
                temp_n = temp_n // i
                break
        else:
            factors.append(temp_n)
            return factors
    return factors


def is_a_creator(n:int, a:int) -> bool:
    print(f"To check if {a} is a creator of the group Z_{n} we will calculate the following:\n")
    print("--------------------")
    print(f"1. Check what are the factors of {n-1 = }:\n")
    factors: list = factor(n-1)
    print(f"The factors of {n-1} are: {factors}")
    print("--------------------")
    print(f"2. Check if", end="\n\n")
    for f in factors:
        print(f"{a}^{(n-1)//f} != 1 mod {n}")
    else:
        print()
    print(f"for all factors of {n-1}")
    print(f"if they are all not equal to 1 then {a} is a creator of the group Z_{n}")
    print("--------------------", end="\n\n")
    for f in factors:
        print(f"{a}^{(n-1)//f} = {(a**((n-1)//f)) % n} mod {n}")
    for f in factors:
        if ((a**((n-1)//f)) % n) == 1:
            return False
    return True


def find_creator(n:int) -> int:
    for a in range(2, n):
        if gcd(a, n) != 1:
            continue
        print("_______________________________________________________________________")
        if is_a_creator(n, a):
            print(f"{a} is a creator of the group Z_{n}")
            return a
        print("_______________________________________________________________________")
    return -1

if __name__ == "__main__":
    n = 1553
    a = find_creator(n)
    # if a == -1:
    #     print(f"No creator found for the group Z_{n}")
    # else:
    #     print(f"The creator of the group Z_{n} is {a}")
    
