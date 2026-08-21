from __builtins__ import *
import farm_utils
import utils


def turn_right(index):
    return (index + 1) % 4


def turn_left(index):
    return (index - 1) % 4

directions = [North, East, South, West]

def search_treasure(preffered_side: string): # for each drone: store original pos and treasure coords. if the coords change during search: move_to original pos
    original_pos = (get_pos_x(), get_pos_y())
    original_treasure: tuple[int, int] = measure() # pyright: ignore
    index = 0
    treasure = measure()
    while measure() == original_treasure:
        if preffered_side == "left":
            index = turn_left(index)
            while not can_move(directions[index]):
                index = turn_right(index)
        elif preffered_side == "right":
            index = turn_right(index)
            while not can_move(directions[index]):
                index = turn_left(index)
        move(directions[index])
        if (get_pos_x(), get_pos_y()) == measure():
            harvest()
    

def distribute_drones():
    utils.move_to((0, 0))
    drones = []
    for _ in range(max_drones()-1):
        drones.append(spawn_drone(search_treasure, "left")) # pyright: ignore
        move(North)
        move(East)
    search_treasure("left")



def regrow_maze(size):
    if can_harvest():
        harvest()
    plant(Entities.Bush)
    substance = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


def start_maze(size):
    pass

start_maze(32)
