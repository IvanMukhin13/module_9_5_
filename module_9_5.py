import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        for readline in f:
            all_data.append(readline)
        f.close()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = datetime.datetime.now()
    for i in filenames:
        res = read_info(i)
    finish = datetime.datetime.now()
    print(f'{finish - start} линейный')
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    finish = datetime.datetime.now()
    print(f'{finish - start} многопроцессорный')
