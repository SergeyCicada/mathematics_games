from gametasks import print_instructions, update_user_score, get_user_score
from gameclasses import BinaryGame, MathGame

math_instructions = '''
В этой игре вам предлагается решить простую арифметичкую задачу. 
За каждый правильный ответ вам начисляется одно очко.
За ошибочные ответы очки не вычитаются.
'''

binary_instructions = '''
В этой игры вы получаете десятичное число.
Ваша задача = преобразовать его в двоичную систему счисления. 
За каждый правильный ответ вам начисляется одно очко.
За ошибочные ответы очки не вычитаются.
 '''

bg = BinaryGame
bg_instance = bg()
mg = MathGame
mg_instance = mg()

user_name = input('Hello! Enter your name: ')
score = int(get_user_score(user_name))
if score == -1:
    new_user = True
    score = 0
else:
    new_user = False

print(f'Hello, welcome to the game {user_name}')
print(f'Your current score is {score}')

user_choice = 0

while user_choice != '-1':
    game = input('MathGame(1) or BinaryGame(2) ?:  ')
    while game != '1' and game != '2':
        game = input('Enter correct number game: ')

    num_promt = input('How many questions (1 to 10) ?: ')
    while True:
        try:
            num = int(num_promt)
            break
        except:
            num_promt = input('Enter correct number : ')

    if game == '1':
        mg.no_of_questions = num
        print_instructions(math_instructions)
        score = int(score) + mg_instance.generate_questions()
    if game == '2':
        bg.no_of_questions = num
        print_instructions(binary_instructions)
        score += bg_instance.generate_questions()
    print(f'Your current score is {score}!')
    user_choice = input(f'Press enter to continue or -1 to end: ')

