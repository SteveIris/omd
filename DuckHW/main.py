def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input().lower()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print(
        'Поехать утке 🦆 на метро, или полететь?'
    )
    option = ''
    options = {'на метро': True, 'полететь': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input().lower()

    if options[option]:
        return step3_umbrella_metro()
    return step3_umbrella_fly()

def step2_no_umbrella():
    print(
        'Поехать утке 🦆 на метро, или полететь?'
    )
    option = ''
    options = {'на метро': True, 'полететь': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input().lower()

    if options[option]:
        return step3_no_umbrella_metro()
    return step3_no_umbrella_fly()

def step3_umbrella_metro():
    print(
        'Ну и зачем утке 🦆 в метро зонтик ☂? Давайте заново'
    )
    return step1()

def step3_umbrella_fly():
    print(
        'И как утка 🦆 понесёт зонтик ☂, если будет лететь? Давайте заново'
    )
    return step1()

def step3_no_umbrella_metro():
    print(
        'Утка-маляр 🦆 добралась до бара и выпустила пар 🎉'
    )

def step3_no_umbrella_fly():
    print(
        'Утка 🦆 попала под ливень и вернулась'
    )
    return step1()

if __name__ == '__main__':
    step1()