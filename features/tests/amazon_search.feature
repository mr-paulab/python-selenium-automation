# Created by mrpau at 10/10/2022
Feature: Test for amazon search

  Scenario: # User can search for a product
    # Enter steps here
    Given Open amazon page
    When Search for milk oolong tea
    Then Search results for "milk oolong tea" are shown

  Scenario: # User can search for a product2
    # Enter steps here
    Given Open amazon page
    When Search for mug
    Then Search results for "mug" are shown