# Created by penguin at 01.06.2020
@all @application
Feature: SuperAgent can request documents from pool
    As a SuperAgent,
    I want to authorize and request documents and see info message if no documents in pool

    Background:
        Given Midhub auth page is displayed
        When I click welcome button
        And  I enter a pin and login
        And  I wait when loader disappeared
    
    # BUG: scenario fails due to lost filter after domain choosing
    @smoke
    Scenario: SuperAgent as operator see info message, if document pool is empty
        Then I should see admin main page
        When I click go to processing
        And  I verify Application page
        When I choose domain "РОССИЙСКАЯ ФЕДЕРАЦИЯ" in filters
        Then  I verify "РОССИЙСКАЯ ФЕДЕРАЦИЯ" is chosen in filters
        When I click request button
        Then I should see No Applications toast
    
    @smoke
    Scenario: SuperAgent as operator role can take documents from pool
        Then I should see admin main page
        When I click go to processing
        And  I get to the Application page
        And  User put empty document in pool
        And  I choose domain "РОССИЙСКАЯ ФЕДЕРАЦИЯ" in filters
        And  I click request button
        And  I wait until request button is active
        Then I should see user empty document
