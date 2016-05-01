def get_none():
    return None


def get_string():
    return "This is a string"


def get_multi_line_string_1():
    return """This is a very long string
        with multiple lines.""".replace('\n', ' ')


def get_multi_line_string_2():
    return 'This is a very long string ' \
           'with multiple lines.'


def get_multi_line_string_3():
    return ('This is a very long string '
            'with multiple lines '
            'and parens with no commas '
            'otherwise it would be a tuple')


def get_integer_1():
    return 1


def get_integer_2():
    return 2


def get_floating_point():
    return 1.0


def get_long_floating_point_1():
    return 5.123456789


def get_long_floating_point_2():
    return 5.134567890


def get_boolean_true():
    return True


def get_boolean_false():
    return False


def get_list_1():
    return [1, 2, 3, 4, 5]


def get_list_2():
    return [2, 1, 4, 5, 3]


def get_mixed_list_1():
    return [1, 2.0, "three"]


def get_tuple_1():
    my_tuple = ('ball', 42, 'green', 55.5)
    return my_tuple


def get_empty_dict():
    my_dict = {}
    return my_dict


def get_populated_dict():
    return {'key': 'value'}


def get_exception():
    raise Exception('Whoops')


def get_custom_exception():
    raise CustomException('Custom whoops')


class SampleClass():
    def __init__(self):
        self.data = []


class SampleClass2():
    def __init__(self):
        self.data = []


class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)