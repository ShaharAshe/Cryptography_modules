class UniversalExponent:
    def __init__(self, n, d, e):
        self.n = n
        self.d = d
        self.e = e
        self.a = 2
        self.ed_sub_1 = self.__factorize((d*e)-1)
        
        print("\n================")
        print(f"we got:")
        print(f"n = {self.n}")
        print(f"d = {self.d}")
        print(f"e = {self.e}")
        print("================\n")

        print(f"ed-1 = {(self.e*self.d)-1} = 2^{self.ed_sub_1[0]}*{self.ed_sub_1[1]} = 2^{self.ed_sub_1[0]}*r")
        
    def __gcd(self, num_1:int, num_2:int)->int:
        if num_1 == 0:
            return 0
        return num_1 if num_2 == 0 else self.__gcd(num_2, num_1%num_2)
    
    def __find_a(self, n:int)->None:
        self.a += 1
        while True:
            if (self.__gcd(self.a, n) != 1):
                self.a += 1
            else:
                break

    def __factorize(self, n:int) -> tuple[int, int]:
        k:int = 0
        while n % 2 == 0:
            n //= 2
            k += 1
        return (k, n)
    
    def process(self):
        while True:
            print("_____________________________________________________")
            print(f"a = {self.a}:")
            print("---------------------------------")
            pow_ex = pow(self.a, self.ed_sub_1[1], self.n)
            print(f"{self.a}^r = {pow_ex} mod {self.n}")
            for i in range(self.ed_sub_1[0]):
                pow_ex_temp = pow(pow_ex, 2, self.n)
                print(f"{pow_ex}^2 = {pow_ex_temp} mod {self.n}")
                if pow_ex_temp == 1:
                    break
                elif pow_ex_temp == -1:
                    print("[ERROR] - The algorithm failed because the number is not a prime number")
                    print("_____________________________________________________")
                    return
                else:
                    pow_ex = pow_ex_temp
            print("---------------------------------")
            if pow(pow_ex, 2, self.n) == 1:
                decompose_1 = self.__gcd(pow_ex-1, self.n)
                decompose_2 = 0
                if decompose_1 != 0:
                    decompose_2 = self.n//decompose_1
                print(f"Decomposition of n: {self.n} = {decompose_1}*{decompose_2}")
                print("_____________________________________________________")
                return
            else:
                print(f"{self.a} is not a universal exponent lets try another number")
                self.__find_a(self.n)
                print(f"New a: {self.a}")
                


if "__main__" == __name__:
    n = 11639
    d = 90919
    e = 19

    ue = UniversalExponent(n, d, e)
    ue.process()
    
