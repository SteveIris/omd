import csv


def menu() -> None:
    """Выводит меню выбора команды"""
    option = ''
    options = {'1': show_teams_hierarchy, '2': show_summary, '3': save_summary, 'Закрыть': close, 'Котик': cat}
    while option not in options:
        print('Выберите команду: {}/{}/{}/{}'.format(*options))
        option = input()
    options[option]()


def show_teams_hierarchy() -> None:
    """Выводит иерархию команд"""
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


def show_summary() -> None:
    """Выводит сводный отчёт по департаментам"""
    departments = create_summary()

    print('Департаменты:')
    for department in departments:
        print(f'{department}: ')
        for dep_property in departments[department]:
            print(f'    {dep_property}: {departments[department][dep_property]}')

    print('Сохранить отчёт в файл?')
    option = ''
    options = {'Да': True, 'Нет': False}
    while option not in options:
        print('Выберите команду: {}/{}'.format(*options))
        option = input()
    if options[option]:
        save_as_csv(departments)
    menu()


def save_summary() -> None:
    """Сохраняет сводный отчёт по департаментам"""
    save_as_csv(create_summary())
    menu()


def save_as_csv(departments: dict) -> None:
    """Сохраняет в csv-файл сводный отчёт"""
    with open('Departments_summary.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Название', 'Численность', 'Минимальная зп', 'Максимальная зп', 'Средняя зп'])
        for department in departments:
            writer.writerow([department] + list(departments[department].values()))
    print('Отчёт записан в файл Departments_summary.csv')
    return


def create_summary() -> dict:
    """Создаёт сводный отчёт по департаментам для команд 2 и 3 и возвращает его"""
    data = open_file('Corp_Summary.csv')
    departments = {}

    for line in data:
        salary = int(line[5])
        if not departments.get(line[1]):
            departments[line[1]] = {'Численность': 1, 'Минимальная зп': salary, 'Максимальная зп': salary,
                                    'Средняя зп': salary}
        else:
            departments[line[1]]['Численность'] += 1
            departments[line[1]]['Средняя зп'] += salary
            if salary < departments[line[1]]['Минимальная зп']:
                departments[line[1]]['Минимальная зп'] = salary
            if int(line[5]) > departments[line[1]]['Максимальная зп']:
                departments[line[1]]['Максимальная зп'] = salary
    for department in departments:
        departments[department]['Средняя зп'] = round(
            departments[department]['Средняя зп']/departments[department]['Численность'],
            1,
        )
    return departments


def close() -> None:
    """Закрывает программу"""
    quit()


def open_file(file_path: str) -> list:
    """Открывает файл по данному адресу и возвращает его в виде списка"""
    with open(file_path, 'r', encoding='utf8') as f:
        reader = csv.reader(f, delimiter=";")
        data_read = [row for row in reader]
    data_read.pop(0)
    return data_read


def cat() -> None:
    """Выводит котика"""
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
