# Created by penguin at 07.07.2020
  @all
Feature: Company invite.
  SuperAgent can create a company for a user with the right to manage the company.
  MidHub verifies user ownership documents.
  User finds a company that invites him to the system and transfers his DID to the executive of this company.
  Executive of SuperCompany can invite user. The invited user as Founder configures the company.
  Configures include inviting Co-founders and executive

  Background:
    Given MidHub verifies user ownership documents via bot
    And   Midhub auth page is displayed
    When  I click welcome button
    And   I enter a pin and login
    And   I wait when loader disappeared

  @smoke
      #BUG Can't create Privacy Policy for new company via bot
      #TODO https://midhub.atlassian.net/browse/MHNEW-1646
  Scenario: Approve company invite and first auth with it and setup
      Then I should see admin main page
      When I click admin button
      Then I am on Admin page
      When I click Connect partners
      Then I verify Connect partners page
      When I click Add new partner link on Connect partners page
      Then I verify expanded Add New Partner block
      When I fill company name "MidhubCompany" field
      And  I input address field
      And  I click the checkbox
      And  Click invite button
      Then I verify "MidhubCompany" with status "Waiting for confirmation" in Requested partners tab
      When User accepts permission via bot
      And  I click Open button
      Then I verify approval page for "MidhubCompany"
      When I click invite button
      Then I verify "MidhubCompany" with status "Accepted" in Requested partners tab
      When I logging out
      And  I logging in as another user
      Then I verify Privacy Policy page
      When I agree with privacy policy
      Then I verify Invite Company Setup page
      When I fill an address field
      And  I invite executive
      And  Executive accepts the invitation via bot
      Then I should see executive document
      When I click finish settings
      Then I verify Nickname Form page
      When I fill Nickname form
      Then I see admin main page

  # BUG: this scenario will not work until scenario "Cancel company invite" will continue create broken invites
  Scenario: Cancel company invite on the setup form
      Then I should see admin main page
      When I click admin button
      Then I am on Admin page
      When I click Connect partners
      Then I verify Connect partners page
      When I click Add new partner link on Connect partners page
      Then I verify expanded Add New Partner block
      When I fill company name "MidhubCompany" field
      And  I input address field
      And  I click the checkbox
      And  Click invite button
      And  User accepts permission via bot
      And  I click Open button
      Then I verify approval page for "MidhubCompany"
      When I click invite button
      And  I logging out
      Then I should see Login page
      When I logging in as another user
      Then I verify Privacy Policy page
      When I agree with privacy policy
      Then I verify Invite Company Setup page
      When I click cancel company button
      Then Midhub auth page is displayed

  # BUG: doesn't work cancel company
  Scenario: Cancel company invite
      Then I should see admin main page
      When I click admin button
      Then I am on Admin page
      When I click Connect partners
      Then I verify Connect partners page
      When I click Add new partner link on Connect partners page
      Then I verify expanded Add New Partner block
      When I fill company name "MidhubCompany" field
      And  I input address field
      And  I click the checkbox
      And  Click invite button
      And  User accepts permission via bot
      And  I click Open button
      Then I verify approval page for "MidhubCompany"
      When I click cancel button
      Then I should see permisson disappeared
