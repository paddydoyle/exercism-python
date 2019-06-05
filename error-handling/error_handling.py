def handle_error_by_throwing_exception():
    error = True
    if error:
        raise Exception("Raising an Exception")


def handle_error_by_returning_none(input_data):
    # Really not sure if this what is wanted.
    if input_data == '1':
        return 1
    else:
        return None


def handle_error_by_returning_tuple(input_data):
    # Really not sure if this what is wanted.
    if input_data == '1':
        return (True, 1)
    else:
        return (False, None)


def filelike_objects_are_closed_on_exception(filelike_object):
    # Took me a very long time to figure this out from the test cases.
    with filelike_object:
        filelike_object.open()
        filelike_object.do_something()
        filelike_object.close()
