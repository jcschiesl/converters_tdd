"""Library of units converters"""
#Declarations

NPL = 4.44822 #newtons per lb/ft
IPM = 1550    #sq in per sq meter
LPN = 0.224809 # poundforce per newton
MPI = 0.00064516 # meters sq per inch sq
MPK = 0.621372 # miles per kilometer
LPG = 3.78541 # litres per gallon
KPM = 1.60934 # litres per gallon
GPL = 0.264172 # Gallons per liter


def psi2kpa(psi):
    """
    Takes in a PSI value and converts it to Kpa
    """
    return psi * NPL * IPM / 1000

def kpa2psi(kpa):
    """
    Takes KPa value and converts it to PSI
    """
    return kpa * 1000 * LPN * MPI

def mpg2lpkm(mpg):
    """
    Takes mpg value and converts it to litres per 100 km
    """
    return 1/mpg * MPK * LPG * 100

def lpkm2mpg(lpkm):
    """
    takes litres per 100 km value and converts it to mpg
    """
    return 1/(lpkm * 0.01 * KPM * GPL)