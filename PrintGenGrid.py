def print_grid(n, marks):
    print_layout(n, marks, get_line(n, marks, '+', '-'), get_line(n, marks, '|', ' '))


def print_layout(n, marks, side, middle):
    print(side)
    for i in range(n):
        for j in range(marks):
            print(middle)
        print(side)


def get_line(n, i, div, mark):
    edge = div
    marks = ''
    for j in range(i):
        marks += ' ' + mark
    segment = marks + ' ' + div
    for k in range(n):
        edge += segment
    return edge


print_grid(4, 4)

