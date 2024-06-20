# Review 1 - Correct

import threading


def add_to_list(value, my_list=[]):

    my_list.append(value)

    return my_list


# Review 2 - Incorrect - need to use 'f' to format output

def format_greeting(name, age):

    # return "Hello, my name is {name} and I am {age} years old."
    return f"Hello, my name is {name} and I am {age} years old."


# Review 3 - Incorrect, this counter cannot increase, need a "add" function

class Counter:

    count = 0

    def __init__(self):

        self.count += 1

    def add_count(self):

        self.count += 1

    def get_count(self):

        return self.count


# Review 4 - Correct


class SafeCounter:

    def __init__(self):

        self.count = 0

    def increment(self):

        self.count += 1


def worker(counter):

    for _ in range(1000):

        counter.increment()


counter = SafeCounter()

threads = []

for _ in range(10):

    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)


for t in threads:

    t.join()


# Review 5 - Incorrect, add operator should be "+=" instead of "=+"

def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            # counts[item] = + 1
            counts[item] += 1

        else:

            counts[item] = 1

    return counts
