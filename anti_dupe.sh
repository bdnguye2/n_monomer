#!/bin/bash

# Prints out the number of lines
tmp=$(wc -l $1 | awk '{print $1 }')

# Removes duplicates and adds atoms and Energy=
sed '1s/^/'$tmp'\nEnergy =\n\n/' $1 | uniq
