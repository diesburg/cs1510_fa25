"""
Name: Diesburg
Program: wage.py
Description: This program asks for a wage and
              calculates the full time amount a
              person would earn per week.
"""

hours = 40

hourly_wage = input("Please enter wage per hour: ")
hourly_wage = float(hourly_wage)

weekly_wage = hourly_wage * hours

print("Your weekly wage is",weekly_wage)
