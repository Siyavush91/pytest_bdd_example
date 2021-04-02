# Created by penguin at 07.08.2020
    @all
Feature: Invite employees and manage them
    Company need employees for process applications
    User must have all documents which need a company for invite him
    Executive can invite employees to the company by them DID
    Executive can change employee role,
    can banned, fired and work with requests on firing

    Background:
        Given MidHub verifies user ownership documents via bot
        And  Midhub auth page is displayed
        When I click welcome button
        And  I enter a pin and login
        And  I wait when loader disappeared
      @smoke
    Scenario: Invite manager
        Then I should see admin main page
        When I click admin button
        Then I verify Admin page
        When I click Team Management
        Then I verify Team Management page
        When I expand Invite Employee block
        And  I input address of employee
        And  I click the checkbox in Invite Employee block
        And  I click invite button in Invite Employee block
        And  I go to Pending authorization tab
        Then I should see permission with status "Access is requested"
        When User accepts permission via bot
        Then I should see permission with status "Data are received"
        And  I should see Open button in permission
        When I click Open permission button
        And  I verify check document page
        And  I click Manager button
        Then I am on Authorized employees tab
        When I go to Pending authorization tab
        Then I should see permission with status "Invite is sent"
        When I logging out
        And  I logging in as another user
        Then I verify Privacy Policy page
        When I agree with privacy policy
        Then I verify Nickname Extended Form page
        When I fill Nickname Extended form
        Then I see admin main page
    @smoke
    Scenario: Invite employee
        Then I should see admin main page
        When I click admin button
        Then I verify Admin page
        When I click Team Management
        Then I verify Team Management page
        When I expand Invite Employee block
        And  I input address of employee
        And  I click the checkbox in Invite Employee block
        And  I click invite button in Invite Employee block
        And  I go to Pending authorization tab
        Then I should see permission with status "Access is requested"
        When User accepts permission via bot
        Then I should see permission with status "Data are received"
        And  I should see Open button in permission
        When I click Open permission button
        And  I verify check document page
        And  I click Employee button
        Then I am on Authorized employees tab
        When I go to Pending authorization tab
        Then I should see permission with status "Invite is sent"
        When I logging out
        And  I logging in as another user
        Then I verify Privacy Policy page
        When I agree with privacy policy
        Then I verify Nickname Extended Form page
        When I fill Nickname Extended form
        Then I see admin main page
