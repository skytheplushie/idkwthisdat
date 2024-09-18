from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Some word №{i}\n')
            sleep(0.1)
    print(f'writing in the {file_name} has been done!')


start = datetime.now()


write_words(10, 'file river.txt')
write_words(30, 'file river1.txt')
write_words(200, 'file river2.txt')
write_words(100, 'file river3.txt')


end = datetime.now()

print(f'the work was done in {end - start}')


start2 = datetime.now()


th1 = Thread(target=write_words, args=(10, 'file river4.txt'))
th2 = Thread(target=write_words, args=(30, 'file river5.txt'))
th3 = Thread(target=write_words, args=(200, 'file river6.txt'))
th4 = Thread(target=write_words, args=(100, 'file river7.txt'))


th1.start()
th2.start()
th3.start()
th4.start()


th1.join()
th2.join()
th3.join()
th4.join()


end2 = datetime.now()


print(f'the work was done in {end2 - start2}')