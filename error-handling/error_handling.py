def handle_error_by_throwing_exception():
    raise Exception("Raising an Exception")


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except ValueError:
        return None


def handle_error_by_returning_tuple(input_data):
    res = handle_error_by_returning_none(input_data)

    return (res is not None, res)


def filelike_objects_are_closed_on_exception(filelike_object):
    with filelike_object:
        filelike_object.do_something()
