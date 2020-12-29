from random import randint
from random import choice
from string import digits, ascii_letters


def email():
    return ''.join([''.join(choice(ascii_letters + digits) for _ in range(randint(10, 20))), '@yandex.ru'])

