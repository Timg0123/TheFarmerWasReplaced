import utils
from __builtins__ import *


def harvest_column(water_min: int):
    change_hat(Hats.Golden_Sunflower_Hat)
    while True:
        if get_pos_y() != 0:
            utils.move_to((get_pos_x(), 0))

        for _ in range(get_world_size()):
            if get_ground_type() != Grounds.Soil:
                till()
            if get_water() < water_min:
                use_item(Items.Water)
            if can_harvest():
                harvest()
            if get_entity_type() == None:
                plant(Entities.Sunflower)
            move(North)


def start_sunflower(size, water_min: int):
    for _ in range(size - 1):
        if spawn_drone(harvest_column, water_min):  # pyright: ignore
            move(East)
    harvest_column(water_min)
