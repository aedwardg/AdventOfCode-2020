def part1(data):
    lines = data.splitlines()
    return find_trees(lines, 3)

def part2(data):
    lines = data.splitlines()

    trees1 = find_trees(lines, 1)
    trees2 = find_trees(lines, 3) # same as part 1
    trees3 = find_trees(lines, 5)
    trees4 = find_trees(lines, 7)
    trees5 = find_trees(lines, 1, 2)

    return trees1 * trees2 * trees3 * trees4 * trees5

def find_trees(lines, right, down=1):
    index = 0
    trees = 0
    for line in lines[::down]:
        if index > len(line) - 1:
            index = index % len(line)
        if line[index] == '#':
            trees += 1
        index += right
    return trees

# first try:
# def part1(data):
#     lines = data.splitlines()
#     index = 0
#     trees = 0

#     for line in lines:
#         if index > len(line) - 1:
#             index = index % len(line)
#         if line[index] == '#':
#             trees += 1
#         index +=3
#     return trees

# def part2(data):
#     lines = data.splitlines()
#     index = 0
#     trees1 = 0
#     trees2 = 200 # part 1
#     trees3 = 0
#     trees4 = 0
#     trees5 = 0

#     # right 1, down 1
#     for line in lines:
#         if index > len(line) - 1:
#             index = index % len(line)
#         if line[index] == '#':
#             trees1 += 1
#         index += 1
#     print(trees1)
    
#     # right 5 down 1
#     index = 0
#     for line in lines:
#         if index > len(line) - 1:
#             index = index % len(line)
#         if line[index] == '#':
#             trees3 += 1
#         index += 5
#     print(trees3)
    
#     # right 7 down 1
#     index = 0
#     for line in lines:
#         if index > len(line) - 1:
#             index = index % len(line)
#         if line[index] == '#':
#             trees4 += 1
#         index += 7
#     print(trees4)

#     # right 1 down 2
#     index = 0
#     for i in range(0, len(lines), 2):
#         if index > len(lines[i]) - 1:
#             index = index % len(lines[i])
#         if lines[i][index] == '#':
#             trees5 += 1
#         index += 1
#     print(trees5)

#     return trees1 * trees2 * trees3 * trees4 * trees5