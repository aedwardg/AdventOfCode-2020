import 'dart:math';

// Change return type daily
List<String> parseContents(lines) {
  // var intData = lines.map((e) => int.parse(e));
  return lines;
}

int part1(data) {
  List<int> idList = [];

  for (String line in data) {
    int row = findRow(line);
    int col = findColumn(line);
    int seatID = findID(row, col);
    idList.add(seatID);
  }

  return idList.reduce(max);
}

int part2(data) {
  List<int> idList = [];

  for (String line in data) {
    int row = findRow(line);
    int col = findColumn(line);
    int seatID = findID(row, col);
    idList.add(seatID);
  }

  idList.sort();
  int mySeat;

  for (int i = idList[0]; i < idList[idList.length - 1]; i++) {
    if (!idList.contains(i)) {
      mySeat = i;
    }
  }

  return mySeat;
}

int findID(int row, int column) {
  int seatID = row * 8 + column;
  return seatID;
}

int findRow(String line) {
  String rowCode = line.substring(0, 7);
  List<int> rows = List.generate(128, (i) => i);

  for (int i = 0; i < rowCode.length; i++) {
    if (rowCode[i] == 'F') {
      rows = rows.sublist(0, rows.length ~/ 2);
    } else {
      rows = rows.sublist(rows.length ~/ 2);
    }
  }

  return rows[0];
}

int findColumn(String line) {
  String colCode = line.substring(line.length - 3);
  List<int> cols = List.generate(8, (i) => i);

  for (int i = 0; i < colCode.length; i++) {
    if (colCode[i] == 'L') {
      cols = cols.sublist(0, cols.length ~/ 2);
    } else {
      cols = cols.sublist(cols.length ~/ 2);
    }
  }

  return cols[0];
}
