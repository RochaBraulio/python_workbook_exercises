# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 18:21:55 2025

@author: rocha
"""

# Create a program that displays your name and complete mailing address
# formatted in the manner that you would usually see it on the outside 
# of an envelope. Your program does not need to read any input from the user.

pronoun = "Mr." # Mr., Mrs, Ms,
first_name = "John"
last_name = "Smith"
street_name = "Berkeley St."
house_number = "81"
apartment_number = "4B"
country = "USA"
city = "California"
postal_code = "48202"

print(f'{first_name} {last_name}')
print(f'{street_name}, {house_number} - {apartment_number}')
print(f'{city}, {country} - {48202}')