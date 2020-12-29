from advent import Advent

advent = Advent(6)

# Part 1
sum_questions = 0
for group in advent.paragraphs:
    questions = set([c for answer_person in group for c in answer_person])
    sum_questions += len(questions)

print(sum_questions)


# Part 2
sum_questions = 0
for group in advent.paragraphs:
    questions = set()
    
    for idx, answer_person in enumerate(group):
        person_answers = set()
        for c in answer_person:
            if idx == 0:
                questions.add(c)
            else:
                person_answers.add(c)
        if len(person_answers) > 0:
            questions = questions.intersection(person_answers)
    sum_questions += len(questions)

print(sum_questions)
