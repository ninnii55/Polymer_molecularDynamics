import sys
import numpy
import math
from decimal import Decimal

# formular trying to recreate for ;
# peptide = {[(Box volume (cm3)*density of water)*percent ratio OF PEPTIDE]/Mw Of peptide or compund}*Avogardros number
# water = {[(Box volume (cm3)*density of water)*percent ratio OF WATER]/Mw Of WATER}*Avogardros number 

#Constants
waterMw = 18.01 # g/mol
liquidDensity = 1.03 # kg/m³ 
avoNumber = 6.023E+23

# Input
polymerMw_input = input("Enter polymerMw values separated by commas: ")
polymerMw_values = [float(value) for value in polymerMw_input.split(',')]
ensembleSize = float(input("What is the size of simulation (cube) in nm? "))
percentPolymer = float(input("What % in w/v of polymer solution you need? ")) / 100
boxSize = ((ensembleSize * ensembleSize * ensembleSize) * 1e-21)  # conversion from nm3 to cm3

# Function for polymer/protein/peptides
def numOfpolymermolecules(polymerMw_values, ensembleSize, percentPolymer):
    total_result = 0
    for polymerMw in polymerMw_values:
        result = (((boxSize * liquidDensity) * percentPolymer) / polymerMw) * avoNumber
        total_result += result

    average_result = total_result / len(polymerMw_values)
    return print(f'\n The average number of polymers you need in a {boxSize} cm^3 box is: {round(average_result, 2)} peptides', flush=True)

# Call the function
numOfpolymermolecules(polymerMw_values, ensembleSize, percentPolymer)

percentWater = (float((input("what % in w/v of water you need? "))))/100

#Function for water
def numOfWatermolecules(waterMw, ensembleSize, percentWater):
    #maths of function
    result = (((boxSize * liquidDensity) * percentWater)/waterMw) * avoNumber
    return print(f'\n The number of waters you need in a {boxSize} cm^3 box is: {round(result,2)} waters', flush=True)

#call the function
numOfWatermolecules(waterMw, ensembleSize, percentWater)