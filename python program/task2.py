#try it with own after revision
import random
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_choosen):
    if level_choosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def check_answer(guessed_number,original_number,attempts):
    if guessed_number<original_number:
        print('your guessed number is too low')
        return attempts-1
    elif guessed_number>original_number:
        print('your guessed number is too high')
        return attempts-1
    else:
        print(f'your guessed number is right... The answer was {original_number}')

def game():
    print('let me think of a number between 1 to 50')
    original_number=random.randint(1,50)
    print(original_number)
    level=input("choose level of difficulty....type'easy' or 'hard'")
    attempts=set_difficulty(level)
    guessed_number=0
    while guessed_number!=original_number:
        print(f"you have {attempts} remaining to guess the number")
        guessed_number=int(input('guess a number'))
        attempts=check_answer(guessed_number,original_number,attempts)
        if attempts==0:
            print('you are lose')
            return
        elif guessed_number!=original_number:
            print('try again')
game()