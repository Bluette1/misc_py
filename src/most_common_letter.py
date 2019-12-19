alphabet = "abcdefghijklmnopqrstuvwxyz"


# convert between letters and numbers up to 26
def number_to_letter(i):
    return alphabet[i % 26]  #  %26 does the wrap-around


def letter_to_number(l):
    return alphabet.find(l)  # index in the alp


# How to encode a single character (letter or not)
def caesar_shift_single_character(l, amount):
    i = letter_to_number(l)
    if i == -1:  # character not found in alphabet
        return ""  #  remove it, it's space or punctuation
    else:
        return number_to_letter(i + amount)  # Caesar shift


# How to encode a full text
def caesar_shift(text, amount):
    shifted_text = ""
    for char in text.lower():  # also convert uppercase letters to lowercase
        shifted_text += caesar_shift_single_character(char, amount)
    return shifted_text


# Find the most commonly occurring letter in a text
def find_most_common_letter(text):
    max_count = 0  # initialise the count
    most_common_letter = ['a'] # use letter 'a' as the default
    for letter in text:
        count = text.count(letter)
        if count > max_count:
            max_count = count
            most_common_letter.pop(0)
            most_common_letter.append(letter)
        elif count == max_count: #just add this to the list
            most_common_letter.append(letter)
    print(*most_common_letter)

### MAIN PROGRAM ###

message = """
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door—
"'Tis some visitor," I muttered, "tapping at my chamber door—
Only this and nothing more."
"""

code = caesar_shift(message, 2)
print(code)
t = '''
swodkdbkfovvobpbywkxkxdsaeovkxngrycksndgyfkcdkxndbexuvoccvoqcypcdyx
ocdkxnsxdronocobdxokbdrowyxdrockxnrkvpcexukcrkddobonfsckqovsocgrycop
bygxkxngbsxuvonvszkxncxoobypmyvnmywwkxndovvdrkdsdccmevzdybgovvdrycoz
kccsyxcbokngrsmriodcebfsfocdkwzonyxdrocovspovoccdrsxqcdrorkxndrkdwym
uondrowkxndrorokbddrkdponkxnyxdrozonocdkvdrocogybnckzzokbwixkwoscyji
wkxnskcusxqypusxqcvyyuyxwigybuciowsqrdikxnnoczksbxydrsxqlocsnobowksx
cbyexndronomkiypdrkdmyvycckvgbomulyexnvocckxnlkbodrovyxokxnvofovckxn
ccdbodmrpkbkgki
'''

find_most_common_letter(code)

print("demoving::::::::::::::$$$$$$$$$$$$$$$$$$")
decode = caesar_shift(t, -10)
print("DECODED>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", decode)


