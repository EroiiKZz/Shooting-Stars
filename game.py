# -*- coding: utf-8 -*-
import gaming_tools as gt
import random
import time

def restart():
    """Load game.db, reset the game and add base planets
    Aldebaran and Epislon Aurigae.
    
    """
    gt.reset_game()
    gt.add_new_planet('Aldebaran',0)
    gt.add_new_planet('Epsilon Aurigae',0)
    gt.set_planet_location('Aldebaran',0,0)
    gt.set_planet_location('Epsilon Aurigae',1000,1000)
    print('A new age beggins')

def create_ship(ship):
    """Create a ship on Aldebaran
    
    Parameters
    ----------
    ship: ship name (str)

    """
    if gt.ship_exists(ship):
    # If the ship already exists
        print( '%s already exists' % ship)
    else:
        gt.add_new_ship(ship, speed=1, broken=0)
        gt.set_ship_location(ship,planet='Aldebaran')
        gt.set_when_ship_is_ready(ship,time_stamp=0)
        print( '%s is now online and ready for collapsar jump' % ship)

def create_planet(planet, coord_x, coord_y):
    """Create a planet
    
    Parameters
    ----------
    planet: planet name (str)
    coord_x: X coordinate
    coord_y: Y coordinate

    """
    if gt.planet_exists(planet):
    # If the planet already exists
        print( '% already exists' % planet)
    else:
     resources = random.randint(5, 20)
     gt.add_new_planet(planet, resources)
     gt.set_planet_location(planet,coord_x,coord_y)
    print('%s appears at X: %s || Y: %s with %s resources' % (planet,coord_x,coord_y,resources))

def status_ship(ship):  
    """Get status of a ship
    
    Parameters
    ----------
    ship: ship name (str)

    """    
    whenisready = gt.get_when_ship_is_ready(ship)-time.time()
    print('%s is on %s and has a speed of %s parsec per second' % (ship,gt.get_ship_location(ship),gt.get_ship_speed(ship)))
    if gt.is_ship_broken(ship) == True:
    # If the ship is broken
        print( "/!\\"" %s is broken and unable to perform upgrades and collapsar jumps /!\\""" % ship)
    else:
        print( "%s is not broken and can move" % ship)
        if gt.get_when_ship_is_ready(ship) >= time.time():
        # If current time is greater or equal to the time of the ship
            print( '%s will be ready in: %.2f seconds' % (ship,whenisready))
        else: 
            print('%s is ready' % ship)

def status_planet(planet):
    """Get status of a planet
    
    Parameters
    ----------
    planet: planet name (str)

    """
    print( '%s is at: %s and has %s resources' %(planet,gt.get_planet_location(planet), gt.get_planet_resources(planet)))
    
def travel(ship,planet):
    """Make the ship travel to another planet.
    
    Parameters
    ----------
    ship: ship name (str)
    planet: planet name(str)
    """
    if gt.is_ship_broken(ship) == False:
    # If the ship is not broken
        if gt.get_when_ship_is_ready(ship) <= time.time():
        # If current time is greater or equal to the time of the ship
            if gt.get_ship_location(ship) != planet:
            # If current time is greater or equal to the time of the ship
                gt.get_ship_location(ship)
                Xa,Ya = gt.get_planet_location(gt.get_ship_location(ship))
                gt.set_ship_location(ship,planet)
                Xb,Yb = gt.get_planet_location(gt.get_ship_location(ship))
                distance = ((Xb-Xa)**2 + (Yb-Ya)**2)**1/2
                travel_time = distance/gt.get_ship_speed(ship)            
                gt.set_when_ship_is_ready(ship,time.time()+travel_time)
                print( '%s will arrive in: %.2f seconds.' % (ship,travel_time))
                randomnb = random.randint(1,3)
                if randomnb == 1:
                # If the random number = 1 then ship is broken
                    gt.set_ship_broken(ship,1)
                    print ('Your reactor overheated :( . Repair needed')
            else:
                print('%s is already on %s.' % (ship, planet))
        else:
            whenisready = gt.get_when_ship_is_ready(ship)-time.time()
            print('%s is not ready. It will be in: %.2f seconds' % (ship,whenisready))
    else: 
        print('%s is broken' % ship)

def repair(ship):
    """Repair the ship if it is broken and 
    there are enough resources on the planet.
    
    Parameters
    ----------
    ship: ship name (str)

    """
    
    if gt.get_when_ship_is_ready(ship) <= time.time():
    # If time is smaller or equal than time of the ship
        if gt.is_ship_broken(ship) == True: 
        # If ship is broken
            if gt.get_planet_resources(gt.get_ship_location(ship)) >= 3:
            # If resources on the planet is greater or equal to 3
                gt.set_planet_resources(gt.get_ship_location(ship), gt.get_planet_resources(gt.get_ship_location(ship)) -3 )
                gt.set_ship_broken(ship,0)
                gt.set_when_ship_is_ready(ship,time.time()+20*gt.get_ship_speed(ship))
                whenisready = gt.get_when_ship_is_ready(ship)-time.time()
                print( 'Repair in progress. %s will be ready in: %.2f seconds' % (ship,whenisready))
            else: 
                print( 'Not enough resources on the %s to repair' % gt.get_ship_location(ship))
        else:
            print( '%s is not broken' % ship)
    else:
        whenisready = gt.get_when_ship_is_ready(ship)-time.time()
        print( '%s is not ready. Wait: %.2f seconds' % (ship,whenisready))

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
            gt.set_ship_speed(ship,gt.get_ship_speed(ship) + nbup)
            gt.set_planet_resources(gt.get_ship_location(ship), gt.get_planet_resources(gt.get_ship_location(ship)) - (nbup) )
            gt.set_when_ship_is_ready(ship,time.time()+40*nbup**2)
            whenisready =gt.get_when_ship_is_ready(ship)-time.time()
            print( '%s will be ready in: %.2f seconds' % (ship,whenisready))
        else:
            print( 'Not enough resources on %s to upgrade' % gt.get_ship_location(ship))
    else:
        whenisready =gt.get_when_ship_is_ready(ship)-time.time()
        print( '%s is not ready. It will be in: %.2f seconds ' % (ship,whenisready))

def check_win(ship):
    """User checks if he is on Epsilon and has won
    
    Parameters
    ----------
    ship: ship name (str)
    """
    if time.time() >= gt.get_when_ship_is_ready(ship):
    # If time is bigger or equal to ship time
        if gt.get_ship_location(ship) == "Epsilon Aurigae":
        # If ship location isn't the same as Epsilon
            print('Congratulations %s, you win ! :)')
        else:
            print('%s is not on Epsilon Aurigae' % ship)
    else: 
        print('%s is not ready' % ship)
