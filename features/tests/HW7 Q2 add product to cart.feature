# HW7 Q2 add product to cart using Page Object Model
#
# Created by mrpau at 11/19/2022
Feature: # Enter feature name here
  # Use Page Object Model

  Scenario: Add to cart verify cart using POM
    Given Open amazon page
    When Search for organic oolong tea
    Then Search results for organic oolong tea are shown
    And click to display one product page
    And click one-time purchase button
    Then click add to cart button
