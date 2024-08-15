import time
from time import sleep
from datetime import datetime
from threading import Thread


def wite_words(word_count, file_name):
    test = open(file_name, 'a')
    for i in range(word_count):
        # print(i)
        test.write(f'Какое-то слово № {str(i + 1)}' + '\n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
wite_10 = wite_words(10, 'example1.txt')
wite_30 = wite_words(30, 'example2.txt')
wite_200 = wite_words(200, 'example3.txt')
wite_100 = wite_words(100, 'example4.txt')
time_stop = datetime.now()
time_res_1 = time_stop - time_start
print(f'Последовательная запись длилась {time_res_1}')

time_start = datetime.now()

trh_10 = Thread(target=wite_words, args=(10, 'example5.txt'))
trh_30 = Thread(target=wite_words, args=(30, 'example6.txt'))
trh_200 = Thread(target=wite_words, args=(200, 'example7.txt'))
trh_100 = Thread(target=wite_words, args=(100, 'example8.txt'))

trh_10.start()
trh_30.start()
trh_200.start()
trh_100.start()

trh_10.join()
trh_30.join()
trh_200.join()
trh_100.join()

time_stop = datetime.now()
time_res_2 = time_stop - time_start
print(f'Поточная запись длилась {time_res_2}')
print(f'Разница между способами записи {time_res_1 - time_res_2}')
