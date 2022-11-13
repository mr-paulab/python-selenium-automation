# Created by mrpau at 10/25/2022
Feature: sign in test cases
  # Enter feature description here

  Scenario: # Sign In page can be opened from SignIn popup
    # Enter steps here
    Given Open amazon page
    When Click on button from SignIn popup
    Then Verify Sign In URL opened

 Scenario: Amazon users see sign in button
   Given open amazon page
   Then Verify Sign In is clickable
   When Wait for 5 sec
   Then Verify Sign In is clickable
   Then Verify Sign in disappears
