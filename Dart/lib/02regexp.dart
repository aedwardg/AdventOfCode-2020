import 'dart:io';

void main() async {
  var contents = await File('02.txt').readAsString();
  RegExp pattern = RegExp(r'^(\d+)-(\d+) (\w): (.+)$', multiLine: true);
  Iterable<RegExpMatch> matches = pattern.allMatches(contents);

  int count1 = 0;
  int count2 = 0;

  for (var m in matches) {
    int low = int.parse(m.group(1));
    int high = int.parse(m.group(2));
    String letter = m.group(3);
    String pw = m.group(4);

    count1 += validLetterCount(low, high, letter, pw);
    count2 += validLetterPos(low, high, letter, pw);
  }

  print('Part 1: $count1 passwords');
  print('Part 2: $count2 passwords');
}

int validLetterCount(int low, int high, String letter, String pw) {
  int charCount = letter.allMatches(pw).length;
  return low <= charCount && charCount <= high ? 1 : 0;
}

int validLetterPos(int low, int high, String letter, String pw) {
  List<String> positions = [pw[low - 1], pw[high - 1]];
  var letterAtIndex = positions.where((e) => e == letter);
  return letterAtIndex.length == 1 ? 1 : 0;
}
