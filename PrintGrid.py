def print_grid(n):
    get_layout(n)


def get_edge(n):
    edge = '+'
    segment = ' - - - - +'
    for i in range(n):
        edge += segment
    return edge


def get_middle(n):
    edge = '|'
    segment = '         |'
    for i in range(n):
        edge += segment
    return edge


def get_layout(n):
    side = get_edge(n)
    middle = get_middle(n)
    print(side)
    for i in range(n):
        for j in range(4):
            print(middle)
        print(side)


print_grid(2)

