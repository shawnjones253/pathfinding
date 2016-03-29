"""a pathfinding simulation for a fictional character named Robbie"""

from __future__ import print_function
from operator import itemgetter
from collections import deque

__author__ = "Shawn Jones"

#Robbie's house
rooms = [
    ['living-room',
     ['north', 'front-stairs'],
     ['south', 'dining-room'],
     ['east', 'kitchen']],
    ['upstairs-bedroom',
     ['west', 'library'],
     ['south', 'front-stairs']],
    ['dining-room',
     ['north', 'living-room'],
     ['east', 'pantry'],
     ['west', 'downstairs-bedroom']],
    ['kitchen',
     ['west', 'living-room'],
     ['south', 'pantry']],
    ['pantry',
     ['north', 'kitchen'],
     ['west', 'dining-room']],
    ['downstairs-bedroom',
     ['north', 'back-stairs'],
     ['east', 'dining-room']],
    ['back-stairs',
     ['south', 'downstairs-bedroom'],
     ['north', 'library']],
    ['front-stairs',
     ['north', 'upstairs-bedroom'],
     ['south', 'living-room']],
    ['library',
     ['east', 'upstairs-bedroom'],
     ['south', 'back-stairs']]
    ]

#Robbie's current location
loc = ''

#Create a list of valid room names
roomnames = list(map(itemgetter(0), rooms))

def SetRobbieLocation(room):
    """Sets Robbie's location to input room"""
    global loc
    if room not in roomnames:
        raise ValueError(str(room) + ' is not a valid room name.')
    else:
        loc = room

def Choices(room):
    """Returns a list of rooms Robbie can move to from the input room"""
    if room not in roomnames:
        raise ValueError(str(room) + ' is not a valid room name.')
    else:
        return [i[1:] for i in rooms if i[0] == str(room)][0]

def Look(dir, room):
    """
    Returns the room in the direction specified from the input room,
    or None if no room exists in that direction.
    """
    if room not in roomnames:
        raise ValueError(str(room) + ' is not a valid room name.')
    elif dir not in ['north', 'east', 'south', 'west']:
        raise ValueError(str(dir) + ' is not a valid direction.')
    for elem in Choices(room):
        if elem[0] == dir:
            return elem[1]
    return None

def Where():
    """Prints Robbie's current location"""
    if loc[-6:] == 'stairs':
        print('Robbie is on the ' + str(loc))
    elif loc[:8] == 'upstairs' or loc[:10] == 'downstairs':
        print('Robbie is in the ' + str(loc))
    elif loc == 'library':
        print('Robbie is upstairs in the ' + str(loc))
    else:
        print('Robbie is downstairs in the ' + str(loc))

def Move(dir):
    """Moves Robbie in the direction specified, provided a room exists in that direction"""
    """Prints error if not possible to move, otherwise prints Robbie's new location"""
    global loc
    if dir not in ['north', 'east', 'south', 'west']:
        raise ValueError(str(dir) + ' is not a valid direction.')
    result = Look(dir, loc)
    if result == None:
        print('Ouch! Robbie hit a wall.')
    else:
        SetRobbieLocation(result)
        Where()

def FindPath(source, dest):
    """Find and return a path (list of rooms) from source to dest, using BFS"""
    visited = {source}
    candidates = deque([])
    for elem in Choices(source):
        if elem[1] == dest:
            return elem
        else:
            candidates.append([elem])
            visited.add(elem[1])
    while(True):
        path = candidates.popleft()
        for elem in Choices(path[-1][1]):
            if elem[1] not in visited:
                newpath = path[:]
                newpath.append(elem)
                if elem[1] == dest:
                    return newpath
                candidates.append(newpath)
                visited.add(elem[1])

def Traverse(source, dest):
    """Print path from source to dest"""
    if source not in roomnames or dest not in roomnames:
        raise ValueError(str(room) + ' is not a valid room name.')
    for elem in FindPath(source, dest):
        print('Go ' + str(elem[0]) + ' to ' + str(elem[1]))

#Set Robbie's initial location
SetRobbieLocation('kitchen')