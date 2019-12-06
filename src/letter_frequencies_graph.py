import matplotlib.pyplot as plt
# from matplotlib import pyplot
alphabet = "abcdefghijklmnopqrstuvwxyz"

code = """
yfdpcpoplhhwdpssbjnsqvtlcpzpxqugtjphvgotuvwxufgoqigxwgkskduooyeuoue
fjlnmsqpgxrmcseeliswdheywseqgcbeothskxdzekgxmmkildjnaqbukprpfaaknsu
qpdwayqaqfxsoapvsgreqydqjnkpjghvrkygtidzibhrqkmocukhcunpjcazzvomtsc
fgycwfltmiegaejwcqrgsnxxcbtcrckufwsdxdhbxgppxcuzapbdhftzmugryfseavv
bssqlxanvmfwwzityziixasivzkmvtfczqmdgkabcnjbyhaoealengfptuedlmvryeb
titbwqkekzdpmbtiphdkwwiduassvbgalxgrfhrjrjplxpujrprqzcpcdqsjorigazt
kwwlnwbjryrzhgcttroyemuwwixwufymnknirzmexyowobvardlqktzajzoijwulomg
ztefdpftjealzapcgipgaaspuzxklvd
"""

letter_counts = [code.count(l) for l in alphabet]
letter_colors = plt.cm.hsv([0.8*i/max(letter_counts) for i in letter_counts])

plt.bar(range(26), letter_counts, color=letter_colors)
plt.xticks(range(26), alphabet) # letter labels on x-axis
plt.tick_params(axis="x", bottom=False) # no ticks, only labels on x-axis
plt.title("Frequency of each letter")
plt.savefig("output.png")

if __name__ == '__main__':
    print('Printing letters frequencies graph.')