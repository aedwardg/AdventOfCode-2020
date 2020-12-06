import 'dart:io';
// Change these Daily:
import './05.dart';

String day = '05';

void main() async {
  // Change to readAsString when needed - Days: 4
  var contents = await File('../../inputs/$day.txt').readAsLines();
  // print(contents);
  var dataset = parseContents(contents);

  DateTime start1 = DateTime.now();
  try {
    print(part1(dataset));
    DateTime end1 = DateTime.now();
    print('Completed in ${end1.difference(start1).inMicroseconds}μs');
  } on Exception catch (e) {
    print('$e');
  }

  try {
    DateTime start2 = DateTime.now();
    print(part2(dataset));
    DateTime end2 = DateTime.now();
    print('Completed in ${end2.difference(start2).inMicroseconds}μs');
    print('Total Time: ${end2.difference(start1).inMicroseconds}μs');
  } on Exception catch (e) {
    print('$e');
  }
}
