from math import sqrt


def factor(n):
    temp_n = n
    factors = []
    while temp_n != 1:
        for i in range(2,int(sqrt(temp_n))+1):
            if temp_n % i == 0:
                if i not in factors:
                    factors.append(i)
                temp_n = temp_n // i
                break
        else:
            factors.append(temp_n)
            return factors
    return factors


def euler_phi(n):
    factors:list = factor(n)
    print(f'The factors of {n} are {factors}')
    phi = 1
    print("_________________________")
    print("phi = ", end="")
    for f in factors:
        phi *= (f-1)
        print(f'({f}-1) ', end="")
    print(f'= {phi}')
    print("_________________________")
    return phi


if __name__ == "__main__":
    n = 82
    phi1 = euler_phi(n)
    # print(f'{phi = }')