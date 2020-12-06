def part1(data):
    groups = data.split('\n\n')
    # print(groups)
    total_count = 0
    for group in groups:
        group = group.replace('\n', '')
        questions = []
        for ans in group:
            if ans not in questions:
                questions.append(ans)

        total_count += len(questions)

    return total_count

def part2(data):
    groups = data.split('\n\n')
    total_count = 0
    for group in groups:
        answers = {}
        group = group.split('\n')
        for person in group:
            for ans in person:
                if ans not in answers:
                    answers[ans] = 1
                else:
                    answers[ans] += 1
        unanimous = {k: v for k, v in answers.items() if v == len(group)}

        total_count += len(unanimous)
        
    return total_count
