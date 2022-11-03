# Created by mrpau at 11/2/2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: # User can open and close Amazon Privacy Notice
    # Conditions of use = COU
    Given Open cou page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to new window
    Then Verify Amazon Privacy Notice page is opened
    And Close new window and switch back to original
#    # Enter steps here