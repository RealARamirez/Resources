def logical_type(arg):
    if (float(arg)-int(arg)) == 0:
        return int(arg)
    else:
        return float(arg)