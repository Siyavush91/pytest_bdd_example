# Created by penguin at 13.02.2021
Feature: Валидаторы - это тип компании который может получать заявки для обработки. Например верифицировать документы.
  Здесь мы широко трактуем понятие валидатора –это м.б и валидатор для обработки персональных документов пользователя или консультант,
  который получает документы компании на проверку или любая другая роль со схожим механизмом.

  Background:
    Given MidHub create company for user via bot
    And   Midhub auth page is displayed
    When  I click welcome button
    And   I enter a pin and login
    And   I wait when loader disappeared

  Scenario: Invite validator
    Then I should see admin main page
    When I click admin button
    Then I am on Admin page
    When I click Invite validator
    Then I verify Invite validator page
    When I click Invite validator link on Connect partners page
    Then I verify expanded Invite validator block
    When I input address field
    And  I click the checkbox
    And  Click invite button
    Then I verify "Company name" with status "Access requested" in Invited validators tab
    When User accepts permission via bot
    And  I click Invite validator button
    Then I verify approval page for "Validator"
    When I click the checkbox
    And  I click invite button
    Then I verify "Company name" with status "Approved" in Invited validators tab
    When I logging out
    And  I logging in as another user
    Then I see admin main page
    When I click admin button
    Then I am on Admin page
    When I click Accept validator role
    #проверить только заголовок
    #Then I verify Invitation to become a validator page
    # и проверить что приглашение отображается
    #Then I verify item with validator invite
    When I click on validator invite
    Then I verify accept invitation page for "Validator"


  Scenario: Invite validator with two approve
 #TODO  обсудить как лучше реализовать, так как нужно проверить приглашение на разных уровнях






