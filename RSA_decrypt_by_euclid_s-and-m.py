class RsaEncoding:
    def __init__(self, n, e_a, e_b, c_a, c_b):
        self.n = n
        self.e_a = e_a
        self.e_b = e_b
        self.c_a = c_a
        self.c_b = c_b

        print("In this capter we calculate the private key d using the extended Euclidean algorithm.", end="\n\n")
        self.s, self.t = self.__euclidean_algorithm(self.e_a, self.e_b)

        print("Now we calculate:", end="\n\n")
        print(f'C_a^s*C_b^t = m^(se_a)*m^(te_b) = m^(se_a + te_b) = m (mod {self.n})', end="\n\n")
        ca, cb = self.__decript()
        print('\n============================')
        print(f'The message is: {ca}X{cb} = {ca*cb%self.n} (mod {self.n})')
        print("============================")
    

    def __euclidean_algorithm(self, e_a, e_b):
        r = [e_b, e_a]
        q = []

        while r[-1] != 0:
            q.append(r[-2] // r[-1])
            r.append(r[-2] % r[-1])
        r = r[:-1]
        
        s = [0, 1]
        t = [1, 0]
        c = -1
        for i in range(2, len(q)+1):
            s.append(c*((abs(s[i - 1])*q[i - 2])+abs(s[i - 2])))
            c *= -1
            t.append(c*((abs(t[i - 1])*q[i - 2])+abs(t[i - 2])))

        for i in range(len(r)):
            if not i:
                print(f'{i = }, r = {r[i]},        s = {s[i]}, t = {t[i]}')
            else:
                print(f'{i = }, r = {r[i]}, q = {q[i-1]}, s = {s[i]}, t = {t[i]}')
        print("-----------------")
        print(f'we got that {r[-1]} = {e_a}*({s[-1]}) + {e_b}*({t[-1]})')
        print("-----------------")
        print("So:")
        print(f"The value of s is {s[-1]}")
        print(f"The value of t is {t[-1]}")
        print("-----------------")
        return (s[-1], t[-1])
    

    def __decript(self):
        if self.s < 0:
            z, c = self.__eu_sm(self.s, self.c_a)
            ca =  self.__square_and_mul(c, z, self.t, self.c_b)
            print('\n============================')
            print('Now we calculate:')
            print(f'{self.c_b}^{self.t} = (mod {self.n})', end="\n\n")
            cb = self.__square_and_mul(self.t, self.c_b, self.t, self.c_b)
            return (ca, cb)
        
        z, c = self.__eu_sm(self.t, self.c_b)
        cb = self.__square_and_mul(c, z, self.t, self.c_b)
        print('\n============================')
        print('Now we calculate:')
        print(f'{self.c_a}^{self.s} = (mod {self.n})', end="\n\n")
        ca = self.__square_and_mul(self.s, self.c_a, self.s, self.c_a)
        return (ca, cb)


    def __square_and_mul(self, c, z, ts, c_ab):
        c_bit = []
        temp_c = c
        s_k = []
        r_k = []

        while temp_c != 0:
            if temp_c % 2 == 0:
                c_bit.insert(0, 0)
            else:
                c_bit.insert(0, 1)
            temp_c >>= 1
        print(f"{c} in binary is {c_bit}")

        k = 0
        z_new = 1
        for i in range(len(c_bit)):
            print("-----------------------------")
            print(f'{i = }')
            print(f'e_i = {c_bit[i]}')
            
            if k == 0:
                s_k.append(1)
                k += 2
                print(f'z^2 = 1 (mod {self.n})')
            else:
                z_new = (z_new**2)%self.n
                s_k.append(z_new)
                print(f'z^2 = {s_k[-2]}^2 = {s_k[-1]} (mod {self.n})')

            if c_bit[i] == 1:
                z_new = (z_new*z)%self.n
                r_k.append(z_new)
                print(f'z*{z} = {z_new}*{z} = {r_k[-1]} (mod {self.n})')
        print("-----------------------------")
        print(f'And we got that {c_ab}^{ts} = {z_new} (mod {self.n})')
        return z_new
    

    def __eu_sm(self, s_st, c_ab):
        print(f"Calculate {c_ab}^{s_st}:")
        print(f'First we need to calculate the inverse of {c_ab}: {c_ab}^-1 = {c_ab}^-1 (mod {self.n})')
        print(f'Now we calculate it using the extended Euclidean algorithm:')
        s, t = self.__euclidean_algorithm(c_ab, self.n)
        print(f'The inverse of {c_ab} is {s} (mod {self.n})')
        print(f'{c_ab}^-1 = {s} = {s%self.n} (mod {self.n})')

        s = s%self.n

        print(f"Now we calculate {c_ab}^{s_st} = {s}^{s_st*-1} (mod {self.n}):")

        print(f'using the square and multiply algorithm:')

        return (s, s_st*-1)


if __name__ == "__main__":
    n = 16157
    e_a = 17
    e_b = 33
    c_a = 13910
    c_b = 11449

    rsa = RsaEncoding(n, e_a, e_b, c_a, c_b)
