def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(callback):
    def run_callback(a, b):
        return a

    return callback(run_callback)


def cdr(callback):
    def run_callback(a, b):
        return b

    return callback(run_callback)


if __name__ == "__main__":
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))
