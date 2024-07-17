from math import sqrt


class Elgaml:
    def __init__(self, p, alpha, beta, a, m):
        self.p = p
        self.m = m
        self.alpha = alpha
        self.beta = beta
        self.a = a
        print(f'First, we need to chose k. k is a random number between 1 and {p-1} that - gcd(k, {p-1}) = 1')
        self.k = self.find_creator(p-1)
        if self.k == -1:
            print(f"No creator found for the group Z_{p}")
            return
        print(f'The random number k is {self.k}')
        self.gama:int = (self.alpha**self.k) % self.p
        self.delta:int = ((self.m - (self.a*self.gama))*pow(self.k, -1, self.p-1))%(self.p-1)

    def find_creator(self, n:int) -> int:
        for a in range(2, n):
            if self.__gcd(a, n) != 1:
                continue
            if self.__is_a_creator(n, a):
                return a
        return -1

    def __gcd(self, num_1:int, num_2:int)->int:
        if num_1 == 0:
            return 0
        return num_1 if num_2 == 0 else self.__gcd(num_2, num_1%num_2)
    

    def __factor(self, n:int) -> list:
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
    
    def __is_a_creator(self, n:int, a:int) -> bool:
        factors: list = self.__factor(n-1)
        for f in factors:
            if ((a**((n-1)//f)) % n) == 1:
                return False
        return True
    
    def sign(self):
        print(f"k^-1 = {self.k}^-1 mod {self.p-1} = {pow(self.k, -1, self.p-1)}")
        print(f"\ngama = alpha^k mod p = {self.alpha}^{self.k} mod {self.p} = {self.gama}")
        print(f"delta = (m - a*gama)*k^-1 mod p-1 = ({self.m} - {self.a}*{self.gama})*{pow(self.k, -1, self.p-1)} mod {self.p-1} = {self.delta}\n")
        print(f"The signature is: ({self.gama}, {self.delta})")
        return (self.gama, self.delta)
    

    def verify(self):
        print(f'Verifying the signature ({self.gama}, {self.delta})')
        print(f'\nbeta^gama * gama^delta mod p = {self.beta}^{self.gama} * {self.gama}^{self.delta} mod {self.p} = {(pow(self.beta, self.gama, self.p) * pow(self.gama, self.delta, self.p))%1553} mod {self.p}')
        print(f'alpha^m mod p = {self.alpha}^{self.m} mod {self.p} = {pow(self.alpha, self.m, self.p)} mod {self.p}\n')
        print("chack if the two values are equal!")


if __name__ == "__main__":
    p = 1553
    alpha = 5
    beta = 1356
    a = 300
    # --- message ---
    m=123
    # ---------------

    elgamal = Elgaml(n, alpha, beta, a, m)
    elgamal.sign()
    elgamal.verify()
