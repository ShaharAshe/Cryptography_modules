def calc_char_to_num(char:str):
    num = ord(char.lower())-ord("a")
    print(f"{char} --> {num}")
    return num

def calc_num_to_char(num:int):
    char:str = chr(num+ord("a"))
    print(f"{num} --> {char}")
    return char

if __name__ == "__main__":
    char = "o"
    num = 14

    calc_char_to_num(char=char)
    calc_num_to_char(num=num)
    