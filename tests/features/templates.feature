# Created by penguin at 13.12.2020
Feature: Templates.
  Созданные шаблоны могут заполнять пользователи и отправлять их на проверку.
  Шаблоны можно:
  создавать, публиковать, редактировать, передавать между доменами
  Создание/редактирование шаблона происходит в специальном конструкторе шаблона.
  В нем можно добавлять свойства документа и создавать/удалять поля. Заполненные шаблоны можно публиковать или сохранять
  в черновик. Черновики можно редактировать/удалять.

  Background:
    Given Midhub auth page is displayed
    When I click welcome button
    And  I enter a pin and login
    And  I wait when loader disappeared

  #BUG 404 after open template constructor during loader on main page
  #TODO https://midhub.atlassian.net/browse/MHNEW-1592
  Scenario: Create template in Midhub Global domain
    Then I should see admin main page
    When I click admin button
    Then I am on Admin page
    When I click Domains
    Then I verify Domains page
    When I click Midhub Global
    Then I verify MH Global Management page
    When I click Add template
    Then I verify Create template page
    When I fill name field with test value on Create template page
    And  I select "Citizenship" category on Create template page
    And  I select without verification status on Create template page
    And  I select unique type on Create template page
    And  I fill description field with test value on Create template page
    And  I fill code field with test value on Create template page
    And  I click Add field button on Create template page
    Then I verify add field form on Create template page
    When I close field form on Create template page
    And  I add "Surname" field on Create template page
    And  I add "Name" field on Create template page
    And  I add "Date" field on Create template page
    And  I add "Signature" field on Create template page
    # TODO: no restrictions for number field, but there are for text fields
    And  I add "Number" number field with exact number of characters "10" on Create template page
    # TODO: no opportunity to add options
    And  I add "Gender" option field with "Male, Female" options on Create template page
    And  I add "Photo" photo field on Create template page
    Then I verify "Surname" field on Create template page
    And  I verify "Name" field on Create template page
    And  I verify "Date" field on Create template page
    And  I verify "Signature" field on Create template page
    And  I verify "Number" field on Create template page
    And  I verify "Gender" field on Create template page
    And  I verify "Photo" field on Create template page
    When I click Publish button on Create template page
    Then I verify added template on MH Global Management page
    When I click on added template on MH Global Management page
    Then I verify Template page
    And  I verify test template name on Template page
    And  I verify "Citizenship" category on Template page
    And  I verify without verification status on Template page
    And  I verify unique type on Template page
    And  I verify code field with test value on Template page
    And  I verify description field with test value on Template page
    And  I verify "Surname" field on Template page
    And  I verify "Name" field on Template page
    And  I verify "Date" field on Template page
    And  I verify "Signature" field on Template page
    And  I verify "Number" number field with exact number of characters "10" on Template page
    And  I verify "Gender" option field with "Male, Female" options on Template page
    And  I verify "Photo" photo field on Template page
