from string import ascii_lowercase
from string import ascii_uppercase


def moving_shift(str, number):
    output_str = str
    for i in range(len(output_str)):
        letter = str[i]
        if ascii_lowercase.find(letter) > 0:
            index = ascii_lowercase.find(letter)
            output_str = output_str[:i] + ascii_lowercase[(index + number) % len(ascii_lowercase)] + output_str[i + 1:]
        if ascii_uppercase.find(letter) > 0:
            index = ascii_uppercase.find(letter)
            output_str = output_str[:i] + ascii_uppercase[(index + number) % len(ascii_uppercase)] + output_str[i + 1:]

        number += 1
    return output_str

def divide(str):
    length = len(str)
    print('length: ', length)
    if length % 5 == 0:
        length_part = length // 5
        arr_str = [
            str[:length_part],
            str[length_part: 2 * length_part],
            str[2 * length_part: 3 * length_part],
            str[3 * length_part: 4 * length_part],
            str[4 * length_part:]
        ]
        return arr_str

    quotient = length // 4
    four_equals = True
    while(length % 4) > quotient:
        quotient = length % quotient
        four_equals = False

    print('quotient: ', quotient)

    if four_equals:
        arr_str = [
            str[:quotient],
            str[quotient: 2 * quotient],
            str[2 * quotient: 3 * quotient],
            str[3 * quotient: 4 * quotient],
            str[4 * quotient:]
        ]
        return arr_str
    arr_str = [
        str[:quotient],
        str[quotient: 2 * quotient],
        str[2 * quotient: 3 * quotient],
        str[3 * quotient: 3 * quotient + length % quotient],
        ''
    ]
    return arr_str


moved = moving_shift('I should have known that you would have a perfect answer for me!!!', 1)
print(moved)
print(divide(moved))

