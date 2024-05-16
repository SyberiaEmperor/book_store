# pylint: skip-file

from pythonfuzz.main import PythonFuzz

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from book import *

@PythonFuzz
def book_fuzzing(buf):
    try:
        string = buf.decode("ascii")
        book = Book(string, string, int(string), int(string), string, string)
    except ValueError:
        pass
    except InvalidBookPrice:
        pass
    except InvalidBookYear:
        pass

if __name__ == '__main__':
    book_fuzzing()
