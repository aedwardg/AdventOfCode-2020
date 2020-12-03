// Change return type daily
List<String> parseContents(lines) {
  // var intData = lines.map((e) => int.parse(e));
  return lines;
}

int part1(data) {
  int count = 0;
  for (String line in data) {
    String nums = line.split(' ')[0];

    String letter = line.split(' ')[1];
    letter = letter[0];

    String pw = line.split(' ')[2];

    int num1 = int.parse(nums.split('-')[0]);
    int num2 = int.parse(nums.split('-')[1]);

    int charCount = letter.allMatches(pw).length;

    if (num1 <= charCount && charCount <= num2) {
      count++;
    }
  }

  return count;
}

int part2(data) {
  int count = 0;
  for (String line in data) {
    String nums = line.split(' ')[0];

    String letter = line.split(' ')[1];
    letter = letter[0];

    String pw = line.split(' ')[2];

    int num1 = int.parse(nums.split('-')[0]);
    int num2 = int.parse(nums.split('-')[1]);

    List<String> positions = [pw[num1 - 1], pw[num2 - 1]];

    var letterAtIndex = positions.where((e) => e == letter);

    if (letterAtIndex.length == 1) {
      count++;
    }
  }

  return count;
}
