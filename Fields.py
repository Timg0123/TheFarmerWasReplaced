from __builtins__ import *


def field_dict(size, args: dict) -> list[list[dict]]:
    grid = []
    for i in range(size):
        grid.append([])
        for j in range(i, i + size):
            tile = {}
            for key in args:
                tile[key] = args[key]

            if args["entity"] == Entities.Tree and j % 2 == 0:
                tile["entity"] = Entities.Grass
            grid[i].append(tile)
    return grid


# [
#     [{args}, ...,{args}],
#     ...,
#     [{args}, ...,{args}],
# ]


def field_list(size, information) -> list[list]:
    grid = []
    for i in range(size):
        grid.append([])
        for _ in range(size):
            grid[i].append(information)

    return grid


# [
#     [information, ..., information],
#     ...,
#     [information, ..., information],
# ]


def field_tuple(size) -> list[list[tuple]]:
    grid = []
    for i in range(size):
        for j in range(size):
            grid.append((j, i))
    return grid


# [
#     [(0,      0), ..., (size-1,      0)],
#     ...,
#     [(0, size-1), ..., (size-1, size-1)]
# ]


def field_dict_list(start, end) -> dict[int, list]:
    grid = {}
    for i in range(start, end):
        grid[i] = []
    return grid


# {
#     0: [(x0, y0), ..., (x, y)],
#     ...,
#     15: [(x0, y0), ..., (x, y)],
# }
