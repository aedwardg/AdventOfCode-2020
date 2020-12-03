def part1(data):
  new_data = set(map(int, data.split()))
  for i in new_data:
    if 2020 - i in new_data:
      return i * (2020 - i)
  
def part2(data):
  new_data = set(map(int, data.split()))
  for i in new_data:
    for j in new_data:
      if 2020 - (i + j) in new_data:
        return i * j * (2020 - (i + j))

# Brute Force:
#
# def part1(data):
#   split_data = data.split()
#   new_data = [int(num) for num in split_data]
  
#   for i in new_data:
#     other_num = 2020 - i
#     if other_num in new_data:
#       return i * other_num

# def part2(data):
#   split_data = data.split()
#   new_data = [int(num) for num in split_data]

#   for i in new_data:
#     for j in new_data[1:]:
#       for k in new_data[2:]:
#         if i + j + k == 2020:
#           return i * j * k
