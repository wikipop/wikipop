import string
import re

# replace_dict = {
#     "Q": "N",
#     "P": "I",
#     "F": "E",
#     "U": "N",
#     "N": "A",
#     "G": "T",
#     "A": "M",
# }

# JFRENUPAN -> JEREAUIKA
# XNGF -> XATE
# JFRENUPAN ABNUSWBN -> JEREAUIKA KBAUS0BA
# _E_EA_I_A __A____A

with open("dane/slowa.txt") as ff:
    # regex match kazde slowo pattern: _E_EA_I_A
    # gdzie _ to dowolny znak

    slowa = []

    for line in ff:
        line = line.strip()
        if re.match(r".e.ea.i.a", line):
            slowa.append(line)


replace_dict = {
    "N": "A",
    "P": "I",
    "F": "E",
    "W": "0",
    "G": "T",
    "Q": "N",
    "A": "K",
}

with open("dane/kod.txt") as ff:
    # analiza częstości występowania znaków

    count_dict = {}
    for line in ff:
        for char in line:
            if char.lower() in string.ascii_lowercase:
                if char in count_dict:
                    count_dict[char] += 1
                else:
                    count_dict[char] = 1

    # print count_dict sorted by value
    sorted_count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_count_dict)

with open("dane/kod.txt") as ff:
    text = ff.read()

    new_text = ""
    for char in text:
        if char in replace_dict:
            new_text += replace_dict[char]
        else:
            new_text += char

    print(new_text)
