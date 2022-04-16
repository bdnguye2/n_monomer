#!/usr/bin/python3

from gen_unit import *
from dupe_code import *

# Main Program

with open("center_super2.txt", "r") as file:
    test = file.read().splitlines()
    center = []
    for i in test:
        center = center + [[float(x) for x in i.split()]]

        
# Generating the NxN supercell and remove duplicates;
# map_center_cell contains maps the center to corresponding unit
# cell 
super_cell = []
var_center = ['c'+str(i) for i in range(len(center))]
map_center_cell = []

for i in range(0,len(center)):
    tmp = gen_unit(center[i],4.429)
    super_cell = super_cell + gen_unit(center[i],4.429)
    map_center_cell = map_center_cell + [[var_center[i],tmp]]

super_cell = duplicate(super_cell)

# Checks for length of the list e.g. two unit cells next
# to each other should give 23 coordinates
#
#print(len(super_cell))
#print(map_center_cell[0][1])
