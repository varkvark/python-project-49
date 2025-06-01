from random import randint
from random import choice


TERMS = "What is the result of the expression?"


def questions_and_answers():
    random_int1 = randint(0, 100)
    random_int2 = randint(0, 100)
    operation = choice(["+", "-", "*"])
    question = f"{random_int1} {operation} {random_int2}"

    if operation == "+":
        correct_answer = str(random_int1 + random_int2)
    elif operation == "-":
        correct_answer = str(random_int1 - random_int2)
    elif operation == "*":
        correct_answer = str(random_int1 * random_int2)

    return question, correct_answer
