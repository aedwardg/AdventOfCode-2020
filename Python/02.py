# 655
def part1(data):
    count = 0
    lines = data.splitlines()

    for line in lines:
        nums, letter, pw = line.split(' ')
        num1, num2 = map(int, nums.split('-'))
        letter = letter[0]

        if num1 <= pw.count(letter) <= num2:
            count +=1

    return count

# 673
def part2(data):
    count = 0
    lines = data.splitlines()
    
    for line in lines:
        nums, letter, pw = line.split(' ')
        num1, num2 = map(int, nums.split('-'))
        letter = letter[0]

        positions = [pw[num1 - 1], pw[num2 - 1]]

        if positions.count(letter) == 1:
            count += 1

    return count