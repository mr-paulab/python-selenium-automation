# Created by mrpau at 10/12/2022
Feature: # Enter feature description here
  Test for sign in page at order click

  Scenario: # User can see empty cart after logging in and clicking cart icon
    # Enter steps here
    Given Open amazon page
    When Click on Returns and Orders
    Then Verify Sign In page opened
