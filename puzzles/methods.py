from os import path


def txt_opener(input_file, separator=None):
    if not separator:
        return open(path.dirname(__file__) + input_file).read()

    try:
        the_list = list(map(int, open(path.dirname(__file__) + input_file).read().split(separator)))
    except ValueError:
        the_list = list(map(str, open(path.dirname(__file__) + input_file).read().split(separator)))

    return the_list if len(the_list) > 1 else the_list[0]
