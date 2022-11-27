# Created by mrpau at 10/10/2022
Feature: Tests for amazon search
  Scenario: User can select a product and hover over New Arrivals to see deals
    Given Open amazon product page for B074TBCSC8
    When Hover over New Arrivals menu selection
    Then Verify New Arrivals popup is visible
