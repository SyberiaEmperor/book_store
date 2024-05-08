from pythonfuzz.main import PythonFuzz

@PythonFuzz
def BookFuzzing(buf):
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
    BookFuzzing()