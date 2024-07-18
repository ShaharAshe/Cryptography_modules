from math import sqrt


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

if __name__ == "__main__":
    n = 223
    a = 3
    if is_a_creator(n, a):
        print("\n")
        print(f"YES {a} is a creator of the group Z_{n}")
    else:
        print("\n")
        print("NO")
        print(f"{a} is NOT a creator of the group Z_{n}")
