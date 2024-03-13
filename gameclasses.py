from random import randint


class Game:
    def __init__(self, no_of_questions=0):
        self._no_of_questions = no_of_questions

    @property
    def no_of_questions(self):
        return self._no_of_questions

    @no_of_questions.setter
    def no_of_questions(self, value):
        if value < 1:
            _no_of_questions = 1
            print('Minimum Number of Questions = 1')
            print('Hence, number of questions will be set to 1')
        if value > 10:
            _no_of_questions = 10
            print('Minimum Number of Questions = 10')
            print('Hence, number of questions will be set to 10')
        else:
            _no_of_questions = value


class BinaryGame(Game):
    def generate_questions(self) -> int:
        score = 0
        for i in range(self.no_of_questions):
            base10 = randint(1, 100)
            user_result = input(f'Convert {base10}, to binary: ')
            while True:
                try:
                    answer = int(user_result, base=2)
                    if answer == base10:
                        print('Right!')
                        score += 1
                        break
                    if answer != base10:
                        print('Wrong answer, the correct answer is {:b}.'.format(base10))
                        break
                except Exception as e:
                    user_result = input('Wrong answer, input correct answer on binary: ')
            return score


class MathGame(Game):
    def generate_questions(self) -> int:
        score = 0
        number_list = [0, 0, 0, 0, 0]
        symbol_list = [' ', ' ', ' ', ' ', ' ']
        operator_dict = {
            1: '+',
            2: '-',
            3: '*',
            4: '**'
        }

        for i in range(self.no_of_questions):
            for j in range(len(number_list)):
                number_list[j] = randint(1, 9)

            for k in range(len(symbol_list)):
                if k > 0 and symbol_list[k-1] == '**':
                    symbol_list[k] = operator_dict[randint(1, 3)]
                else:
                    symbol_list[k] = operator_dict[randint(1, 4)]

        question_string = str(number_list[0])
        for index in range(0, 4):
            question_string = question_string + symbol_list[index] + str(number_list[index+1])

        result = eval(question_string)

        question_string = question_string.replace('**', '^')

        user_result = input(f'Please evaluate {question_string}: ')
        while True:
            try:
                answer = int(user_result)
                if answer == result:
                    print('Right!')
                    score += 1
                    break
                if answer != result:
                    print('Wrong answer!')
                    break
            except Exception as e:
                user_result = input('Please, input correct answer: ')
        return score





