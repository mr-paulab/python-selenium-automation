# Created by mrpau at 10/12/2022
Feature: # Test for Sign In when clocking and Returns and Orders
  # Enter feature description here

  Scenario: # User can see Sign In after clicking Returns and Orders
    # Enter steps here
    Given Open amazon page
    When Click on Returns and Orders
    Then Verify Sign In page opened
