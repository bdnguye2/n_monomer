#!/usr/bin/python3


# Generates the coordinates of face-centered unit cell
def gen_unit(coord,lat_const):
    tmp1 = []
    # Coordinates of 6 faces
    for i in [lat_const/2,-lat_const/2]:
        tmp1 = tmp1 + [[coord[0]+i,coord[1],coord[2]]] \
            + [[coord[0],coord[1]+i,coord[2]]] \
            + [[coord[0],coord[1],coord[2]+i]]

    # Coordinates of 8 corners
    for i in [lat_const/2,-lat_const/2]:
        tmp1 = tmp1 + [[coord[0]+i,coord[1]+i,coord[2]+i]] \
            + [[coord[0]+i,coord[1]-i,coord[2]+i]] \
            + [[coord[0]-i,coord[1]+i,coord[2]+i]] \
            + [[coord[0]+i,coord[1]+i,coord[2]-i]]

    return tmp1
    
    
