line = [1, 2, 3, 4, 5, 6]
def howmanyin(lst):
    if lst[1:]:
        print("me and the gus behind")
        return 1 + howmanyin(lst[1:])
    else:
        print("just me")
        return 1
howmanyin(line)