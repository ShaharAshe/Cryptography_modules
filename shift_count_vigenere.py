def shift_count_vigenere(text:str, loop_time) -> int:
    text_str:list = [int(c) if c.isnumeric() else c for c in text if c.isalnum()]
    first_frequencies_vector:list = text_str[:]
    
    for s in text_str:
        print(f"{s}", end=" ")
    print(" -> The original text")

    for time in range(1, loop_time+1):
        print(f"{'':{time * 2}}", end="")
        for s in text_str:
            print(f"{s}", end=" ")
        print(f" -> ", end="")

        temp_frequencies_vector:list = first_frequencies_vector[:len(first_frequencies_vector)-time]
        sum = 0
        temp_first_frequencies_vector = first_frequencies_vector[time:]
        for i in range(len(temp_frequencies_vector)):
            if temp_first_frequencies_vector[i] == temp_frequencies_vector[i]:
                sum += 1
        print(f'for {time} we have {sum} equal elements')


if __name__ == '__main__':
    text:str = "01221 text#$#$ 22102 21211"
    loop=10
    shift_count_vigenere(text, loop)
