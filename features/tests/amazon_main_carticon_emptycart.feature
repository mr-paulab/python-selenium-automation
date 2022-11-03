# Created by mrpau at 10/12/2022
Feature: Test for empty shopping cart
  # Test for empty shopping cart

  Scenario: # User sees empty cart after cart icon click
    # Enter steps here
    Given Open amazon home page
    When Click on Cart
    Then Verify Cart page opens cart empty