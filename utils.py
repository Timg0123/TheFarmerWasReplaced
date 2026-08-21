def move_to(point):
    x = get_pos_x()
    y = get_pos_y()
    dx = point[0] - x
    dy = point[1] - y

    if abs(dx) > get_world_size() / 2:
        if dx > 0:
            while get_pos_x() != point[0]:
                move(West)
        else:
            while get_pos_x() != point[0]:
                move(East)
    else:
        if dx > 0:
            while get_pos_x() != point[0]:
                move(East)
        else:
            while get_pos_x() != point[0]:
                move(West)

    if abs(dy) > get_world_size() / 2:
        if dy > 0:
            while get_pos_y() != point[1]:
                move(South)
        else:
            while get_pos_y() != point[1]:
                move(North)
    else:
        if dy > 0:
            while get_pos_y() != point[1]:
                move(North)
        else:
            while get_pos_y() != point[1]:
                move(South)


def move_dino(dir, size):
    x = get_pos_x()
    y = get_pos_y()

    if dir == East:
        if y == size - 1:
            if x == size - 1:
                dir = South
        elif x == size - 1:
            dir = North
    elif dir == West:
        if y == size - 1:
            if x == 0:
                dir = South
        elif x == 1:
            dir = North

    elif dir == North:
        if x == size - 1:
            dir = West
        else:
            dir = East
    elif dir == South:
        if y == 0:
            if x == size - 1:
                dir = West
            else:
                dir = East
    move(dir)
    return dir


def move_to_next_tile(dir, size):
    x = get_pos_x()

    if x == size - 1 or x == 0:
        dir = North
    if dir == North:
        if x == 0:
            dir = East
        if x == size - 1:
            dir = West

    move(dir)
    return dir


def sleep(seconds):
    if seconds == 0:
        return
    do_a_flip()
    sleep(seconds - 1)


def copy(arr):
    new = []
    for row in arr:
        new_row = []
        for item in row:
            new_row.append(item)
        new.append(new_row)
    return new


def turn_left(dir):
    if dir == East:
        return North
    elif dir == North:
        return West
    elif dir == West:
        return South
    else:
        return East
