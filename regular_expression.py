import subprocess

def get_expression():
    expression = input('Write an expression: ')
    return expression

def get_word():
    word = input('Write the word: ')
    return word

def format_terminal(exp, word):
    command = f'echo "{word}" | grep -Ex \"{exp}\"'
    return command

def write_terminal(command):
    result = subprocess.run(command, shell = subprocess.DEVNULL)
    return result

def validation(exp, word, result):
    if result.returncode == 0:
        print(f'Yes!!!! The word {word} is on the expression: {exp} \n')
    else:
        print(f'Nooo :( The word {word} is not on the expression: {exp} \n')

def main():
    expression = get_expression()
    while True:
        word = get_word()
        command = format_terminal(expression, word)
        validation(expression, word, write_terminal(command))

if __name__ == '__main__':
    main()