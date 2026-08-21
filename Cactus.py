# pyright: reportOperatorIssue=false

# TODO: Cocktail Shaker optimization
import utils
import farm_utils


def cocktail_sort(args):
    size, dir = args[0], args[1]
    opposite_dir = utils.turn_left(utils.turn_left(dir))
    start = 0
    end = size - 2
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(start, end):
            if measure() > measure(dir):
                swapped = True
                swap(dir)
            move(dir)
        if measure() > measure(dir):
            swapped = True
            swap(dir)
        end = end - 1

        swapped = False
        for i in range(end, start, -1):
            if measure() < measure(opposite_dir):
                swapped = True
                swap(opposite_dir)
            move(opposite_dir)
        if measure() < measure(opposite_dir):
            swapped = True
            swap(opposite_dir)
        start = start + 1


def start_cactus(size):  # grid: [[...], ..., [...]]
    utils.move_to((0, 0))
    farm_utils.for_all(
        32,
        North,
        {harvest: None, farm_utils.check_till: Entities.Cactus, plant: Entities.Cactus},
    )

    utils.move_to((0, 0))
    drones = farm_utils.for_rows(size, North, {cocktail_sort: [size, North]})
    for drone in drones:
        wait_for(drone)
    utils.move_to((0, 0))
    drones = farm_utils.for_rows(size, East, {cocktail_sort: [size, East]})
    for drone in drones:
        wait_for(drone)
