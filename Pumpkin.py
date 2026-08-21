import utils
# make everything for one row -> pass the row to start_pumpkin from main and wait on other drones before harvest


def check_pumpkin():  # Returns True if Entity is Pumpkin
    if get_entity_type() != Entities.Pumpkin:
        harvest()
        plant(Entities.Pumpkin)
    else:
        return True


def replace_dead(size, grid):
    dir = East
    need_check = utils.copy(grid)
    quick_print(need_check)

    utils.move_to((0, 0))
    for _ in range(2):
        for _ in range(size):
            for _ in range(size):
                if check_pumpkin():
                    need_check.remove((get_pos_x(), get_pos_y()))
                dir = utils.move_to_next_tile(dir, size)

    while len(need_check) != 0:
        for check in need_check:
            utils.move_to((check))
            if check_pumpkin():
                need_check.remove(check)


def start_pumpkin(size, grid):
    # utils.replant_all(size, Entities.Pumpkin)
    replace_dead(size, grid)
    harvest()
    utils.move_to((0, 0))
