# Created by mrpau at 10/12/2022
Feature: Test for product search add to cart verify cart
  # Enter product name in search bar, click, add item to cart from search results page

  Scenario: Test for product search add to cart verify cart
    # Enter steps here
    # Steps_1
    Given Open amazon home page
    When Search for oolong tea
    # Steps_2
    And oolong tea search results displayed
    And click to display one product page
    # Steps_3
    And verify page for product
    And click one time purchase button
    And click add to cart for single product
    # Steps_4
    Then chosen product is in cart