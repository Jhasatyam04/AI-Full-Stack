import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 8.5
current_temp = 95.49999999999

print(f"Current temperature: {current_temp}")
print(f"Ideal temperature: {ideal_temp}")
print(f"Difference temp {current_temp - ideal_temp}")
print(sys.float_info)