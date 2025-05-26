from brain_games.cli import welcome_user
from random import randint


def is_even(number):
    return number % 2 == 0


def main():
    user_name = welcome_user()


    print('Answer "yes" if the number is even, otherwise answer "no".')


    score = 0
    while score < 3:
        random_int = randint(0, 100)
        print('Question: ', random_int)


        user_answer = input('Your answer: ').strip().lower()
        correct_answer = 'yes' if is_even(random_int) else 'no'


        if user_answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'")
            break


    if score == 3:
        print('Congratulations, ', user_name)


if __name__ == "__main__":
    main()
