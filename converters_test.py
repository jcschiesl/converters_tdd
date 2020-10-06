"""Unit tests for the unit converter library functions"""

#import the functions to be tested
from converters import psi2kpa, kpa2psi, mpg2lpkm, lpkm2mpg 

def describe_a_library_of_units_converters():
    
    """Test suite for units conversion functions"""
    # pylint: disable=unused-variable

    def blows_smoke():
      assert True
    
    def can_convert_psi_to_kpa():
      assert psi2kpa(32) == 220.631712 #32 PSI == 220.631712 
      assert psi2kpa(8.5) == 58.6052985 #8.5 PSI == 58.6054 basketball pressure

    def can_convert_kpa_to_psi():
      assert kpa2psi(101.325) == 14.695952495133 # KPa -> PSI; avg air pressure at sea level
      assert kpa2psi(220.631712) == 31.999932479367043 # KPa -> PSI; avg car tire pressure

    def can_convert_mpg_to_LpKM():
      assert mpg2lpkm(40) == 5.8803694563 #mpg -> litres per 100km; average car mpg
    
    def can_convert_LpKM_to_mpg():
      assert lpkm2mpg(9.4) == 25.022895167663442 #litre per 100 km converted to mpg; 2018 fuel consumption
