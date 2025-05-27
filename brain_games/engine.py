import prompt
from brain_games.cli import welcome_user


ROUND_COUNT = 3


def launch(game):
    name = welcome_user()
    print(game.TERMS)

    score = 0
    while score < ROUND_COUNT:
        question, correct_answer = game.questions_and_answers()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').strip().lower()

        if user_answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'"
            )
            print(f"Let's try again, {name}!")
            break

    if score == 3:
        print(f'Congratulations, {name}!')
