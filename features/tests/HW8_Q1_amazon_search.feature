# Created by mrpau at 10/10/2022
Feature: Tests for amazon search
  Scenario Outline: User can select and search in a department
    Given Open amazon page
    When Select department by value <value>
    And Search for <search_term>
    Then Verify <department> department is selected
    Examples:
    |value         |search_term                      |department     |
    |appliances    |Breville smart oven air fryer    |appliances     |
    |toys-and-games|Carrera slot cars                |toys-and-games |