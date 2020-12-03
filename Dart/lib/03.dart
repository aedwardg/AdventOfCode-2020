// Change return type daily
List<String> parseContents(lines) {
  // var intData = lines.map((e) => int.parse(e));
  return lines;
}

int part1(data) {
  return findTrees(data, 3);
}

int part2(data) {
  int runOne = findTrees(data, 1);
  int runTwo = part1(data);
  int runThree = findTrees(data, 5);
  int runFour = findTrees(data, 7);
  int runFive = findTrees(data, 1, 2);
  return runOne * runTwo * runThree * runFour * runFive;
}

int findTrees(List<String> lines, int right, [int down = 1]) {
  int index = 0;
  int trees = 0;
  for (var i = 0; i < lines.length; i += down) {
    index = index > lines[i].length - 1 ? index % lines[i].length : index;
    if (lines[i][index] == '#') {
      trees++;
    }
    index += right;
  }
  return trees;
}
