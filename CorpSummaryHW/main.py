import csv


def menu():
    option = ''
    options = {'1': first_option, '2': second_option, '3': third_option}
    while option not in options:
        print('Выберите команду: {}/{}/{}'.format(*options))
        option = input()
    options[option]()


def first_option():
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
    pass


def third_option():
    pass


def open_file(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf8') as f:
        reader = csv.reader(f, delimiter=";")
        data_read = [row for row in reader]
    data_read.pop(0)
    print(data_read)
    return data_read


if __name__ == '__main__':
    menu()
