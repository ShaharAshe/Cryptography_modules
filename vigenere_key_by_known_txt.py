def calc(str_1, str_2):
    str_1 = [s for s in str_1 if s.isalpha()]
    str_2 = [s for s in str_2 if s.isalpha()]
    
    for s,t in zip(str_1, str_2):
        print(((ord(s)-ord('a'))-(ord(t)-ord('a')))%26, end=' ')


if __name__ == '__main__':
    original_txt = "b o b w a n t s t o i n t e r c e p t a l i c e s c a r d s"
    encript_txt = "ocsis ahjfg vbkqj psgfs ywtqk poipk"
    calc(encript_txt, original_txt)
