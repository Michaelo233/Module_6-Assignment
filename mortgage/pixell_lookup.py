"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: Michael Obikwere
Date: 07/04/2025
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

# amortization 
VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}

# morgage class as Enum
class MortgageRate(Enum):
    """
    Enumeration of Pixell rivers mortgage rates. 
    """
    FIXED_5 = 0.0519
    FIXED_3 = 0.0589
    FIXED_1 = 0.0599
    VARIABLE_5 = 0.0649
    VARIABLE_3 = 0.0669
    VARIABLE_1 = 0.0679

# payment frequency class as Enum
class PaymentFrequency(Enum):
    """
    Enumeration of mortgage payment frequency
    """
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52