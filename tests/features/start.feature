# Created by penguin at 01.06.2020
    @smoke
Feature: SuperAgent can login by pin in Midhub Global company and have all roles interface
    As a SuperAgent,
    I want to auth by pin in Midhub Global admin and use all functions

    Background:
      Given Midhub auth page is displayed

    Scenario: SuperAgent authorize
        Then I verify Welcome screen
        When I click welcome button
        Then I verify Admin Login screen
        When I enter a pin and login
        And  I wait when loader disappeared
        Then I verify admin main page
