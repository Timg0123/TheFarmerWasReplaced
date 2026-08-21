from __builtins__ import *

plant_data = {
    Entities.Grass: Grounds.Grassland,
    Entities.Bush: Grounds.Grassland,
    Entities.Tree: Grounds.Grassland,
    Entities.Carrot: Grounds.Soil,
    Entities.Sunflower: Grounds.Soil,
    Entities.Pumpkin: Grounds.Soil,
    Entities.Cactus: Grounds.Soil,
}


def check_till(entity):
    if get_ground_type() != plant_data[entity]:
        till()


def check_water(water_level):
    if get_water() < water_level and num_items(Items.Water) != 0:
        use_item(Items.Water)


def for_rows(size, dir, functions: dict[Callable, Any]):
    drones = []
    if dir == East:
        dir_spawner = North
    else:
        dir_spawner = East
    for _ in range(size):
        for func in functions:
            if num_drones() == max_drones():
                func(functions[func])
            else:
                drones.append(spawn_drone(func, functions[func]))
        move(dir_spawner)
    return drones


def for_all(size, dir, functions: dict[Callable, Any]) -> list[Drone]:
    drones = []
    if dir == East:
        dir_spawner = North
    else:
        dir_spawner = East

    def row():
        for _ in range(size - 1):
            for func in functions:
                if functions[func] == None:
                    func()
                else:
                    func(functions[func])
            move(dir)
        for func in functions:
            if functions[func] == None:
                func()
            else:
                func(functions[func])

    for _ in range(size):
        if num_drones() == max_drones():
            row()
        else:
            drones.append(spawn_drone(row))
        move(dir_spawner)
    return drones
