"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION 

class MortgageTests(TestCase):

    def test_init_raises_invalid_loan_amount_value_error(self):
        # Arrange
        loan_amount = -0
        rate = "FIXED_5"
        frequency = "MONTHLY"
        amortization = 5
        excepted = "Loan Amount must be positive."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)

        # Assert
        self.assertEqual(str(context.exception), excepted)

    def test_init_raises_invalid_rate_value_error(self):
        # Arrange
        loan_amount = 100
        rate = "FIXED_0"
        frequency = "MONTHLY"
        amortization = 5
        excepted = "Rate provided is invalid."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)

        # Assert
        self.assertEqual(str(context.exception), excepted)

    def test_init_raises_invalid_frequency_value_error(self):
        # Arrange
        loan_amount = 100
        rate = "FIXED_5"
        frequency = "YEARLY"
        amortization = 5
        excepted = "Frequency provided is invalid."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)

        # Assert
        self.assertEqual(str(context.exception), excepted)

    def test_init_raises_invalid_amorization_value_error(self):
        # Arrange
        loan_amount = 100
        rate = "FIXED_5"
        frequency = "MONTHLY"
        amortization = 0
        excepted = "Amortization provided is invalid."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)

        # Assert
        self.assertEqual(str(context.exception), excepted)

    def test_init_is_set_if_valid_attributes(self):
        
        # Arrange
        loan_amount = 1000
        rate = "FIXED_5"
        frequency = "MONTHLY"
        amortization = 5

        #Act
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        
        # Assert
        # Isolate each test and test for when the are all valid.
        excepted_loan_amount = 1000
        excepted_rate = MortgageRate[rate]
        excepted_frequency = PaymentFrequency[frequency]
        excepted_amortization = amortization
        self.assertEqual(excepted_loan_amount, mortgage._Mortgage__loan_amount)
        self.assertEqual(excepted_rate, mortgage._Mortgage__rate)
        self.assertEqual(excepted_frequency, mortgage._Mortgage__frequency)
        self.assertEqual(mortgage._Mortgage__amortization, excepted_amortization)
        