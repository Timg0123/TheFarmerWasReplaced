from __builtins__ import *
import farm_utils
import utils

DIRECTIONS = [North, East, South, West]


def turn_right(index):
    return (index + 1) % 4


def turn_left(index):
    return (index - 1) % 4


def regrow_maze(size):
    if can_harvest():
        harvest()
    plant(Entities.Bush)
    substance = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


def search_treasure(
    preffered_side: string, regrow=False, size=32
):  # for each drone: store original pos and treasure coords. if the coords change during search: move_to original pos
    while True:
        original_pos = (get_pos_x(), get_pos_y())
        for _ in range(6):
            while measure() == None:
                if regrow == True:
                    regrow_maze(size)
            original_treasure: tuple[int, int] = measure()  # pyright: ignore
            index = 0
            while measure() == original_treasure:
                if preffered_side == "left":
                    index = turn_left(index)
                    while not can_move(DIRECTIONS[index]):
                        index = turn_right(index)
                elif preffered_side == "right":
                    index = turn_right(index)
                    while not can_move(DIRECTIONS[index]):
                        index = turn_left(index)
                move(DIRECTIONS[index])
                if (get_pos_x(), get_pos_y()) == measure():
                    harvest()

        harvest()
        utils.move_to(original_pos)
        do_a_flip()


def distribute_drones(size):
    harvest()
    utils.move_to((0, 0))
    drones = []
    for i in range(max_drones() - 1):
        if i % 2 == 0:
            drones.append(spawn_drone(search_treasure, "left"))  # pyright: ignore
        else:
            drones.append(spawn_drone(search_treasure, "right"))  # pyright: ignore
        move(North)
        move(East)
    search_treasure("left", True)


distribute_drones(32)


def start_maze(size):
    pass


start_maze(32)
