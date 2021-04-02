# TODO: waiting for ids
# Created by penguin at 28.07.2020
Feature: SuperAgent can create domains.
  Everything on the platform depends on domains,
  domains need to be managed, they need to be created, as well as transferred.
  We already have main Domain which call Midhub Global
  and Subdomain "Российская Федерация"

  # Enter feature description here
  Background:
    Given Midhub auth page is displayed
    When I click welcome button
    And  I enter a pin and login
    And  I wait when loader disappeared

  #TODO refactor scenario for a specific domain [Kazakhstan] with domain code KZ
  Scenario: Create Subdomain in Midhub Global
    Then I should see admin main page
    When I click admin button
    Then I am on Admin page
    When I click Domains
    Then I verify Domains page
    When I click Midhub Global
    Then I verify MH Global Management page
    When I open Subdomain menu
    Then I verify Subdomain menu options
    When I choose "Create subdomain" option in Subdomain menu
    Then I verify Create Subdomain page
    When I fill test domain name
    And  I fill country code
    And  I accept rules on Create Subdomain page
    And  I tap create button on Create Subdomain page
    # TODO: created domain displays only after page update
    And  I update Domain Management page
    Then I verify created domain on Domain Management page

  # TODO
  # Scenario: Create domains
    # Enter steps here
