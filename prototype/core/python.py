'''
Consonant = {"basic" : ['r', 's', 'e', 'f', 'a', 'q', 't', 'd', 'w', 'c', 'z', 'x', 'v', 'g'],
             "double" : ['R', 'E', 'Q', 'T', 'W'],
             "complex" : ['rt', 'sw', 'sg', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'qt']}
Vowel = {"basic" : ['k', 'o', 'j', 'p', 'h', 'hl', 'n', 'nl', 'm', 'l'],
         "dipthong" : ['i', 'O', 'u', 'P', 'hk', 'ho', 'y', 'nj', 'np', 'b', 'ml']}
'''

import os
import platform
# or pyautogui

class A2H():
    def __init__(self):
        self.Vowel = ['k', 'o', 'j', 'p', 'h', 'hl', 'n', 'nl', 'm', 'l' # basic
                ,'i', 'O', 'u', 'P', 'hk', 'ho', 'y', 'nj', 'np', 'b', 'ml' # dipthong
                ]

        self.L_map = {
            'r': 0,   # ㄱ
            'R': 1,   # ㄲ
            's': 2,   # ㄴ
            'e': 3,   # ㄷ
            'E': 4,   # ㄸ
            'f': 5,   # ㄹ
            'a': 6,   # ㅁ
            'q': 7,   # ㅂ
            'Q': 8,   # ㅃ
            't': 9,   # ㅅ
            'T': 10,  # ㅆ
            'd': 11,  # ㅇ
            'w': 12,  # ㅈ
            'W': 13,  # ㅉ
            'c': 14,  # ㅊ
            'z': 15,  # ㅋ
            'x': 16,  # ㅌ
            'v': 17,  # ㅍ
            'g': 18,  # ㅎ
        }

        self.V_map = {
            'k': 0,   # ㅏ
            'o': 1,   # ㅐ
            'i': 2,   # ㅑ
            'O': 3,   # ㅒ
            'j': 4,   # ㅓ
            'p': 5,   # ㅔ
            'u': 6,   # ㅕ
            'P': 7,   # ㅖ
            'h': 8,   # ㅗ
            'hk': 9,  # ㅘ
            'ho': 10, # ㅙ
            'hl': 11, # ㅚ
            'y': 12,  # ㅛ
            'n': 13,  # ㅜ
            'nj': 14, # ㅝ
            'np': 15, # ㅞ
            'nl': 16, # ㅟ
            'b': 17,  # ㅠ
            'm': 18,  # ㅡ
            'ml': 19, # ㅢ
            'l': 20,  # ㅣ
        }

        self.T_map = {
            '':  0,   # 終声なし
            'r': 1,   # ㄱ
            'R': 2,   # ㄲ
            'rt': 3,  # ㄳ
            's': 4,   # ㄴ
            'sw': 5,  # ㄵ
            'sg': 6,  # ㄶ
            'e': 7,   # ㄷ
            'f': 8,   # ㄹ
            'fr': 9,  # ㄺ
            'fa': 10, # ㄻ
            'fq': 11, # ㄼ
            'ft': 12, # ㄽ
            'fx': 13, # ㄾ
            'fv': 14, # ㄿ
            'fg': 15, # ㅀ
            'a': 16,  # ㅁ
            'q': 17,  # ㅂ
            'qt': 18, # ㅄ
            't': 19,  # ㅅ
            'T': 20,  # ㅆ
            'd': 21,  # ㅇ
            'w': 22,  # ㅈ
            'c': 23,  # ㅊ
            'z': 24,  # ㅋ
            'x': 25,  # ㅌ
            'v': 26,  # ㅍ
            'g': 27,  # ㅎ
        }

        self.L, self.V, self.T = "", "", ""

    def run(self):
        input_string = input()
        len_input = len(input_string)
        output = []

        for i in range(len_input-1, -1, -1):
            element = input_string[i]
            if ord("a") <= ord(element) <= ord("z") or ord("A") <= ord(element) <= ord("Z"):
                pass
            else:
                output.insert(0, element)
                continue


            if element in self.Vowel:
                self.V = element + self.V
            else:
                if self.V:
                    self.L, self.V, self.T = self.L_map[element], self.V_map[self.V], self.T_map[self.T]
                    Syllables_Code = (self.L * 21 + self.V) * 28 + self.T
                    converted = chr(0xAC00 + Syllables_Code)
                    output.insert(0, converted)
                    # initializing
                    self.L, self.V, self.T = "", "", ""
                else:
                    self.T = element + self.T

        result = ("".join(output))

        if platform.system() == "Darwin":
            with os.popen("pbcopy", "w") as pipe:
                pipe.write(result)

        elif platform.system() == "Windows":
            with os.popen("clip", "w") as pipe:
                pipe.write(result)

if __name__ == "__main__":
    a2h = A2H()
    while 1: a2h.run()


'''
音節番号 =
    (初声番号 x 21 + 中声番号) x 28 + 終声番号

コードポイント =
    U+AC00 + 音節番号

    
L = 18  # ㅎ Leading
V = 0   # ㅏ Vowel
T = 4   # ㄴ Trailing

S = (L * 21 + V) * 28 + T

print(S)
print(hex(0xAC00 + S))
print(chr(0xAC00 + S))

'''


'''
番号 L	Jamo	日本語的な呼び方
0	ㄱ	k/g
1	ㄲ	kk
2	ㄴ	n
3	ㄷ	t/d
4	ㄸ	tt
5	ㄹ	r/l
6	ㅁ	m
7	ㅂ	p/b
8	ㅃ	pp
9	ㅅ	s
10	ㅆ	ss
11	ㅇ	無音/ng
12	ㅈ	j
13	ㅉ	jj
14	ㅊ	ch
15	ㅋ	k
16	ㅌ	t
17	ㅍ	p
18	ㅎ	h

番号 V	Jamo	
0	ㅏ	a
1	ㅐ	ae
2	ㅑ	ya
3	ㅒ	yae
4	ㅓ	eo
5	ㅔ	e
6	ㅕ	yeo
7	ㅖ	ye
8	ㅗ	o
9	ㅘ	wa
10	ㅙ	wae
11	ㅚ	oe
12	ㅛ	yo
13	ㅜ	u
14	ㅝ	wo
15	ㅞ	we
16	ㅟ	wi
17	ㅠ	yu
18	ㅡ	eu
19	ㅢ	ui
20	ㅣ	i

番号 T	終声	Jamo
0	なし	—
1	ㄱ	ㄱ
2	ㄲ	ㄲ
3	ㄳ	ㄳ
4	ㄴ	ㄴ
5	ㄵ	ㄵ
6	ㄶ	ㄶ
7	ㄷ	ㄷ
8	ㄹ	ㄹ
9	ㄺ	ㄺ
10	ㄻ	ㄻ
11	ㄼ	ㄼ
12	ㄽ	ㄽ
13	ㄾ	ㄾ
14	ㄿ	ㄿ
15	ㅀ	ㅀ
16	ㅁ	ㅁ
17	ㅂ	ㅂ
18	ㅄ	ㅄ
19	ㅅ	ㅅ
20	ㅆ	ㅆ
21	ㅇ	ㅇ
22	ㅈ	ㅈ
23	ㅊ	ㅊ
24	ㅋ	ㅋ
25	ㅌ	ㅌ
26	ㅍ	ㅍ
27	ㅎ	ㅎ
'''