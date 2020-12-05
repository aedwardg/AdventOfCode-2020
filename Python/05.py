def part1(data):
    lines = data.splitlines()
    id_list = []
    for line in lines:
        row = find_row(line)
        col = find_column(line)
        seat_id = find_id(row, col)
        id_list.append(seat_id)
    
    return max(id_list)

def part2(data):
    lines = data.splitlines()
    id_list = []
    for line in lines:
        row = find_row(line)
        col = find_column(line)
        seat_id = find_id(row, col)
        id_list.append(seat_id)
    
    id_list.sort()
    for i in range(id_list[0], id_list[-1] + 1):
        if i not in id_list:
            my_seat = i
    return my_seat

def find_id(row, column):
    seat_id = row * 8 + column
    return seat_id

def find_row(line):
    row_code = line[:7]
    rows = list(range(128))

    for char in row_code:
        if char == 'F':
            rows = rows[:int(len(rows) / 2)]
        else:
            rows = rows[int(len(rows) / 2):]

    return rows[0]

def find_column(line):
    col_code = line[-3:]
    cols = list(range(8))

    for char in col_code:
        if char == 'L':
            cols = cols[:int(len(cols) / 2)]
        else:
            cols = cols[int(len(cols) / 2):]

    return cols[0]