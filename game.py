# -*- coding: utf-8 -*-
import gaming_tools as gt
import random
import time


def restart_game():
    """Load game.db, reset the game and add base planets
    Aldebaran and Epislon Aurigae.
    
    """
    gt._load_game_db()
    gt.reset_game()
    gt.add_new_planet('Aldebaran',0)
    gt.add_new_planet('Epsilon Aurigae',0)
    gt.set_planet_location('Aldebaran',0,0)
    gt.set_planet_location('Epsilon Aurigae',1000,1000)


def create_ship(ship, planet='Aldebaran'):
    """Create a ship on Aldebaran
    
    Parameters
    ----------
    ship: ship name (str)

    """
    if gt.ship_exists(ship):
        return 'This ship already exists'
    else:
        gt.add_new_ship(ship, speed=1, broken=0)
        gt.set_ship_location(ship,planet)
        gt.set_when_ship_is_ready(ship,time_stamp=0)

def create_planet(planet, coord_x, coord_y):
    """Create a planet
    
    Parameters
    ----------
    planet: planet name (str)
    coord_x: X coordinate
    coord_y: Y coordinate

    """
    if gt.planet_exists(planet):
        return 'This planet already exists'
    else:
     gt.add_new_planet(planet, random.randint(5, 20))
     gt.set_planet_location(planet,coord_x,coord_y)


def gen_broken():
    """Create a number between 1 and 3
    to randomize if ship is broken or not
    
    """
    randomnb = random.randit(1,3)
    return randomnb

def broken_display(ship):
    """Simply display text and not 1 or 0
    when user checks ship status for broken

    """
    if gt.is_ship_broken(ship) == True:
        return "Yes"
    else:
        return "No"

def get_status_ship(ship):  
    """Get status of a ship
    
    Parameters
    ----------
    ship: ship name (str)

    """    
    return 'Ship location: ', gt.get_ship_location(ship), 'Speed: ', gt.get_ship_speed(ship), 'Need repairs ?: ', broken_display(ship), 'Ship will be ready in: ', gt.get_when_ship_is_ready(ship)

def get_status_planet(planet):
    """Get status of a planet
    
    Parameters
    ----------
    planet: planet name (str)

    """
    return 'Location: ', gt.get_planet_location(planet), 'Resources: ', gt.get_planet_resources(planet)
    if not gt.planet_exists(planet):
        return 'This planet does not exist.'

def travel(ship,planet,speed):
    """Make the ship travel to another planet.
    
    Parameters
    ----------
    ship: ship name (str)
    planet: planet name(str)
    speed: ship speed (int)

    """
    gt.set_ship_location(ship,planet)



def repair(ship):
    """Repair the ship if it is broken and 
    there are enough resources on the planet.
    
    Parameters
    ----------
    ship: ship name (str)

    """
    if gt.get_when_ship_is_ready(ship) <= time.time:
    # If time is smaller or equal than time of the ship
        if gt.is_ship_broken(ship) == True: 
        # If ship is broken
            if gt.get_planet_resources(gt.get_ship_location(ship)) >= 3:
            # If resources on the planet is greater or equal to 3
                gt.set_planet_resources(gt.get_ship_location(ship), gt.get_planet_resources(gt.get_ship_location(ship)) -3 )
                gt.set_ship_broken(ship,0)
                gt.set_when_ship_is_ready(ship,time.time()+60)
                return 'Ship in repair. Your ship is now in sleep mode for: ',gt.get_when_ship_is_ready(ship)
            else: 
                return 'Not enough resources on the planet to repair'
        else:
            return 'This ship is not broken'
    else:
        return 'Your ship is not ready.'

def upgrade(ship,nbup):
    """Upgrade a ship with the number of upgrade 
    chosen by the user
    
    Parameters
    ----------
    ship: ship name (str)
    nbup: number of upgrade to apply (int)

    """
    if gt.get_when_ship_is_ready(ship) <= time.time():
    # If time is smaller or equal than time of the ship
        if gt.get_planet_resources(gt.get_ship_location(ship)) >= 1:
        # If the resources on the planet is greater or equal to 1
            gt.set_ship_speed(ship,gt.get_ship_speed(ship) + 3)
            gt.set_planet_resources(gt.get_ship_location(ship), gt.get_planet_resources(gt.get_ship_location(ship)) - (nbup) )
            gt.set_when_ship_is_ready(ship,time.time()+40*nbup**2)
            return 'This Your ship is now in sleep mode for: ',gt.get_when_ship_is_ready(ship)
        else:
            return 'Not enough resources on the planet to upgrade'
    else:
        return 'Your ship is not ready.'
