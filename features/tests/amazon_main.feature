# Created by mrpau at 11/1/2022
Feature: Tests for Amazon main page
  # Enter feature description here

  Scenario: Hamburger menu is present
    # Enter steps here
    Given open amazon page
    Then Verify hamburger menu is present

  Scenario: Footer has correct amount of links
    # Enter Steps here
    Given open amazon page
    Then Verify that footer has 38 links

  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present
