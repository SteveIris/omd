import csv


def menu():
    """Выводит меню выбора команды"""
    option = ''
    options = {'1': first_option, '2': second_option, '3': third_option, 'Закрыть': close, 'Котик': cat}
    while option not in options:
        print('Выберите команду: {}/{}/{}/{}'.format(*options))
        option = input()
    options[option]()


def first_option():
    """Реализует первую команду"""
    data = open_file('Corp_Summary.csv')
    departments = {}

    for line in data:
        if not departments.get(line[1]):
            departments[line[1]] = {line[2]}
        else:
            departments[line[1]].add(line[2])

    print('Департаменты:')
    for department in departments:
        print(f'{department}: ')
        print('    ' + (', '.join(list(departments[department]))))
    menu()


def second_option():
    """Реализует вторую команду"""
    data = open_file('Corp_Summary.csv')
    departments = {}

    for line in data:
        salary = int(line[5])
        if not departments.get(line[1]):
            departments[line[1]] = {'Численность': 1, 'Минимальная зп': salary, 'Максимальная зп': salary, 'Средняя зп': salary}
        else:
            departments[line[1]]['Численность'] += 1
            departments[line[1]]['Средняя зп'] += salary
            if salary < departments[line[1]]['Минимальная зп']:
                departments[line[1]]['Минимальная зп'] = salary
            if int(line[5]) > departments[line[1]]['Максимальная зп']:
                departments[line[1]]['Максимальная зп'] = salary

    print('Департаменты:')
    for department in departments:
        print(f'{department}: ')
        departments[department]['Средняя зп'] = round(departments[department]['Средняя зп']/departments[department]['Численность'], 2)
        for dep_property in departments[department]:
            print(f'    {dep_property}: {departments[department][dep_property]}')
    menu()


def third_option():
    """Будет реализовывать третью команду"""
    pass


def close():
    """Закрывает программу"""
    quit()


def open_file(file_path: str) -> list:
    """Открывает файл по данному адресу и возвращает его в виде списка"""
    with open(file_path, 'r', encoding='utf8') as f:
        reader = csv.reader(f, delimiter=";")
        data_read = [row for row in reader]
    data_read.pop(0)
    return data_read


def cat():
    print("""             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
          )     (             .              '
         =\     /=
           )===(       *
          /     \\
          |     |
         /       \\
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  jgs|  |  |  |  |  |  |  |  |  |  |  |  |  |""")
    menu()


if __name__ == '__main__':
    menu()
