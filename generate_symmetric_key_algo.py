from random import randint


def gcd(num_1:int, num_2:int)->int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


def generate_key(p, k):
    print(f"We are going to send a symmetric key {k = } using the following algorithm:")
    print('--------------------------------------------',end="\n\n")
    print(f"1. Alice generates a random number 'a' from 'Z*_{p-1}'.")
    a = randint(1, p-1)
    while gcd(a, p-1) != 1:
        a = randint(1, p-1)
    a_1 = pow(a, -1, p-1)
    print(f"{a = }")
    print(f"a^1 = {a_1}",end="\n\n")
    
    print(f"2. Bob generates a random number 'b' from 'Z*_{p-1}' to.")
    b = randint(1, p-1)
    while gcd(b, p-1) != 1:
        b = randint(1, p-1)
    b_1 = pow(b, -1, p-1)
    print(f"{b = }")
    print(f"b^1 = {b_1}",end="\n\n")
    
    K_1 = (k ** a) % p
    K_2 = (K_1 ** b) % p
    print(f"3. Alice calculates K_1 = (k^a) mod p = ({k}^{a}) mod {p} = {K_1}")
    print(f"And then sends K_1 to Bob.",end="\n\n")

    print(f"4. Bob calculates K_2 = (K_1^b) mod p = ({K_1}^{b}) mod {p} = {K_2}")
    print(f"And then sends K_2 to Alice.",end="\n\n")
    
    K_3 = (K_2 ** b_1) % p
    K_4 = (K_3 ** a_1) % p

    print(f"5. Alice calculates K_3 = (K_2^(-a)) mod p = ({K_2}^(-{a})) mod {p} = {K_3}")
    print(f"And then sends K_3 to Bob.",end="\n\n")

    print(f"6. Bob calculates K_4 = (K_3^(-b)) mod p = ({K_3}^(-{b})) mod {p} = {K_4}")
    print(f"And then sends K_4 to Alice.",end="\n\n")

    print('============================================')
    print(f"final we have {K_4 = } which is the symmetric key {k = }.")
    print(f"{K_4 = }, {k = }")
    print('============================================',end="\n\n")


if __name__ == "__main__":
    p = 2003
    k = 111
    symmetric_key = generate_key(p, k)