from string import ascii_lowercase
from string import ascii_uppercase

def moving_shift(str, number):
    output_str = str
    for i in range(len(output_str)):
        letter = str[i]
        if ascii_lowercase.find(letter) >= 0:
            index = ascii_lowercase.find(letter)
            output_str = output_str[:i] + ascii_lowercase[(index + number) % len(ascii_lowercase)] + output_str[i + 1:]
        if ascii_uppercase.find(letter) >= 0:
            index = ascii_uppercase.find(letter)
            output_str = output_str[:i] + ascii_uppercase[(index + number) % len(ascii_uppercase)] + output_str[i + 1:]

        number += 1
    return output_str


def divide(output_str, str):
    divided = []
    if len(str) % 5 == 0:
        length_part = len(str) / 5
    else:
        length_part = int(len(str) / 5) + 1
    for i in range(5):
        divided.append(output_str[length_part * i:length_part * (i + 1)])
    return divided


def demoving_shift(str, number):
    output_str = "".join(str)
    str = "".join(str)

    for i in range(len(output_str)):
        letter = str[i]
        if ascii_lowercase.find(letter) >= 0:
            index = ascii_lowercase.find(letter)
            output_str = output_str[:i] + ascii_lowercase[(index - number) % len(ascii_lowercase)] + output_str[i + 1:]
        if ascii_uppercase.find(letter) >= 0:
            index = ascii_uppercase.find(letter)
            output_str = output_str[:i] + ascii_uppercase[(index - number) % len(ascii_uppercase)] + output_str[i + 1:]

        number += 1
    return output_str


s = 'I should have known that you would have a perfect answer for me!!!'
moved = moving_shift('I should have known that you would have a perfect answer for me!!!', 1)
demoved = demoving_shift(['J vltasl rlhr ', 'zdfog odxr ypw', ' atasl rlhr p ', 'gwkzzyq zntyhv', ' lvz wp!!!'], 1)
print("demoved::::::::::::::::::::::::::::", demoved)
print(moved)
print(divide(moved, s))

