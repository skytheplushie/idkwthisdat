from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Some word №{i}\n')
            sleep(0.1)
    print(f'writing in the {file_name} has been done!')


write_words(10, 'file river.txt')
write_words(30, 'file river1.txt')
write_words(200, 'file river2.txt')
write_words(100, 'file river3.txt')