import itertools
from time import time as t

ch_list = [
    *range(48, 58),      # 0-9
    *range(97, 123),     # a-z
    *range(65, 91),      # A-Z
    *range(33, 48),      # !"#$%&'()*+,-./
    *range(58, 65),      # :;<=>?@
    *range(91, 97),      # [\]^_`
    *range(123, 127)     # {|}~]
]

chars = []
for c in ch_list:
    chars.append(chr(c))


def find_matching_combination(target_string, character_list):
    for length in range(1, 11):  # Try combinations of length 1 to 10
        for combination in itertools.product(character_list, repeat=length):
            current_string = ''.join(combination)
            if current_string == target_string:
                print(f'Matched: {current_string}')
                return


password = input('Enter password to try: ')

s = t()
find_matching_combination(password, chars)
print(f'Elapsed time: {t()-s:.7f}s')
