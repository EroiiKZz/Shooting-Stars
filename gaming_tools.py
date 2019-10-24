"""This module implements basic gaming operations.  These
functions should be used to create higher level operations.
In particular, they should NOT be directly used by players."""


import os, pickle, random


# === game management functions ===
def reset_game():
    """Remove all planets and ships."""
    
    if os.path.exists('game.db'):
        os.remove('game.db')


# === database management (do not use outside of API) ===
def _load_game_db():
    """Loads the game database.
    
    Returns
    -------
    game_db: contains all game information (dict)
    
    Notes
    -----
    If no database exists, an empty one is automatically created.
    
    """
    
    try:
        fd = open('game.db', 'rb')
        game_db = pickle.load(fd)
        fd.close()
    except:
        game_db =  {'planets':{},
                    'ships':{}}

    return game_db


def _dump_game_db(game_db):
    """Dumps the game database.
    
    Parameters
    -------
    game_db: contains all game information (dict)
    
    """
    
    fd = open('game.db', 'wb')
    pickle.dump(game_db, fd)
    fd.close()



# === planet management functions ===
def planet_exists(planet):
    """Tells whether a planet already exists or not.
    
    Parameters
    ----------
    planet: planet name (str)
    
    Returns
    -------
    planet: True if planet already exists, False otherwise (bool)
    
    """
    
    game_db = _load_game_db()
    
    return planet in game_db['planets']
    
    
def add_new_planet(planet, resources):
    """Adds a new planet to the game.
        
    Parameters
    ----------
    planet: planet name (str)
    resources: available resources (int)

    Raises
    ------
    ValueError: if there already is a planet with the same name
    ValueError: if resources is strictly negative
    
    """
    
    game_db = _load_game_db()
    
    if planet_exists(planet):
        raise ValueError('planet %s already exists' % planet)
    if resources < 0:
        raise ValueError('resources cannot be negative (resources = %d)' % resources)

    game_db['planets'][planet] = {'resources':resources}
    
    _dump_game_db(game_db)


def set_planet_location(planet, coord_x, coord_y):
    """Places a planet on the board.
        
    Parameters
    ----------
    planet: planet name (str)
    coord_x: x coordinate of the planet (int)
    coord_y: y coordinate of the planet (int)
        
    Raises
    ------
    ValueError: if the planet does not exist
    
    """
    
    game_db = _load_game_db()
    
    if not planet_exists(planet):
        raise ValueError('planet %s does not exist' % planet)

    game_db['planets'][planet]['location'] = (coord_x, coord_y)
    
    _dump_game_db(game_db)
    

def get_planet_location(planet):
    """Returns the location of a planet.
        
    Parameters
    ----------
    planet: planet name (str)
    
    Returns
    -------
    coord_x: x coordinate of the planet (int)
    coord_y: y coordinate of the planet (int)
        
    Raises
    ------
    ValueError: if the planet does not exist
    ValueError: if the planet is not yet placed on the board
    
    """
    
    game_db = _load_game_db()
    
    if not planet_exists(planet):
        raise ValueError('planet %s does not exist' % planet)
    if 'location' not in game_db['planets'][planet]:
        raise ValueError('planet %s is not yet placed on a planet' % planet)
    
    return game_db['planets'][planet]['location']
    
    
def set_planet_resources(planet, resources):
    """Changes the available resources of a planet.
        
    Parameters
    ----------
    planet: planet name (str)
    resources: available resources (int)
    
    Raises
    ------
    ValueError: if the planet does not exist
    ValueError: if resources is strictly negative
    
    """
    
    game_db = _load_game_db()
    
    if not planet_exists(planet):
        raise ValueError('planet %s does not exist' % planet)
    if resources < 0:
        raise ValueError('resources cannot be negative (resources = %d)' % resources)
    
    game_db['planets'][planet]['resources'] = resources
    
    _dump_game_db(game_db)


def get_planet_resources(planet):
    """Returns the available resources of a planet.
    
    Parameters
    ----------
    planet: planet name (str)
    
    Returns
    -------
    resources: available resources (int)
    
    Raises
    ------
    ValueError: if the planet does not exist
   
    """
    
    game_db = _load_game_db()

    if not planet_exists(planet):
        raise ValueError('planet %s does not exist' % planet)

    return game_db['planets'][planet]['resources']
    


# === ship management functions ===
def ship_exists(ship):
    """Tells whether a ship already exists or not.
    
    Parameters
    ----------
    ship: ship name (str)
    
    Returns
    -------
    result: True if ship already exists, False otherwise (bool)
    
    """
    
    game_db = _load_game_db()
    
    return ship in game_db['ships']
    
    
def add_new_ship(ship, speed, broken):
    """Adds a new ship to the game.
        
    Parameters
    ----------
    ship: ship name (str)
    speed: ship speed (int)
    broken: is ship broken (bool)
    
    Raises
    ------
    ValueError: if there already is a ship with the same name
    ValueError: if speed is strictly negative
    
    """
    
    game_db = _load_game_db()
    
    if ship_exists(ship):
        raise ValueError('ship %s already exists' % ship)
    if speed < 0:
        raise ValueError('speed cannot be speed (speed = %d)' % speed)
    
    game_db['ships'][ship] = {'speed':speed, 'broken':broken}
    
    _dump_game_db(game_db)
    
    
def set_ship_location(ship, planet):
    """Places a  ship on a planet.
        
    Parameters
    ----------
    ship: ship name (str)
    planet: planet name (str)
        
    Raises
    ------
    ValueError: if the ship does not exist
    ValueError: if the planet does not exist
    
    """
    
    game_db = _load_game_db()
    
    if not ship_exists(ship):
        raise ValueError('ship %s does not exist' % ship)
    if not planet_exists(planet):
        raise ValueError('planet %s does not exist' % ship)

    game_db['ships'][ship]['planet'] = planet
    
    _dump_game_db(game_db)
    

def get_ship_location(ship):
    """Returns the name of the planet where the ship is.
        
    Parameters
    ----------
    ship: ship name (str)
        
    Raises
    ------
    ValueError: if the ship does not exist
    ValueError: if the ship is not yet placed on a planet
    
    """
    
    game_db = _load_game_db()
    
    if not ship_exists(ship):
        raise ValueError('ship %s does not exist' % ship)
    if 'planet' not in game_db['ships'][ship]:
        raise ValueError('ship %s is not yet placed on a planet' % ship)
    
    return game_db['ships'][ship]['planet']


def set_ship_speed(ship, speed):
    """Modifies the speed of a ship.
        
    Parameters
    ----------
    ship: ship name (str)
    speed: ship speed (int)
    
    Raises
    ------
    ValueError: if the ship does not exist
    ValueError: if speed is strictly negative
     
    """
    
    game_db = _load_game_db()
    
    if not ship_exists(ship):
        raise ValueError('ship %s does not exist' % ship)
    if speed < 0:
        raise ValueError('speed cannot be negative (speed = %d)' % speed)
    
    game_db['ships'][ship]['speed']  = speed
    
    _dump_game_db(game_db)
    
    
def get_ship_speed(ship):
    """Returns the speed of a ship.
        
    Parameters
    ----------
    ship: ship name (str)
    
    Returns
    -------
    speed: ship speed (int)
    
    Raises
    ------
    ValueError: if the ship does not exist
    
    """
    
    game_db = _load_game_db()
    
    if not ship_exists(ship):
        raise ValueError('ship %s does not exist' % ship)
    
    return game_db['ships'][ship]['speed'] 
    
    
def set_ship_broken(ship, broken):
    """Sets a ship as broken or not.
        
    Parameters
    ----------
    ship: ship name (str)
    broken: is ship broken (bool)
        
    Raises
    ------
    ValueError: if the ship does not exist
     
    """
    
    game_db = _load_game_db()
    
    if not ship_exists(ship):
        raise ValueError('ship %s does not exist' % ship)
    
    game_db['ships'][ship]['broken']  = broken
    
    _dump_game_db(game_db)

        
def is_ship_broken(ship):
    """Tells whether a ship is broken or not.
   
    Parameters
    ----------
    ship: ship name (str)
    
    Returns
    -------
    result: True if ship is broken, False otherwise (bool)
    
    Raises
    ------
    ValueError: if the ship does not exist
    
    """
    
    game_db = _load_game_db()
    
    if not ship_exists(ship):
        raise ValueError('ship %s does not exist' % ship)
    
    return game_db['ships'][ship]['broken']
    

def set_when_ship_is_ready(ship, time_stamp):
    """Stores when the ship will be ready after its last action.
        
    Parameters
    ----------
    ship: ship name (str)
    time_stamp: when the ship is available (float)
        
    Raises
    ------
    ValueError: if the ship does not exist
    ValueError: if time_stamp is strictly negative
     
    """
    
    game_db = _load_game_db()
    
    if not ship_exists(ship):
        raise ValueError('ship %s does not exist' % ship)
    if time_stamp < 0:
        raise ValueError('time stamp cannot be negative (time_stamp = %d)' % time_stamp)
    
    game_db['ships'][ship]['availability']  = time_stamp
    
    _dump_game_db(game_db)


def get_when_ship_is_ready(ship):
    """Returns when the ship will be ready after its last action.
       
    Parameters
    ----------
    ship: ship name (str)
   
    Returns
    -------
    time_stamp: when the ship is available (float)
   
    Raises
    ------
    ValueError: if the ship does not exist   
   
    Notes
    -----
    If the ship never made any action, time_stamp is 0.
       
    """
   
    game_db = _load_game_db()
   
    if not ship_exists(ship):
        raise ValueError('ship %s does not exist' % ship)
   
    if 'availability' in game_db['ships'][ship]:
        return game_db['ships'][ship]['availability']
    else:
        return 0
