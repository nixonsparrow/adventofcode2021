from os import path


def txt_opener(input_file, separator=None, force_str=False):
    if not separator:
        return open(path.dirname(__file__) + input_file).read()

    try:
        if force_str:
            raise ValueError
        the_list = list(map(int, open(path.dirname(__file__) + input_file).read().split(separator)))
    except ValueError:
        the_list = list(map(str, open(path.dirname(__file__) + input_file).read().split(separator)))

    return [x for x in the_list if x != ''] if len(the_list) > 1 else the_list[0]
