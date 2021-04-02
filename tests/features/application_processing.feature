# Created by penguin at 19.06.2020
    @all @application
Feature: SuperAgent can process documents
    As a SuperAgent with validator role,
    I want to open formed document and verify, cancel or pause it

    Background:
        Given User send document in the pool and I get it
        And  Midhub auth page is displayed
        When I click welcome button
        And  I enter a pin and login
        And  I wait when loader disappeared


    @smoke
    Scenario: Verify document
        Then I should see admin main page
        When I click go to processing
        And  I get to the Application page
        Then I verify formed application
        When I click on application
        Then I should see document page
        When I click checkbox
        And  Click Accept button
        And  I'm land on Application page
        Then I should see application disappeared after several page refreshes
    @smoke
    Scenario: Reject document
        Then I should see admin main page
        When I click go to processing
        And  I get to the Application page
        Then I verify formed application
        When I click on application
        Then I should see document page
        When I click checkbox
        And  Click Reject button
        Then I see popup with input field for message
        When I input message and click Send button
        And I'm land on Application page
        Then I should see application disappeared after several page refreshes

    @smoke
    Scenario: Verify after suspend
        Then I should see admin main page
        When I click go to processing
        And  I get to the Application page
        Then I verify formed application
        When I click on application
        Then I should see document page
        When I click checkbox
        And  I click suspend button
        And  I'm land on Application page
        Then I should see application disappeared after several page refreshes
        When I go to In proccess page
        Then I verify formed application
        When I click on application
        Then I should see document page
        When I click checkbox
        And  Click Accept button
        Then I should see application disappeared after several page refreshes
