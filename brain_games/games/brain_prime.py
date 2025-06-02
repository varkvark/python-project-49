from random import randint


TERMS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    prime_list = []
    for index in range(1, number + 1):
        if number % index == 0:
            prime_list.append(index)
    return prime_list


def questions_and_answers():
    question = randint(0, 100)  # NOSONAR
    correct_answer = "yes" if len(is_prime(question)) == 2 else "no"

    return question, correct_answer
