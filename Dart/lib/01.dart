Set<int> parseContents(lines) {
  var intData = lines.map((e) => int.parse(e));
  return {...intData};
}

int part1(data) {
  for (var i in data) {
    if (data.contains(2020 - i)) {
      return i * (2020 - i);
    }
  }
  return 0;
}

int part2(data) {
  for (var i in data) {
    for (var j in data) {
      if (data.contains(2020 - (i + j))) {
        return i * j * (2020 - (i + j));
      }
    }
  }
  return 0;
}
