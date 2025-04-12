"""
Description: A class meant to manage Mortgage options.
Author: Michael Obikwere
Date: 12/04/2025
Usage: Create an instance of the Mortgage class to manage mortgage 
records and calculate payments.
"""

from mortgage.pixell_lookup import (MortgageRate, PaymentFrequency, 
                                    VALID_AMORTIZATION)

# Morgage class
class Mortgage:
    """
    Represents Mortgage Calculation and validation.
    """
  
    def __init__(self, loan_amount: float, rate: str, frequency: str,
                  amortization: int):
        """
        Initialize new mortgage object for clients with loan_amount, 
        mortgage rate, frequency, and how many year of 
        payment(amortization).

        Args:
            loan_amount (float): The clients mortgage loan amount.
            rate (str): mortgage payment rate.
            frequency (str): mortgage payment frequency.
            amortization (int): mortgage amortization.

        Raises:
            loan_amount : raise a value error when loan is invalid.
            rate : raise a value error when rate is not found.
            frequency: raise a value error when frequency is not found.
            amortization : raise a value error when amortization is not
            in amortization list.
        """

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
        """
        Gets the loan amount of the Mortgage.

        Returns:
            float: The loan amount in the Mortgage. 
        """
        return self.__loan_amount
    
    # Mutator
    #Mutator for loan amount, raises an error if loan amount is invalid
    @loan_amount.setter
    def loan_amount(self, loan_amount: int):
        """
        Sets the loan amount of the Mortgage.

        Args:
            loan_amount (float): A non-negative float representing 
            the loan amount.

        Raises:
            ValueError: Raised when the loan amount is a value less
            than or equal to zero.
        """
        if loan_amount <= 0:
            raise ValueError( "Loan Amount must be positive.")
        self.__loan_amount = loan_amount

     # rate Accessor
    @property
    def rate(self):
        """
        Gets the rate of the Mortgage.

        Returns:
            str: The rate in the MortgageRate[Enum]. 
        """
        return self.__rate
    
    # rate Mutator
    @rate.setter
    def rate(self, rate: str):
        """
        Sets the rate of the Mortgage.

        Args:
            rate (str): A string representing rate in 
            MoartgageRate[Enum].

        Raises:
            ValueError: Raised when the rate is not in 
            MortgageRate[Enum].
        """
        try:
            rate = MortgageRate[rate.upper()]
        except ValueError as e:
            raise ValueError("Rate provided is invalid.")

        self.__rate = rate

     
    # frequency Accessor
    @property
    def frequency(self):
        """
        Gets the frequency of the Mortgage.

        Returns:
            str: The frequency in the PaymentFrequency[Enum]. 
        """
        return self.__frequency
    
    # frequency Mutator
    @frequency.setter
    def frequency(self, frequency: str):
        """
        Sets the frequency of the Mortgage.

        Args:
            frequency (str): A string representing frequency in 
            PaymentFrequency[Enum].

        Raises:
            ValueError: Raised when the frequency is not in 
            PaymentFrequency[Enum].
        """
        try:
            frequency = MortgageRate[frequency.upper()]
        except ValueError as e:
            raise ValueError("Frequency provided is invalid.")

        self.__frequency = frequency

       # amortization Accessor
    @property
    def amortization(self):
        """
        Gets the amortization of the Mortgage.

        Returns:
            int: The amortization in the validamortization. 
        """
        return self.__amortization
    
    # amortization Accessor
    @amortization.setter
    def amortization(self, amortization: int):
        """
        Sets the loan amount of the Mortgage.

        Args:
            amortization (int): An int representing the amortization
            in the Mortgage.

        Raises:
            ValueError: Raised when the amortization is not in the 
            amortization list.
        """
        if amortization in VALID_AMORTIZATION:
            amortization = VALID_AMORTIZATION[amortization]
        else:
            raise ValueError("Amortization provided is invalid")
        
        self.__amortization = amortization

    # Calculates the payment according to the mortgage detials.
    def calculate_payment(self):
        """
        Calculates the Mortgage payment of the Mortgage.

        Args:
            PRINCIPAL_LOAN_AMOUNT = loan_amount.
            INTEREST = RATE DIVIDED BY THE FREQUENCY.
            NUMBER_OF_PAYMENTS = AMORTIZATION * FREQUENCY
            payment = (PRINCIPAL_LOAN_AMOUNT * 
                   ((INTEREST * ((1 + INTEREST) ** NUMBER_OF_PAYMENTS)) 
                    / (((1 + INTEREST) ** NUMBER_OF_PAYMENTS) - 1))).

        Returns:
            payment: Mortgage Payment.
        """
        PRINCIPAL_LOAN_AMOUNT =  self.__loan_amount
        INTEREST = self.__rate.value / self.__frequency.value
        NUMBER_OF_PAYMENTS = (self.__amortization *
                               self.__frequency.value)

        payment = (PRINCIPAL_LOAN_AMOUNT * 
                   ((INTEREST * ((1 + INTEREST) ** NUMBER_OF_PAYMENTS)) 
                    / (((1 + INTEREST) ** NUMBER_OF_PAYMENTS) - 1)))
        
        return payment
    
    def __str__(self):
        """
        Return an informal string representation of the object.

        Returns:
            str: An informal string representation of the object.

        Example:
            >>> Mortgage Amount: $682,912.43
            >>> Rate: 5.89%
            >>> Amortization: 30
            >>> Frequency: MONTHLY -- Calculated Payment: $4,046.23
        """
        return(f"Mortgage Amount: ${self.__loan_amount:,.2f} \n"
               + f"Rate: {self.__rate.value * 100:.2f}% \n"
               + f"Amortization: {self.__amortization} \n"
               + f"Frequency: {self.__frequency.name} -- "
               + f"Calculated Payment: "
               + f"${self.calculate_payment():,.2f}")
    
    def __repr__(self):
        """
        Return the canonical string representation of the object.

        Returns:
            str: The canonical string representation of the object.

        Example:
            >>> Mortgage(loan_amount=682912.43, rate=0.0599, 
            frequency=12, amortization=30)
        """
        return(f"Mortgage({self.__loan_amount}, {self.rate.value},"
               f" {self.frequency.value}, {self.amortization})")

