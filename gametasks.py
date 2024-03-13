from os import remove, rename


def print_instructions(instruction):
    print(instruction)


def get_user_score(user_name: str) -> str:
    try:
        with open('user_scores.txt', 'r') as file:
            for line in file:
                content = line.split(' ')
                if user_name == content[0]:
                    return content[2]
                else:
                    return '-1'
    except IOError:
        with open('user_scores.txt', 'w'):
            return '-1'


def update_user_score(new_user: bool, user_name: str, score: int):
    if new_user:
        with open('user_scores.txt', 'a') as file:
            file.write(f'{user_name} : {score}\n')
    if user_name != True:
        with open('user_scores.tmp', 'w') as file:
            with open('user_scores.txt', 'r') as data:
                for line in data:
                    content = line.split(' ')
                    if user_name == content[0]:
                        content[2] = str(score)
                        content.append('\n')
                        file.write(' '.join(content))
                    if user_name != content[0]:
                        file.write(line)

        remove('user_scores.txt')
        rename('user_scores.tmp', 'user_scores.txt')

