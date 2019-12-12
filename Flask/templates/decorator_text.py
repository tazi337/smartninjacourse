import time
import random

def timeit(func): #time_waster ist die Funktion die hier gerufen wird über @timeit decorator. JEdes mal wenn time_waster gerufen wird
    # wird auch timeit gerufen und fügt so start und print ein.
    def wrapper(*args, **kwargs): #args und kwargs sind nur Platzhalter, die die Argumente auflösen, die mitgegeben werden
        start = time.time()
        result = func(*args, **kwargs)
        print("'{}' was running for: {} seconds".format(func.__name__, time.time() - start))
        return result
    return wrapper

@timeit #decorater wird über methode time_waster gesetzt.
def time_waster(wait_seconds):
    time.sleep(wait_seconds)
    return "Done"

@timeit
def other_time_waster():
    return

def new_time_waster():
    time.sleep(2)

def measured_time_waster():
    print("Start")
    start = time.time()
    new_time_waster()
    elapsed = time.time()-start
    print("End", round(elapsed, 2)) #round rundet auf 2 Stellen

def random_time_waster():
    time.sleep(random.random()*3)

if __name__ == '__main__':
    #time_waster(1)
    measured_time_waster()

    random_time_waster()
    # viele viele Zeilen Code folgen hier

    measured_time_waster()
