// Data file must be read as string for this solution
// Change return type as needed daily
List<String> parseContents(lines) {
  // on Windows:
  lines = lines.trim().split('\r\n\r\n'); // Split by '\n\n' on *nix systems
  return lines;
}

int part1(data) {
  int valid = 0;
  for (var line in data) {
    List<String> fields = line.split(RegExp(r'\s+'));
    List<List<String>> passportList =
        fields.map((field) => field.split(':')).toList();

    Map<String, String> passport = Map.fromIterable(passportList,
        key: (field) => field[0], value: (field) => field[1]);

    if (passport.keys.length == 8 ||
        (passport.keys.length == 7 && !passport.containsKey('cid'))) {
      valid++;
    }
  }
  return valid;
}

int part2(data) {
  int valid = 0;
  for (var line in data) {
    List<String> fields = line.split(RegExp(r'\s+'));
    List<List<String>> passportList =
        fields.map((field) => field.split(':')).toList();

    Map<String, String> passport = Map.fromIterable(passportList,
        key: (field) => field[0], value: (field) => field[1]);

    if (validate(passport)) {
      valid++;
    }
  }
  print('Output:');
  return valid;
}

bool validate(passport) {
  //
  RegExp hgt = RegExp(r'^(\d+)(cm|in)$');
  RegExp hcl = RegExp(r'^#[0-9a-f]{6}$');
  RegExp pid = RegExp(r'^\d{9}$');
  List<String> ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'];

  if (passport.keys.length == 8 ||
      (passport.keys.length == 7 && !passport.containsKey('cid'))) {
    // byr
    int byr = int.parse(passport['byr']);
    if (byr < 1920 || byr > 2002) {
      return false;
    }
    // iyr
    int iyr = int.parse(passport['iyr']);
    if (iyr < 2010 || iyr > 2020) {
      return false;
    }
    // eyr
    int eyr = int.parse(passport['eyr']);
    if (eyr < 2020 || eyr > 2030) {
      return false;
    }
    // hgt
    if (!hgt.hasMatch(passport['hgt'])) {
      return false;
    } else if (hgt.firstMatch(passport['hgt']).group(2) == 'cm' &&
        (int.parse(hgt.firstMatch(passport['hgt']).group(1)) < 150 ||
            int.parse(hgt.firstMatch(passport['hgt']).group(1)) > 193)) {
      return false;
    } else if (hgt.firstMatch(passport['hgt']).group(2) == 'in' &&
        (int.parse(hgt.firstMatch(passport['hgt']).group(1)) < 59 ||
            int.parse(hgt.firstMatch(passport['hgt']).group(1)) > 76)) {
      return false;
    } else {
      print(hgt.firstMatch(passport['hgt'])[1]);
    }
    // hcl
    if (!hcl.hasMatch(passport['hcl'])) {
      return false;
    }
    // ecl
    if (!ecl.contains(passport['ecl'])) {
      return false;
    }
    // pid
    if (!pid.hasMatch(passport['pid'])) {
      return false;
    }

    return true;
  } else {
    return false;
  }
}
