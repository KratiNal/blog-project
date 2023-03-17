import time
import multiprocessing
import concurrent.futures


def lets_sleep(seconds):
    print(f"sleeping for {seconds} sec")
    time.sleep(seconds)
    print("done sleeping")


ps = []
for i in range(10):
    # lets_sleep(1)
    p = multiprocessing.Process(target=lets_sleep, args=[1])
    if __name__ == "__main__":
        p.start()
        ps.append(p)

for p in ps:
    p.join()


finish = time.perf_counter()
print("finish running at ", finish)
