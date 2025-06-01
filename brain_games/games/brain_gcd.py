from random import randint


TERMS = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    if a == 0 or b == 0:
        result = abs(a - b)
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    result = a
    return result


def questions_and_answers():
    random_int1 = randint(0, 20)
    random_int2 = randint(0, 20)
    question = f"{random_int1} {random_int2}"
    correct_answer = str(gcd(random_int1, random_int2))
    return question, correct_answer
