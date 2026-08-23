import farm_utils
import utils


def is_pumpkin():  # Returns True if Entity is Pumpkin
    if get_entity_type() != Entities.Pumpkin:
        harvest()
        plant(Entities.Pumpkin)
    else:
        return True


def replace_dead(field):
    need_check = field[:]
    while len(need_check) != 0:
        for x in need_check:
            utils.move_to((x, get_pos_y()))
            if is_pumpkin():
                need_check.remove(x)


def start_pumpkin(size):
    farm_utils.for_all(
        size, East, {farm_utils.check_till: Entities.Pumpkin, plant: Entities.Pumpkin}
    )
    field = []
    for i in range(size):
        field.append(i)

    while True:
        farm_utils.for_rows(size, East, {replace_dead: field})
        utils.sleep(1)
        harvest()
        farm_utils.for_all(size, East, {plant: Entities.Pumpkin})
