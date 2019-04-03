from contextlib import contextmanager
from os import chdir
from os.path import abspath


@contextmanager
def back_path():
    original_path = abspath('.')
    chdir('..')
    yield
    chdir(original_path)


print(abspath('.'))
with back_path():
    print(abspath('.'))

print(abspath('.'))
