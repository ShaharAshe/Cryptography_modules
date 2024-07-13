import numpy as np
from typing import final


ZERO:final = 0.7
ONE:final = 0.2
TWO:final = 0.1


class VigenereCipher:
    def __init__(self, text:str, time:int=2):
        self.__text:str = text
        self.__decrypt_text:str = text
        self.__text_str:list = [int(c) for c in text if c.isnumeric()]
        self.__first_frequencies_vector:list = []
        self.__get_frequencies_vector()
        self.__time:int = time
        self.__right_frequencies_vector:list = self.__first_frequencies_vector[:]
        self.__right_text_str:list = self.__text_str[:]
        self.__encrypt_key:list = []
        self.__decrypt_key:list = []
    

    def __get_frequencies_vector(self):
        for i in range(len(self.__text_str)):
            if self.__text_str[i] == 0:
                self.__first_frequencies_vector.append(ZERO)
            elif self.__text_str[i] == 1:
                self.__first_frequencies_vector.append(ONE)
            elif self.__text_str[i] == 2:
                self.__first_frequencies_vector.append(TWO)


    def process(self):
        # loop for the key
        sum:int = self.__check_key()
        print("=====================================")

        self.__right_text_str:list = []
        for i in range(1, (len(self.__text_str)//self.__time)+1):
            self.__right_text_str += [self.__text_str[(i-1)*self.__time:i*self.__time]]
        
        self.__decrypt()
        self.get_decrypt_text()


    def get_decrypt_text(self):
        decrypt_lst:list = []
        key_lst:list = []
        for c in self.__right_text_str:
            temp_dec_lst:list = []
            temp_key_lst:list = []
            if len(c):
                temp_dec_lst.append(str((c[0]+self.__decrypt_key[0])%3))
                temp_key_lst.append(str(c[0]))
            if len(c) > 1:
                temp_dec_lst.append(str((c[1]+self.__decrypt_key[1])%3))
                temp_key_lst.append(str(c[1]))
            if len(c) > 2:
                temp_dec_lst.append(str((c[2]+self.__decrypt_key[2])%3))
                temp_key_lst.append(str(c[2]))
            decrypt_lst += [''.join(temp_dec_lst)+" "]
            key_lst += [''.join(temp_key_lst)+" "]
        key_lst = ''.join(key_lst)
        self.__decrypt_text = ''.join(decrypt_lst)
        print(f'The key of the decrypt text is: {key_lst}')
        print(f'The decrypt text is: {self.__decrypt_text}')
        print("=====================================")
        

    def __decrypt(self):
        A1 = [ZERO, ONE, TWO]
        A2 = A1[2:]+A1[:2]
        A3 = A2[2:]+A2[:2]

        first_leteer = [c[0] for c in self.__right_text_str if len(c)]
        second_leteer = [c[1] for c in self.__right_text_str if len(c) > 1]
        third_leteer = [c[2] for c in self.__right_text_str if len(c) > 2]

        V1 = [0, 0, 0]
        V2 = [0, 0, 0]
        V3 = [0, 0, 0]

        # build V1
        for i in range(len(first_leteer)):
            if first_leteer[i] == 0:
                V1[0] += 1
            elif first_leteer[i] == 1:
                V1[1] += 1
            elif first_leteer[i] == 2:
                V1[2] += 1
        sumv = sum(V1)
        for i in range(len(V1)):
            V1[i] /= sumv

        # build V2
        for i in range(len(second_leteer)):
            if second_leteer[i] == 0:
                V2[0] += 1
            elif second_leteer[i] == 1:
                V2[1] += 1
            elif second_leteer[i] == 2:
                V2[2] += 1
        sumv = sum(V2)
        for i in range(len(V2)):
            V2[i] /= sumv

        # build V3
        for i in range(len(third_leteer)):
            if third_leteer[i] == 0:
                V3[0] += 1
            elif third_leteer[i] == 1:
                V3[1] += 1
            elif third_leteer[i] == 2:
                V3[2] += 1
        sumv = sum(V3)
        for i in range(len(V3)):
            V3[i] /= sumv
        
        A1V1 = np.dot(A1, V1)
        A2V1 = np.dot(A2, V1)
        A3V1 = np.dot(A3, V1)
        result1 = [A1V1, A2V1, A3V1]
        print("=====================================")
        print(f"{A1 = }\n{A2 = }\n{A3 = }\n")
        print("=====================================")
        print("The key of the first letter:", end="\n\n")
        print("The first of the blocks are: ", end="")
        print(first_leteer)
        print(f"The Vector of the frequencies of the first letter is: {V1 = }")
        print("Now we will calculate the dot products of the matrix V1 with the matrix A1, A2, A3")
        print(f"{A1V1 = }\n{A2V1 = }\n{A3V1 = }")
        print(f"The maximal value is for i = {result1.index(max(result1))} and the key of the first letter is: {result1.index(max(result1))}", end="\n\n")

        A1V2 = np.dot(A1, V2)
        A2V2 = np.dot(A2, V2)
        A3V2 = np.dot(A3, V2)
        result2 = [A1V2, A2V2, A3V2]
        print("=====================================")
        print("The key of the second letter:", end="\n\n")
        print("The second of the blocks are: ", end="")
        print(second_leteer)
        print(f"The Vector of the frequencies of the second letter is: {V2 = }")
        print("Now we will calculate the dot products of the matrix V2 with the matrix A1, A2, A3")
        print(f"{A1V2 = }\n{A2V2 = }\n{A3V2 = }")
        print(f"The maximal value is for i = {result2.index(max(result2))} and the key of the second letter is: {result2.index(max(result2))}")

        A1V3 = np.dot(A1, V3)
        A2V3 = np.dot(A2, V3)
        A3V3 = np.dot(A3, V3)
        result3 = [A1V3, A2V3, A3V3]
        print("=====================================")
        print("The key of the third letter:", end="\n\n")
        print("The third of the blocks are: ", end="")
        print(third_leteer)
        print(f"The Vector of the frequencies of the third letter is: {V3 = }")
        print("Now we will calculate the dot products of the matrix V3 with the matrix A1, A2, A3")
        print(f"{A1V3 = }\n{A2V3 = }\n{A3V3 = }")
        print(f"The maximal value is for i = {result3.index(max(result3))} and the key of the third letter is: {result3.index(max(result3))}")

        self.__encrypt_key = [result1.index(max(result1)), result2.index(max(result2)), result3.index(max(result3))]
        self.__decrypt_key = [(m+m)%len(self.__encrypt_key) for m in self.__encrypt_key]

        print("=====================================")
        print(f"The encrypt key is: {self.__encrypt_key}")
        print(f"The decrypt key is: {self.__decrypt_key}")
        print("=====================================")
        

    def __check_key(self) -> int:
        sum = 0
        print(f"{self.__text_str}")
        while True:
            print(f"{' '*(self.__time*3)}{self.__text_str}")
            temp_frequencies_vector:list = self.__first_frequencies_vector[:len(self.__first_frequencies_vector)-self.__time]
            temp_sum = 0
            temp_first_frequencies_vector = self.__first_frequencies_vector[self.__time:]
            for i in range(len(temp_frequencies_vector)):
                f = temp_first_frequencies_vector[i]
                l = temp_frequencies_vector[i]
                if temp_first_frequencies_vector[i] == temp_frequencies_vector[i]:
                    temp_sum += 1
            print(f'for {self.__time} we have {temp_sum} equal elements (Adjustments)')
            if temp_sum > sum:
                sum = temp_sum
                self.__time += 1
            else:
                self.__time -= 1
                self.__right_frequencies_vector = temp_frequencies_vector[:]
            # print(f"{' '*(self.__time*self.__time+self.__time)}{self.__text_str}")
                return sum

    def __str__(self) -> str:
        return f'=========================\n{self.__text = }\n -> {self.__text_str = }\n -> {self.__first_frequencies_vector = }\n -> {self.__time = }\n -> {self.__right_frequencies_vector = }\n -> {self.__right_text_str = }\n -> {self.__encrypt_key = }\n -> {self.__decrypt_key = }\n -> {self.__decrypt_text = }\n========================='


if __name__ == '__main__':
    Encrypted_text:str = "01221 22102 21211"
    cipher = VigenereCipher(Encrypted_text, 2)
    cipher.process()
