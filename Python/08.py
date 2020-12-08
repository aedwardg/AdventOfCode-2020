import re

def part1(data, alt=None):
    if alt:
        instructions = alt
    else:    
        instructions = parse_instructions(data)
    accum = 0
    indexes = []
    i = 0
    while i not in indexes:
        indexes.append(i)
        if i == 635:
            return accum, max(indexes)
        command = instructions[i]
        if command[0] == 'acc':
            if command[1] == '+':
                accum += int(command[2])
            else:
                accum -= int(command[2])
    
            i += 1

        elif command[0] == 'jmp':
            if command[1] == '+':
                i += int(command[2])
            else:
                i -= int(command[2])
        else:
            i += 1

    return accum, max(indexes)

def part2(data):
    instructions = parse_instructions(data)
    instructions2 = instructions
    accum = 0
    indexes = []
    i = 0

    for i in range(len(instructions)):
        if instructions[i][0] == 'nop':
            try:
                instructions[i] = ('jmp', instructions[i][1], instructions[i][2])
                accum, max_index = part1(data, instructions)
                if max_index >= 632:
                    print('returning accumulator and max index')
                    return accum, max_index
            except IndexError:
                print('returning accumulator')
                return accum

            instructions[i] = ('nop', instructions[i][1], instructions[i][2])

        elif instructions[i][0] == 'jmp':
            try:
                instructions[i] = ('nop', instructions[i][1], instructions[i][2])
                accum, max_index = part1(data, instructions)
                if max_index >= 632:
                    print('returning accumulator and max index')
                    return accum, max_index
            except IndexError:
                print('returning accumulator')
                print(instructions)
                return accum

            instructions[i] = ('jmp', instructions[i][1], instructions[i][2])

    return 0

def parse_instructions(data):
    pattern = re.compile(r'^([a-z]{3}) ([-+])(\d+)$', re.MULTILINE)
    instructions = pattern.findall(data)
    return instructions