import sys
import random
import argparse

DEFAULT_DIV_AMOUNT = 10
DEFAULT_MUL_AMOUNT = 10

DEFAULT_FIRST_RANK = 3
DEFAULT_SECOND_RANK = 2


class Example:
    def __init__(self, first_dig_rank, sec_dig_rank, operation_char='x'):
        self.first_dig_rank = first_dig_rank
        self.sec_dig_rank = sec_dig_rank
        self.operation_char = operation_char
        self.first_num, self.second_num = self.generate_nums()

    def generate_nums(self):
        sec_num = random.randint(
            10 ** (self.sec_dig_rank-1),  # from 100
            10 ** self.sec_dig_rank - 1)  # to 999

        if self.operation_char == 'x':
            # multiplication
            first_num = random.randint(
                10 ** (self.first_dig_rank-1),  # from 100
                10 ** self.first_dig_rank - 1)  # to 999
        else:
            # division without remainder
            result = random.randint(
                10 ** (self.first_dig_rank-1),  # from 100
                10 ** self.first_dig_rank - 1)  # to 999

            first_num = result * sec_num

        return (first_num, sec_num)

    def __repr__(self):
        return f'First num: {self.first_num}, Second num: {self.second_num}'

    def form_example_string(self):
        return f'{self.first_num} {self.operation_char} {self.second_num}'

    def form_example_string_solved(self):
        if self.operation_char == 'x':
            result = self.first_num * self.second_num
        else:
            result = self.first_num / self.second_num

        return self.form_example_string() + f' = {int(result)}'


def init_args():
    parser = argparse.ArgumentParser(
        description='Програма служить на генерування прикладів із математики на множення та ділення. Вона є помічником для батьків у справі вигадування таких прикладів.')

    parser.add_argument('-a', '--amount', type=int, metavar='',
                        help='Кількість прикладів, по скільки для множення і для ділення.')
    parser.add_argument('-f', '--first', type=int, metavar='',
                        help='Розряд першого числа. Сотні за замовчуванням.')
    parser.add_argument('-s', '--second', type=int, metavar='',
                        help='Розряд другого числа. Десятки за замовчуванням.')
    args = parser.parse_args()

    return args


def main():
    divs = [Example(first_dig_rank=INPUT_FIRST_RANK or DEFAULT_FIRST_RANK,
                    sec_dig_rank=INPUT_SECOND_RANK or DEFAULT_SECOND_RANK,
                    operation_char=':')
            for i in range(INPUT_AMOUNT or DEFAULT_DIV_AMOUNT)]

    muls = [Example(first_dig_rank=INPUT_FIRST_RANK or DEFAULT_FIRST_RANK,
                    sec_dig_rank=INPUT_SECOND_RANK or DEFAULT_SECOND_RANK,
                    operation_char='x')
            for i in range(INPUT_AMOUNT or DEFAULT_DIV_AMOUNT)]

    with open('приклади.txt', 'w',  encoding='utf-8') as unsolved:
        with open('відповіді.txt', 'w', encoding='utf-8') as solved:

            unsolved.write('Приклади:\n\n')
            solved.write('Відповіді на приклади:\n\n')

            unsolved.write('\tДілення:\n')
            solved.write('\tДілення:\n')
            for index, example in enumerate(divs, start=1):
                unsolved.write(
                    f'\t\t{index}. {example.form_example_string()}\n')
                solved.write(
                    f'\t\t{index}. {example.form_example_string_solved()}\n')

            unsolved.write('\n')
            solved.write('\n')

            unsolved.write('\tМноження:\n')
            solved.write('\tМноження:\n')
            for index, example in enumerate(muls, start=1):
                unsolved.write(
                    f'\t\t{index}. {example.form_example_string()}\n')
                solved.write(
                    f'\t\t{index}. {example.form_example_string_solved()}\n')


if __name__ == "__main__":
    args = init_args()

    INPUT_AMOUNT = args.amount
    INPUT_FIRST_RANK = args.first
    INPUT_SECOND_RANK = args.second

    main()
