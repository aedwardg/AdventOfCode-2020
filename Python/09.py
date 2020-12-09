from collections import deque

def part1(data):
    lines = data.splitlines()
    preamb = deque(i for i in lines[:25])
    index = 25

    is_valid = True
    is_valid, bad_index = check_if_valid(lines, preamb, index, is_valid)
    return lines[bad_index]

def part2(data):
    pt_1_ans = 400480901 # hard-coded pt 1 ans 
    lines = data.splitlines()
    lines.remove(str(pt_1_ans))
    contig = deque(int(i) for i in lines if int(i) < pt_1_ans)
    for i in range(1, len(contig) -1):
        piece = deque()
        piece.append(contig[i])

        max_index = len(contig) - 1
        index = i
        while index - 1 < max_index - 1 and sum(piece) != pt_1_ans:
            index += 1
            piece.append(contig[index])

        if sum(piece) == pt_1_ans:
            return min(piece) + max(piece)

def check_if_valid(lines, preamble, index, is_valid):
    forward = preamble.copy()
    rev = deque(forward[i] for i in range(len(forward)-1, -1, -1))
    for num1 in forward:
        for num2 in rev:
            if int(num1) + int(num2) == int(lines[index]) and int(num1) != int(num2):
                # print('All valid!')
                preamble.popleft()
                preamble.append(lines[index])
                new_preamb = preamble.copy()
                index += 1
                # print(f'new index: {index}')
                return check_if_valid(lines, new_preamb, index, is_valid)

    is_valid = False
    bad_index = index
    return is_valid, bad_index
