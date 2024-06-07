from math import sqrt

def factor(n):
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


if __name__ == "__main__":
    n = 348
    factors = factor(n)
    print(f"The factors of {n} are: {factors}")