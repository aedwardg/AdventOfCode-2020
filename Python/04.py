import re

def part1(data):
    lines = data.split('\n\n')
    valid = 0
    for line in lines:
        fields = line.split()
        passport = {field.split(':')[0]: field.split(':')[1] for field in fields}
        
        if len(passport.keys()) == 8 or (len(passport.keys()) == 7 and 'cid' not in passport):
            valid += 1
        
    return valid

def part2(data):
    lines = data.split('\n\n')
    valid = 0
    for line in lines:
        fields = line.split()
        passport = {field.split(':')[0]: field.split(':')[1] for field in fields}
        if validate(passport):
            valid += 1
    return valid


def validate(passport):
    hgt = re.compile(r'^(\d+)(cm|in)$')
    hcl = re.compile(r'^#[0-9a-f]{6}$')
    pid = re.compile(r'^\d{9}$')

    if len(passport.keys()) == 8 or (len(passport.keys()) == 7 and 'cid' not in passport):
        # byr
        if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            return False
        # iyr
        if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            return False
        # eyr
        if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            return False
        # hgt
        if not hgt.match(passport['hgt']):
            return False
        elif hgt.match(passport['hgt'])[2] == 'cm' and (int(hgt.match(passport['hgt'])[1]) < 150 or int(hgt.match(passport['hgt'])[1]) > 193):
            return False
        elif hgt.match(passport['hgt'])[2] == 'in' and (int(hgt.match(passport['hgt'])[1]) < 59 or int(hgt.match(passport['hgt'])[1]) > 76):
            return False
        else:
            print(hgt.match(passport['hgt'])[1])
        # hcl
        if not hcl.match(passport['hcl']):
            return False
        # ecl
        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        # pid
        if not pid.match(passport['pid']):
            return False
            
        return True
    else:
        return False
