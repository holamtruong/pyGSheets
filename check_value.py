def checkNull(value):
    if value is None:
        return 'null'
    elif value == '-':
        return 'null'
    else:
        value = value.replace(",", ".")
        value = float(value)
        return value
