from a import Ex


def func():
    print("Id inside func: %s" % id(Ex))
    raise Ex
