def find_the_special_block_cipher(M1:str, M2:str, M3:str) -> str:
    M1:str = M1.replace(" ", "")
    M2:str = M2.replace(" ", "")
    M3:str = M3.replace(" ", "")

    if len(M1) != len(M2) or len(M1) != len(M3) or len(M2) != len(M3):
        print("[ERROR]: The length of the messages are not equal")
        return "[ERROR]"
    
    blocks_len:int = len(M1)
    leter_in_M1:list = {}
    leter_in_M2:list = {}
    leter_in_M3:list = {}

    for i in range(blocks_len):
        if leter_in_M1.get(M1[i]) == None:
            leter_in_M1[M1[i]] = [i]
        else:
            leter_in_M1[M1[i]].append(i)

        if leter_in_M2.get(M2[i]) == None:
            leter_in_M2[M2[i]] = [i]
        else:
            leter_in_M2[M2[i]].append(i)

        if leter_in_M3.get(M3[i]) == None:
            leter_in_M3[M3[i]] = [i]
        else:
            leter_in_M3[M3[i]].append(i)

        if len(leter_in_M1[M1[i]]) == 2:
            if len(leter_in_M2[M2[i]]) == 2:
                if (leter_in_M1[M1[i]][0] == leter_in_M2[M2[i]][0] and
                    leter_in_M1[M1[i]][1] == leter_in_M2[M2[i]][1]):
                    print(f"[INFO]: The special block cipher is M3")
                    return "M3"
            elif len(leter_in_M3[M3[i]]) == 2:
                if (leter_in_M1[M1[i]][0] == leter_in_M3[M3[i]][0] and
                    leter_in_M1[M1[i]][1] == leter_in_M3[M3[i]][1]):
                    print(f"[INFO]: The special block cipher is M2")
                    return "M2"
        elif len(leter_in_M2[M2[i]]) == 2:
            if len(leter_in_M3[M3[i]]) == 2:
                if (leter_in_M2[M2[i]][0] == leter_in_M3[M3[i]][0] and
                    leter_in_M2[M2[i]][1] == leter_in_M3[M3[i]][1]):
                    print(f"[INFO]: The special block cipher is M1")
                    return "M1"
                
    print("[ERROR]: There is no special block cipher")
    return "[ERROR]"


if __name__ == "__main__":
    M1 = "vielm bdugb oujld iglof ltbmc lbohl"
    M2 = "lzlgx ujprk uqqxt vnsne uffhj uztol"
    M3 = "sfzql oexpo bxaqe fpqbu qcolj qobkq"

    block:str = find_the_special_block_cipher(M1, M2, M3)
    # print(block)
