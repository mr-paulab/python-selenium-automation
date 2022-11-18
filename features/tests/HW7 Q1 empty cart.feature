# Created by mrpau at 11/17/2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: 'Your Amazon Cart is empty' shown if no product added
    # Enter steps here
   Given Open Amazon page
   When Click on cart icon
   Then Verify Your Amazon Cart is empty text