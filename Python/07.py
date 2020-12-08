test_rules1 = {
    'light red': [{'bright white': '1'}, {'muted yellow': '2'}],
    'dark orange': [{'bright white': '3'}, {'muted yellow': '4'}],
    'bright white': [{'shiny gold': '1'}],
    'muted yellow': [{'shiny gold': '2'}, {'faded blue': '9'}],
    'shiny gold': [{'dark olive': '1'}, {'vibrant plum': '2'}],
    'dark olive': [{'faded blue': '3'}, {'dotted black': '4'}],
    'vibrant plum': [{'faded blue': '5'}, {'dotted black': '6'}],
    'faded blue': [{'other bags': 'no'}],
    'dotted black': [{'other bags': 'no'}]
}

test_rules2 = {
    'shiny gold': [{'dark red': '2'}],
    'dark red': [{'dark orange': '2'}],
    'dark orange': [{'dark yellow': '2'}],
    'dark yellow': [{'dark green': '2'}],
    'dark green': [{'dark blue': '2'}],
    'dark blue': [{'dark violet': '2'}],
    'dark violet': [{'other bags.': 'no'}]
}

def part1(data):
    bag_set = {'shiny gold'}
    lines = data.splitlines()
    rules = get_rules(lines)
    final_bag_count = find_bags(bag_set, rules)
    return final_bag_count

def part2(data):
    lines = data.splitlines()
    rules = get_rules_with_count(lines)
    count = find_count(rules)
    test = find_count(test_rules1)
    test2 = find_count(test_rules2)
    return count, test, test2

def find_count(rules_dict):
    total_count = 0
    bag_list = rules_dict['shiny gold']
    counted_list = []

    while len(bag_list) > 0:

        current = bag_list[0]
        path = []
        inner_bags = []
        for k, v in current.items():

            total_count += traverse_rules(rules_dict, k, v)
            
        bag_list.pop(0)
    
    return total_count
    
def traverse_rules(rules_dict, k, v):
    total = 0
    if v.isdigit():
        total += int(v)
        rule = rules_dict[k]

        for r in rule:
            for inner_k, inner_v in r.items():
                if inner_v.isdigit():
                    
                    total += int(v) * traverse_rules(rules_dict, inner_k, inner_v)
    return total
            
def get_rules(lines):
    rules = []
    for line in lines:
        split_line = line.split(' bags contain ')
        rule = {split_line[0]: [' '.join(bag.split(' ')[1:3]) for bag in split_line[1].split(', ')]}
        rules.append(rule)
    return rules

def get_rules_with_count(lines):
    rules = []
    rules_dict = {}

    for line in lines:
        split_line = line.split(' bags contain ')
        rule = {split_line[0]: [{' '.join(bag.split(' ')[1:3]): bag.split(' ')[0]} for bag in split_line[1].split(', ')]}
        rules.append(rule)

    for rule in rules:
        for k, v in rule.items():
            rules_dict[k] = v
    return rules_dict

def find_bags(bag_set, rules):
    bags = bag_set
    rules = rules
    starting = len(bags)

    for id, bag in enumerate(bags.copy()):
        for rule in rules:
            for k, v in rule.items():
                for s in v:
                    if bag == s:
                        bags.add(k)
    ending = len(bags)
    
    if ending > starting:
        find_bags(bags, rules)
    else:
        print(ending - 1) # DON'T COUNT SHINY GOLD
        return ending - 1
