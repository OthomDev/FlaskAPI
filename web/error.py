def Error(data):
    if "x" not in data or "y" not in data:
        return 301
    else:
        return 200