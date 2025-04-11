"""
Description: A class meant to manage Mortgage options.
Author: {Student Name}
Date: {Date}
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import (MortgageRate, PaymentFrequency, 
                                    VALID_AMORTIZATION)

class Mortgage:
    """"
    """
  
    def __init__(self, loan_amount: float, rate: str, frequency: str, amortization: int):
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        
        self.__loan_amount = loan_amount

        try:
            self.__rate = MortgageRate[rate.upper()]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
        try:
            self.__frequency = PaymentFrequency[frequency.upper()]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")
        
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        
        self.__amortization = amortization

    # Accessor
    # Accessor for loan_amount
    @property 
    def loan_amount(self):
        return self.__loan_amount
    
    # Mutator
    #Mutator for loan amount, raises an error if loan amount is invalid
    @loan_amount.setter
    def loan_amount(self, loan_amount: int):
        if loan_amount <= 0:
            raise ValueError( "Loan Amount must be positive.")
        self.__loan_amount = loan_amount

     # rate Accessor
    @property
    def rate(self):
        return self.__rate
    
    # rate Mutator
    @rate.setter
    def rate(self, rate: str):
        try:
            rate = MortgageRate[rate.upper()]
        except ValueError as e:
            raise ValueError("Rate provided is invalid.")

        self.__rate = rate

    