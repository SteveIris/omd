def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    if choice('да', 'нет'):
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    """Просит выбрать как добираться до бара с зонтиком"""
    print(
        'Поехать утке 🦆 на метро, или полететь?'
    )
    if choice('на метро', 'полететь'):
        return step3_umbrella_metro()
    return step3_umbrella_fly()


def step2_no_umbrella():
    """Просит выбрать как добираться до бара без зонтика"""
    print(
        'Поехать утке 🦆 на метро, или полететь?'
    )
    if choice('на метро', 'полететь'):
        return step3_no_umbrella_metro()
    return step3_no_umbrella_fly()


def step3_umbrella_metro():
    """Выводит сообщение о проигрыше и возвращает в начало игры"""
    print(
        'Ну и зачем утке 🦆 в метро зонтик ☂? Давайте заново'
    )
    return step1()


def step3_umbrella_fly():
    """Выводит сообщение о проигрыше и возвращает в начало игры"""
    print(
        'И как утка 🦆 понесёт зонтик ☂, если будет лететь? Давайте заново'
    )
    return step1()


def step3_no_umbrella_metro():
    """Выводит сообщение о победе"""
    print(
        'Утка-маляр 🦆 добралась до бара и выпустила пар 🎉'
    )


def step3_no_umbrella_fly():
    """Выводит сообщение о проигрыше и возвращает в начало игры"""
    print(
        'Утка 🦆 попала под ливень и вернулась'
    )
    return step1()


def choice(first_option, second_option):
    """Функция выбора одной из двух опций"""
    option = ''
    options = {first_option: True, second_option: False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input().lower()
    return options[option]


if __name__ == '__main__':
    step1()
