from random import randint


TERMS = "What number is missing in the progression?"


def random_progression():
    progression = []
    first_digit = randint(0, 100)  # NOSONAR
    progression_length = randint(5, 10)  # NOSONAR
    progression_step = randint(1, 10)  # NOSONAR
    counter = 0

    while counter < progression_length:
        progression.append(first_digit)
        first_digit += progression_step
        counter += 1

    return progression


def questions_and_answers():
    new_list = []
    progression = random_progression()
    random_digit = randint(0, len(progression) - 1)  # NOSONAR

    for digit in range(len(progression)):
        if digit == random_digit:
            new_list.append("..")
        else:
            new_list.append(str(progression[digit]))

    question = " ".join(new_list)
    correct_answer = str(progression[random_digit])

    return question, correct_answer
