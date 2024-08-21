from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    f = open(name, 'r')
    while True:
        line = f.readline()
        all_data.append(line)
        if not line:
            break


filenames = [f'./homework 10.5/file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = datetime.now()
    for file in filenames:
        read_info(file)
    stop = datetime.now()
    interval_1 = stop - start
    print(f'Время работы линейного алгоритма {interval_1}')

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)
        stop = datetime.now()
        interval_2 = stop - start
    print(f'Время работы многопроцессного алгоритма {interval_2}')

    print(f'Скорость вычисления с помощью многопроцессного в {round(interval_1 / interval_2,2)} раз выше,' + '\n'
          'чем у линейного алгоритма')
