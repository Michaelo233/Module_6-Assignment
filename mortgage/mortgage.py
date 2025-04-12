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

     
    # frequency Accessor
    @property
    def frequency(self):
        return self.__frequency
    
    # frequency Mutator
    @frequency.setter
    def frequency(self, frequency: str):
        try:
            frequency = MortgageRate[frequency.upper()]
        except ValueError as e:
            raise ValueError("Frequency provided is invalid.")

        self.__frequency = frequency

       # amortization Accessor
    @property
    def amortization(self):
        return self.__amortization
    
    # amortization Accessor
    @amortization.setter
    def amortization(self, amortization: int):
        if amortization in VALID_AMORTIZATION:
            amortization = VALID_AMORTIZATION[amortization]
        else:
            raise ValueError("Amortization provided is invalid")
        
        self.__amortization = amortization

    # Calculates the payment according to the mortgage detials.
    def calculate_payment(self):
        PRINCIPAL_LOAN_AMOUNT =  self.__loan_amount
        INTEREST = self.__rate.value / self.__frequency.value
        NUMBER_OF_PAYMENTS = self.__amortization * self.__frequency.value

        payment = (PRINCIPAL_LOAN_AMOUNT * 
                   ((INTEREST * ((1 + INTEREST) ** NUMBER_OF_PAYMENTS)) 
                    / (((1 + INTEREST) ** NUMBER_OF_PAYMENTS) - 1)))
        
        return payment
    
    def __str__(self):
        return(f"Mortgage Amount: ${self.__loan_amount:,.2f} \n"
               + f"Rate: {self.__rate.value * 100:.2f}% \n"
               + f"Amortization: {self.__amortization} \n"
               + f"Frequency: {self.__frequency} -- "
               + f"Calculated Payment: "
               + f"${self.calculate_payment():,.2f}")
    
    def __repr__(self):
        return(f"Mortgage({self.__loan_amount}, {self.rate.value},"
               f" {self.frequency.value}, {self.amortization})")

