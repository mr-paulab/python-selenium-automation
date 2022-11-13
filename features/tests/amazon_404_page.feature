# Created by mrpau at 11/1/2022
Feature: Tests for 404 page
  # Enter feature description here

  Scenario: User is able to navigate to amazon blog from 404 page
    # Enter steps here
    Given Open Amazon product B07NF5WGQ11111111 page
    And Store original window
    When Click on dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window
 #   And Return to original window
