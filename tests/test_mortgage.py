"""
Description: A class used to test the Mortgage class.
Author: Michael Obikwere
Date: 07/04/2025
Usage: Use the tests encapsulated within this class to test the 
MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import (MortgageRate, PaymentFrequency,
                                     VALID_AMORTIZATION) 

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
        
    def test_mutator_raise_valueError_if_loan_amount_is_negative(self):
        # Arrange
        excepted = "Loan Amount must be positive."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(-10, "FIXED_5", "MONTHLY", 5)

        # Assert
        self.assertEqual(str(context.exception), excepted)

    def test_mutator_raise_valueError_if_loan_amount_is_0(self):
        # Arrange
        excepted = "Loan Amount must be positive."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(0, "FIXED_5", "MONTHLY", 5)

        # Assert
        self.assertEqual(str(context.exception), excepted)

    def test_mutator_for_valid_loan_amount(self):
        # Arrange
        loan_amount = 10

        # Act
        mortgage = Mortgage(loan_amount, "FIXED_5", "MONTHLY", 5)

        # Assert
        expected_loan_amount = loan_amount
        self.assertEqual(mortgage._Mortgage__loan_amount, expected_loan_amount)

    def test_mutator_for_valid_rate(self):
        # Arrange
        rate = "FIXED_5"

        # Act
        mortgage = Mortgage(10000, rate, "MONTHLY", 5)

        # Assert
        expected_rate = MortgageRate[rate]
        self.assertEqual(mortgage._Mortgage__rate, expected_rate)

    def test_mutator_raise_valueError_if_rate_is_invalid(self):
        # Arrange
        excepted = "Rate provided is invalid."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(1000, "FIXED_0", "MONTHLY", 5)

        # Assert
        self.assertEqual(str(context.exception), excepted)

    def test_mutator_for_valid_frequency(self):
        # Arrange
        frequency = "MONTHLY"

        # Act
        mortgage = Mortgage(10000, "FIXED_5", frequency, 5)

        # Assert
        expected_frequency = PaymentFrequency[frequency]
        self.assertEqual(mortgage._Mortgage__frequency, expected_frequency)

    def test_mutator_raise_valueError_if_frequency_is_invalid(self):
        # Arrange
        excepted = "Frequency provided is invalid."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(1000, "FIXED_5", "YEARLY", 5)

        # Assert
        self.assertEqual(str(context.exception), excepted)

    def test_mutator_for_valid_amortization(self):
        # Arrange
        amortization = 5

        # Act
        mortgage = Mortgage(10000, "FIXED_5", "MONTHLY", amortization)

        # Assert
        expected_amortization = amortization
        self.assertEqual(mortgage._Mortgage__amortization, expected_amortization)

    def test_mutator_raise_valueError_if_amortization_is_invalid(self):
        # Arrange
        excepted = "Amortization provided is invalid."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(1000, "FIXED_5", "MONTHLY", 0)

        # Assert
        self.assertEqual(str(context.exception), excepted)

    def test_calculate_payment_returns_payment(self):
        # Arrange
         loan_amount = 682912.43
         rate = "FIXED_1"
         frequency = "MONTHLY"
         amortization = 10
         mortgage = Mortgage(loan_amount, rate, frequency, amortization)




        # Act
         actual = mortgage.calculate_payment()
         expected = 7578.30

        # Assert
         self.assertAlmostEqual(actual, expected, places=2)
    
    def test_str_returns_correct_strings_2(self):
    # Arrange
        loan_amount = 682912.43
        rate = "FIXED_3"
        frequency = "MONTHLY"
        amortization = 30
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)




    # Act
        actual = str(mortgage)
        expected = (f"Mortgage Amount: ${loan_amount:,.2f} \n"
            + f"Rate: {MortgageRate[rate].value * 100:.2f}% \n"
            + f"Amortization: {amortization} \n"
            + f"Frequency: {PaymentFrequency[frequency]} -- Calculated Payment: ${mortgage.calculate_payment():,.2f}")

    # Assert
        self.assertEqual(actual, expected)

    def test_str_returns_correct_strings_3(self):
    # Arrange
        loan_amount = 682912.43
        rate = "FIXED_3"
        frequency = "BI_WEEKLY"
        amortization = 30
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)




    # Act
        actual = str(mortgage)
        expected = (f"Mortgage Amount: ${loan_amount:,.2f} \n"
            + f"Rate: {MortgageRate[rate].value * 100:.2f}% \n"
            + f"Amortization: {amortization} \n"
            + f"Frequency: {PaymentFrequency[frequency]} -- Calculated Payment: ${mortgage.calculate_payment():,.2f}")

    # Assert
        self.assertEqual(actual, expected)
    def test_str_returns_correct_strings(self):
    # Arrange
        loan_amount = 682912.43
        rate = "FIXED_3"
        frequency = "WEEKLY"
        amortization = 30
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)




    # Act
        actual = str(mortgage)
        expected = (f"Mortgage Amount: ${loan_amount:,.2f} \n"
            + f"Rate: {MortgageRate[rate].value * 100:.2f}% \n"
            + f"Amortization: {amortization} \n"
            + f"Frequency: {PaymentFrequency[frequency]} -- Calculated Payment: ${mortgage.calculate_payment():,.2f}")

    # Assert
        self.assertEqual(actual, expected)

    def test_repr_returns_correct_strings(self):
    # Arrange
        loan_amount = 682912.43
        rate = "FIXED_1"
        frequency = "MONTHLY"
        amortization = 30
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)




    # Act
        actual = repr(mortgage)
        expected = (f"Mortgage({loan_amount}, "
                    + f"{MortgageRate[rate].value}, "
                    + f"{PaymentFrequency[frequency].value}, "
                    + f"{amortization})")

    # Assert
        self.assertEqual(actual, expected)