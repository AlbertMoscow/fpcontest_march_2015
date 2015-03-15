# -*- coding: utf-8 -*-
from os import listdir

bugs_data_list = []
states_dict = {}
states_list = []
frequencies_dict = {}


def read_bugs_data():
    files = listdir('.')
    dat_files = list(filter(lambda x: x.endswith('.dat'), files))
    for file_name in dat_files:
        freq_list = []
        with open(file_name, mode='r') as f:
            lines = f.readlines()
            bug_name = lines[0].rstrip()
            for i in range(2, len(lines)):
                freq, states = lines[i].rstrip().split(': ')
                states_tuple = tuple(states.split(', '))  # превращаем список стран в кортеж
                freq_list.append((states_tuple, freq))
            bugs_data_list.append((bug_name, freq_list))
    bugs_data_list.sort()


def read_states():
    with open('States.txt', mode='r') as f:
        for line in f:
            value, key = line.split(' ')
            states_dict[key.rstrip()] = int(value)
            states_list.append(key.rstrip())
    states_list.sort()


def read_frequencies():
    with open('Frequencies.txt', mode='r') as f:
        for line in f:
            temp_list = line.rstrip().split()
            frequencies_dict[' '.join(temp_list[1::])] = int(' '.join(temp_list[:1:]))


def write_table_to_file_and_print_number_of_bugs(file_name='out1.csv'):
    print '1. Таблица в требуемом формате будет записана в файл "%s".' % file_name
    print
    print '3. Количество жуков по регионам:'
    print
    with open(file_name, mode='w') as f:
        f.write('Регион')
        for bug_name, _ in bugs_data_list:
            f.write(';%s' % bug_name)
        f.write('\n')
        for state in states_list:
            f.write(state)
            bugs_count = 0
            for _, state_freq_list in bugs_data_list:
                freq_value = '—'
                for states_tuple, freq in state_freq_list:
                    if state in states_tuple:
                        freq_value = freq
                        bugs_count += frequencies_dict[freq]
                f.write(';%s' % freq_value)
            f.write('\n')
            print state, '-', bugs_count


def print_risk_of_extinction_and_write_to_file(file_name='out2.csv'):
    print '4. Данные о совокупном риске исчезновения для каждого жука, которые будут записаны в "%s":' % file_name
    print
    with open(file_name, mode='w') as f:
        for bug_name, state_freq_list in bugs_data_list:
            risk_of_extinction = 0
            for state in states_list:
                for states_tuple, freq in state_freq_list:
                    if state in states_tuple:
                        risk_of_extinction += states_dict[state] * frequencies_dict[freq]
            print '%s - %d' % (bug_name, risk_of_extinction)
            f.write('%s;%d\n' % (bug_name, risk_of_extinction))


def main():
    """
    1. Получить на вход список файлов с ЕЯ-описанием частот и выдать на выходе CSV-файл таблицы в указанном формате.
    2. Предусмотреть возможность добавить в таблицу новый столбец для нового жука.
    3. Для каждого региона рассчитать количество жуков, которые в нём встречаются.
    4. Для каждого жука рассчитать совокупный риск исчезновения.
    """
    read_bugs_data()  # для п. 2
    read_states()  # для п. 2
    read_frequencies()  # для п. 2
    print
    write_table_to_file_and_print_number_of_bugs('result1.csv')  # для пп. 1 и 3
    print
    print_risk_of_extinction_and_write_to_file('result4.csv')  # для п. 4
    print

if __name__ == '__main__':
    main()

# вид структуры данных в переменной bugs_data_list: [(bug_name, [((state1, ..., stateN), frequency) ...]) ...]

# [
#  ('Аурата сетуньская', [(('Вевелония', 'Германия', 'Греция', 'Кения', 'Танзания'), 'В огромных количествах'), (('Камчатка', 'Россия'), 'Мало'), (('Австралия', 'Бутан', 'Непал', 'Шри-Ланка'), 'Много'), (('Индия', 'Йемен', 'Малайзия', 'Танганьика', 'Уганда', 'Эритрея', 'Эфиопия', 'Япония'), 'Сравнительно немного')]),
#  ('Гортикола филоперьевая', [(('Ливан'), 'В огромных количествах'), (('Австралия', 'Камчатка', 'Россия'), 'Единицы'), (('Греция', 'Елабуга', 'Сибирь', 'Сингапур', 'Уганда', 'Херсонес', 'Югославия'), 'Много'), (('Вайоминг', 'Кения', 'Прерия'), 'Немного'), (('Зимбабве', 'Танганьика', 'Филиппины', 'Ямайка'), 'Очень мало'), (('Эфиопия'), 'Очень много'), (('Вевелония', 'Дания', 'Индия'), 'Сравнительно немного')]),
#  ('Десятилиньята лепая', [(('Индия', 'Парагвай', 'Патагония', 'Эритрея'), 'Единицы'), (('Россия', 'Сибирь', 'Филиппины'), 'Мало'), (('Австралия', 'Вевелония', 'Пакистан', 'Прерия'), 'Немного'), (('Албания', 'Зимбабве'), 'Очень мало'), (('Уганда', 'Ямайка'), 'Сравнительно немного')]),
#  ('Мелолонтий западный', [(('Кения', 'Филиппины', 'Эфиопия'), 'Единицы'), (('Ломбардия'), 'Мало'), (('Сингапур', 'Танганьика', 'Таруса', 'Япония'), 'Много'), (('Ливан'), 'Немного'), (('Елабуга', 'Пакистан', 'Парагвай'), 'Очень мало'), (('Тотьма'), 'Очень много'), (('Австралия', 'Вевелония', 'Дания'), 'Сравнительно немного')]),
#  ('Популий грыжомельский', [(('Ливан'), 'В огромных количествах'), (('Албания', 'Зимбабве', 'Патагония', 'Россия', 'Танзания', 'Япония'), 'Единицы'), (('Непал'), 'Мало'), (('Елабуга', 'Кения', 'Курдистан', 'Херсонес', 'Эфиопия', 'Югославия'), 'Много'), (('Вайоминг', 'Греция', 'Пакистан', 'Прерия'), 'Немного'), (('Танганьика', 'Филиппины'), 'Очень много'), (('Вевелония', 'Сингапур'), 'Сравнительно немного')]),
#  ('Семипунктата Коха', [(('Дания'), 'В огромных количествах'), (('Зимбабве', 'Эфиопия'), 'Единицы'), (('Малайзия', 'Херсонес', 'Шри-Ланка'), 'Мало'), (('Вевелония', 'Елабуга'), 'Много'), (('Германия', 'Греция', 'Йемен', 'Пакистан'), 'Немного'), (('Россия'), 'Очень мало'), (('Танганьика', 'Ямайка', 'Япония'), 'Очень много'), (('Сингапур'), 'Сравнительно немного')])
# ]