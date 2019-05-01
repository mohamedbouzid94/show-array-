from contextlib import contextmanager

@contextmanager
def show_complete_array():
    oldoptions = np.get_printoptions()
    np.set_printoptions(threshold=np.inf)
    try:
        yield
    finally:
        np.set_printoptions(**oldoptions)


with show_complete_array():
    print(matrix)
