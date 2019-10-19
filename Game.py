import gaming_tools
import random
import time

def gen_ressources():
    randomnb = random.randint(5, 25)
    return randomnb

def get_status_ship(ship):
    if gaming_tools.is_ship_broken(ship) == 1:
        print('Ship does need repairs')
    else: print("Ship %s don't need repairs")

def create_planet(planet, coord_x, coord_y):
    if gaming_tools.planet_exists(planet):
        raise ValueError("Planet %s already exists" % planet)
        print('This planet already exists')
    else:
     gaming_tools.add_new_planet(planet, gen_ressources())
     gaming_tools.set_planet_location(planet,coord_x,coord_y)


def get_status_planet(planet):
    print(gaming_tools.get_planet_resources(planet))
    if not planet_exists(planet):
        raise ValueError('planet %s does not exist' % planet)
        print('This planet does not exist.')

def create_ship(ship):
    if gaming_tools.ship_exists(ship):
        raise ValueError('ship %s already exists' % ship)
        print('Ship %s already exists' % ship)
    else:
        gaming_tools.add_new_ship(ship, speed=1, broken=0)
