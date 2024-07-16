# import numpy as np


# def gcd(num_1:int, num_2:int)->int:
#         if num_1 == 0:
#             return 0
#         return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


# def hill(original_text, encrypted_text):
#     key=2
#     original_text = [c for c in original_text if c.isalpha()]
#     encrypted_text = [c for c in encrypted_text if c.isalpha()]
#     if len(original_text) != len(encrypted_text):
#         print("Length of original text and encrypted text should be equal")
#         return
    
#     if key:
#         if len(original_text) <= (key*key) or len(encrypted_text) <= (key*key):
#             print("Length of original text and encrypted text should be greater than key*key")
#             return
#     else:
#         print("Key should be greater than 0")
#         return

#     p = []
#     c = []

#     print("_________________________")
#     print(f"The original text:")
#     for i in range(0, key*key):
#         print(f"{original_text[i]} --> {ord(original_text[i]) - ord('a')}")

#     print("\n")
#     for i in range(0, key*key, key):
#         p.append([ord(char) - ord("a") for char in original_text[i:i+key]])
    
#     p = np.transpose(np.array(p))
#     print(f'p =\n{p}', end = '\n\n')

#     print("_________________________")
#     print(f"The encrypted text:")
#     for i in range(0, key*key):
#         print(f"{encrypted_text[i]} --> {ord(encrypted_text[i]) - ord('a')}")
    
#     print("\n")
#     for i in range(0, key*key, key):
#         c.append([ord(char) - ord("a") for char in encrypted_text[i:i+key]])

#     # Convert lists to NumPy arrays with each list entry as a row
    
#     c = np.transpose(np.array(c))
#     print(f'c =\n{c}', end = '\n\n')
#     print("_________________________")


#     det_p = int(np.linalg.det(p))%26
#     print(f"{det_p = }")
#     det_p_inv = 0
#     if(gcd(det_p, 26) != 1):
#         det_p_inv = pow(int(det_p)//2, -1, 13)
#     else:
#         det_p_inv = pow(int(det_p), -1, 26)
#     adj_p = np.array([[p[1,1], -p[0,1]], [-p[1,0], p[0,0]]])
#     inverse_p = det_p_inv * adj_p % 26
#     print(f"\nNow we gona find the inverse of p")
#     print(f'({det_p}^-1)*\n{adj_p} =\n{inverse_p} mod 26', end = '\n\n')

#     K = np.dot(c, inverse_p) % 26
#     print(f'K = c*(p^-1) =\n{c} *\n{inverse_p} mod 26 =\n{K}', end = '\n\n')
#     print("=========================")
#     print(f"And the encryption key is:\n{K}", end = '\n\n')
#     print("=========================")

#     det_k = int(np.linalg.det(K))%26
#     det_k_inv = 0
#     if(gcd(det_k, 26) != 1):
#         det_k_inv = pow(int(det_k)//2, -1, 13)
#     else:
#         det_k_inv = pow(int(det_k), -1, 26)
#     adj_k = np.array([[K[1,1], -K[0,1]], [-K[1,0], K[0,0]]])
#     K_inv = det_k_inv * adj_k % 26
#     print(f"\nNow we gona find the inverse of K")
#     print(f'({det_k}^-1)*\n{adj_k} =\n{K_inv} mod 26', end = '\n\n')
#     print("=========================")
#     print(f"And the decryption key is:\n{K_inv}", end = '\n\n')
#     print("=========================")


# if __name__ == "__main__":
#     original_text:str = "w h e n d i d a l i c e w r i t e t o o s c a r "
#     encrypted_text:str ="nexs mpmf wpbx nkpg xgdd vbfk"
    
#     hill(original_text, encrypted_text)