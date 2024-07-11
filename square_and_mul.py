# def square_and_mul(c, z):
#     c_bit = []
#     temp_c = c
#     s_k = []
#     r_k = []

#     while temp_c != 0:
#         if temp_c % 2 == 0:
#             c_bit.insert(0, 0)
#         else:
#             c_bit.insert(0, 1)
#         temp_c >>= 1
#     print(f"{c} in binary is {c_bit}")

#     k = 0
#     for i in range(len(c_bit)):
#         s_k.append((c_bit[i]**k)%self.n)
#         if k == 0:
#             k += 2
#         if i == 0:
#             r_k.append()
#         else:
#             r_k.append((s_k[-1]*z)%self.n)
            


# if __name__ == "__main__":
#     square_and_mul(8, 5658)