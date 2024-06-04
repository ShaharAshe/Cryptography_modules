class LfsrCipher:
    def __init__(self, original_text: str) -> None:
        self.original_text = original_text
        self.original_text_lst = [int(c) for c in self.original_text if c.isdigit()]
        self.cicle = 0
        self.maximal_length = 2 ** len(self.original_text_lst) - 1
    
    def process(self):
        temp_text = self.original_text_lst[:]
        total_text = self.original_text_lst[:]+[" "]
        for i in range(1, self.maximal_length+1):
            temp_XOR = 0
            for j in temp_text:
                temp_XOR ^= j
            temp_text.pop(0)
            temp_text.append(temp_XOR)
            total_text.append(temp_XOR)
            if temp_text == self.original_text_lst:
                self.cicle = i
                total_text = [str(c) for c in total_text]
                print(f"The sequence is periodic with cycle length {self.cicle}")
                print(f"The sequence is {self.original_text}")
                print(f'The total sequence is {"".join(total_text)}')
                print(f'The maximal length of the sequence is {self.maximal_length}')
                if i == self.maximal_length:
                    print("The sequence is maximal length")
                else:
                    print("The sequence is not maximal length")
                break


if __name__ == "__main__":
    original_text = "100011"
    lfsr_cipher = LfsrCipher(original_text)
    lfsr_cipher.process()