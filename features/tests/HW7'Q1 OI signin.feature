# Created by mrpau at 10/1/2022
Feature: # Homework 7 Question 1 Page Object version
  Test for sign in page at order click

  Scenario: User can see empty cart after logging in and clicking cart icon
    Given Open amazon page
    When Click Returns and Orders
    Then Verify Sign In page opened
