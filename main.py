import Cactus
import farm_utils
import Fields
#import Maze
import Pumpkin
import Sunflower
import utils
from __builtins__ import *


def dino_game(size):
    dir = East
    for _ in range(size):
        for _ in range(size):
            if can_harvest():
                harvest()
            dir = utils.move_dino(dir, size)


size = get_world_size()
min_water_level = 0
use_fertilizer = False
modes = ["cactus", "dino", "maze", "pumpkin", "sunflower", "poly", "other"]
change_hat(Hats.Golden_Cactus_Hat)

while True:
    plant(Entities.Pumpkin)
    use_item(Items.Fertilizer)
    while not can_harvest():
        if get_entity_type() == Entities.Dead_Pumpkin:
            harvest()
            plant(Entities.Pumpkin)
        use_item(Items.Fertilizer)
    harvest()

def main():
    harvest()
    utils.move_to((0, 0))
    selected_mode = 3
    selected_entity = Entities.Sunflower
    pet_the_piggy()
    

    if modes[selected_mode] == "cactus":
        change_hat(Hats.Golden_Cactus_Hat)
        while True:
            Cactus.start_cactus(size)
    if modes[selected_mode] == "dino":
        change_hat(Hats.Dinosaur_Hat)
        while True:
            dino_game(size)
    elif modes[selected_mode] == "maze":
        while True:
            Maze.start_maze(size)
    elif modes[selected_mode] == "sunflower":
        Sunflower.start_sunflower(size, min_water_level)
    elif modes[selected_mode] == "pumpkin":
        change_hat(Hats.Pumpkin_Hat)
        grid = Fields.field_tuple(size)
        while True:
            Pumpkin.start_pumpkin(size, grid)
    # elif modes[selected_mode] == "poly":
    #     while True:
    #         pass
    else:
        farm_utils.for_all(
            size,
            East,
            {
                harvest: None,
                farm_utils.check_till: selected_entity,
                plant: selected_entity,
                farm_utils.check_water: min_water_level,
            },
        )
        utils.move_to((0, 0))
        while True:
            farm_utils.for_all(
                size,
                East,
                {
                    harvest: None,
                    plant: selected_entity,
                    farm_utils.check_water: min_water_level,
                },
            )
            utils.move_to((0, 0))


if __name__ == "__main__":
    main()
