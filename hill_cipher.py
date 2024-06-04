# import numpy as np

# class HillCipher:
#     def __init__(self, o_text:str, e_text:str, key:int):
#         self.__original_text = o_text
#         self.__encrypted_text = e_text
#         self.__original_text_lst = [c for c in self.__original_text if c.isalpha()]
#         self.__encrypted_text_lst = [c for c in self.__encrypted_text if c.isalpha()]
#         self.__key = key
#         self.__original_matrix = np.array([])
#         self.__encrypted_matrix = np.array([])
#         self.__inverse_matrix_original_indexes:list = []
#         self.__P = self.__get_original_matrix()
#         self.__Q = self.__get_encrypted_matrix()
#         self.__P_1 = np.linalg.inv(self.__P)%26
#         print(type(self.__P_1[0][0]))
#         self.__key_matrix = np.array([])
#         self.__decripted_key_matrix = np.array([])


#     def proccess(self):
#         self.__key_matrix = (self.__Q @ self.__P_1) % 26
#         print(f'{self.__Q = } {self.__P_1 = }')
#         print(f'{(self.__Q @ self.__P_1) = }')
#         print(f'{self.__key_matrix = }')
    
    
#     def __gcd(self, num_1:int, num_2:int)->int:
#         if num_1 == 0:
#             return 0
#         return num_1 if num_2 == 0 else self.__gcd(num_2, num_1%num_2)
    
    
#     def __get_encrypted_matrix(self):
#         matrix_l = np.array([])
#         matrix_r = np.array([])
#         l_index = self.__inverse_matrix_original_indexes[0]
#         r_index = self.__inverse_matrix_original_indexes[1]
#         l = 0
#         r = 0
#         if self.__encrypted_text_lst[l_index[0]] >= 'a' and self.__encrypted_text_lst[l_index[0]] <= 'z':
#             l = ord(self.__encrypted_text_lst[0])-ord('a')
#         elif self.__encrypted_text_lst[l_index[0]] >= 'A' and self.__encrypted_text_lst[l_index[0]] <= 'Z':
#             l = ord(self.__encrypted_text_lst[0])-ord('A')

#         if self.__encrypted_text_lst[l_index[1]] >= 'a' and self.__encrypted_text_lst[l_index[1]] <= 'z':
#             r = ord(self.__encrypted_text_lst[1])-ord('a')
#         elif self.__encrypted_text_lst[l_index[1]] >= 'A' and self.__encrypted_text_lst[l_index[1]] <= 'Z':
#             r = ord(self.__encrypted_text_lst[1])-ord('A')

#         matrix_l = np.array([l, r])

#         l = 0
#         r = 0
#         if self.__encrypted_text_lst[r_index[0]] >= 'a' and self.__encrypted_text_lst[r_index[0]] <= 'z':
#             l = ord(self.__encrypted_text_lst[2])-ord('a')
#         elif self.__encrypted_text_lst[r_index[0]] >= 'A' and self.__encrypted_text_lst[r_index[0]] <= 'Z':
#             l = ord(self.__encrypted_text_lst[2])-ord('A')
        
#         if self.__encrypted_text_lst[r_index[1]] >= 'a' and self.__encrypted_text_lst[r_index[1]] <= 'z':
#             r = ord(self.__encrypted_text_lst[3])-ord('a')
#         elif self.__encrypted_text_lst[r_index[1]] >= 'A' and self.__encrypted_text_lst[r_index[1]] <= 'Z':
#             r = ord(self.__encrypted_text_lst[3])-ord('A')

#         matrix_r = np.array([l, r])

#         return np.array((matrix_l, matrix_r))
    

#     def __get_original_matrix(self):
#         matrix = np.array([])
#         matrix_l = np.array([])
#         matrix_r = np.array([])
#         for c1 in range(len(self.__original_text_lst)-3):
#             l = 0
#             r = 0
#             if self.__original_text_lst[c1] >= 'a' and self.__original_text_lst[c1] <= 'z':
#                 l = ord(self.__original_text_lst[c1])-ord('a')
#             elif self.__original_text_lst[c1] >= 'A' and self.__original_text_lst[c1] <= 'Z':
#                 l = ord(self.__original_text_lst[c1])-ord('A')

#             if self.__original_text_lst[c1+1] >= 'a' and self.__original_text_lst[c1+1] <= 'z':
#                 r = ord(self.__original_text_lst[c1+1])-ord('a')
#             elif self.__original_text_lst[c1+1] >= 'A' and self.__original_text_lst[c1+1] <= 'Z':
#                 r = ord(self.__original_text_lst[c1+1])-ord('A')

#             matrix_l = np.array([l, r])
#             for c2 in range(c1+2, len(self.__original_text_lst)-1):
#                 l = 0
#                 r = 0
#                 if self.__original_text_lst[c2] >= 'a' and self.__original_text_lst[c2] <= 'z':
#                     l = ord(self.__original_text_lst[c2])-ord('a')
#                 elif self.__original_text_lst[c2] >= 'A' and self.__original_text_lst[c2] <= 'Z':
#                     l = ord(self.__original_text_lst[c2])-ord('A')
                
#                 if self.__original_text_lst[c2+1] >= 'a' and self.__original_text_lst[c2+1] <= 'z':
#                     r = ord(self.__original_text_lst[c2+1])-ord('a')
#                 elif self.__original_text_lst[c2+1] >= 'A' and self.__original_text_lst[c2+1] <= 'Z':
#                     r = ord(self.__original_text_lst[c2+1])-ord('A')

#                 matrix_r = np.array([l, r])
#                 matrix = np.array((matrix_l, matrix_r), dtype=np.int64)
#                 determinant = round(np.linalg.det(matrix)%26)
                
#                 print(f'{determinant = } {matrix = }')
#                 print(f'{self.__gcd(determinant, 26) = }')
#                 if self.__gcd(determinant, 26) == 1:
#                     self.__inverse_matrix_original_indexes.append([c1, c1+1])
#                     self.__inverse_matrix_original_indexes.append([c2, c2+1])
#                     print(f'{self.__inverse_matrix_original_indexes = }')
#                     return matrix


# if __name__ == "__main__":
#     # original_text:str = "Victor has read this text from Trent"
#     # encrypted_text:str = "Lzlgxu jpr kuqq xtvn sneu ffhj uztol"

#     original_text:str = "cryptoanalysis"
#     encrypted_text:str = "mzkrnyankzimmk"

#     key = 2
#     hill_cipher = HillCipher(original_text, encrypted_text, key)
#     hill_cipher.proccess()