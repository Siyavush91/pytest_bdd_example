# Created by penguin at 28.10.2020
Feature: Requirements
  Верификации это требование для валидаторов, которые позволяют дать валидатору право обрабатывать документы
  по шаблонам.
  Верификации создаются, прикрепляются к существующему шаблону.
  Валидатор по этому шаблону может верифицировать документ

  Background:
    Given   Midhub auth page is displayed
    When  I click welcome button
    And   I enter a pin and login
    And   I wait when loader disappeared
  @smoke
  Scenario: Create requirements
    Then I should see admin main page
    When I click admin button
    Then I am on Admin page
    When I click Domains
    Then I verify Domains page
    When I click Requirements tab
    Then I verify Requirements page
    When I click create requirement
    Then I verify Create Requirements page
    When I fill test name on Create Requirements page
    And  I fill test description on Create Requirements page
    And  I choose domain "Midhub Global" on Create Requirements page
    And  I choose "Глобальный желтый" type of verification on Create Requirements page
    And  I enable checkbox "Международная желтая" on Create Requirements page
    And  I enable checkbox "Международная зеленая" on Create Requirements page
    And  I click Add document button on Create Requirements page
    Then I verify expanded docs section on Create Requirements page
    When I open "Midhub Global" docs on Create Requirements page
    And  I open "РОССИЙСКАЯ ФЕДЕРАЦИЯ" docs on Create Requirements page
    And  I enable checkbox "Приказ о назначении ген. директора" doc on Create Requirements page
    And  I click Choose button for doc on Create Requirements page
    Then I verify added doc "Приказ о назначении ген. директора" on Create Requirements page
    When I click Create requirement button on Create Requirements page
    # TODO: no added requirement without update
    And  I update Requirements page
    Then I verify created requirement for "Midhub Global" domain with "Глобальный желтый" type on Requirements page
    When I click on created requirement on Requirements page
    Then I verify Requirement page
    And  I verify test name on Requirement page
    And  I verify test description on Requirement page
    And  I verify "Midhub Global" domain on Requirement page
    And  I verify "Глобальный желтый" type of verification on Requirement page
    And  I verify "Международный:" type for documents on Requirement page
    # TODO: can't check green and yellow
    And  I verify "Приказ о назначении ген. директора" doc on Requirement page

    Scenario: Attaching verification to a template
      Then I should see admin main page
      When I click admin button
      Then I am on Admin page
      When I click Domains
      Then I verify Domains page
      When I click Requirements tab
      Then I verify Requirements page
      When I click create requirement
      Then I verify Create Requirements page
      When I fill test name on Create Requirements page
      And  I fill test description on Create Requirements page
      And  I choose domain "Midhub Global" on Create Requirements page
      And  I choose "Глобальный желтый" type of verification on Create Requirements page
      And  I enable checkbox "Международная желтая" on Create Requirements page
      And  I enable checkbox "Международная зеленая" on Create Requirements page
      And  I click Add document button on Create Requirements page
      Then I verify expanded docs section on Create Requirements page
      When I open "Midhub Global" docs on Create Requirements page
      And  I open "РОССИЙСКАЯ ФЕДЕРАЦИЯ" docs on Create Requirements page
      And  I enable checkbox "Приказ о назначении ген. директора" doc on Create Requirements page
      And  I click Choose button for doc on Create Requirements page
      Then I verify added doc "Приказ о назначении ген. директора" on Create Requirements page
      When I click Create requirement button on Create Requirements page
      # TODO: no added requirement without update
      And  I update Requirements page
      Then I verify created requirement for "Midhub Global" domain with "Глобальный желтый" type on Requirements page
      When I click Domains
      Then I verify Domains page
      When I click Midhub Global
      Then I verify MH Global Management page
      When I click subdomain "РОССИЙСКАЯ ФЕДЕРАЦИЯ" on the MH Global Management page
      Then I verify РОССИЙСКАЯ ФЕДЕРАЦИЯ Managment page
      When I choose "Паспорт гражданина РФ" template in РОССИЙСКАЯ ФЕДЕРАЦИЯ Managment page
      Then I verify Template constructor with document
          # нужно проверить общие элементы при открытии данного экрана для разных шаблонов
          # кнопка "Создать черновик новой версии", блок "Требования к международной проверке", блок "Требования к локальной проверке"
      And  I verify Template constructor with "Паспорт гражданина РФ" data
          # нужно проверить элементы связанный с паспортом РФ "Свойства документа" с полем "Наименование документа" и Категория -Удостоверение личности
          # Поля документа - думаю нескольких достаточно
      When I click "Добавить требования" button on "Требования к международной проверке" block
      Then I verify Choose global requirements page
      #проверяем наличие кнопок и заголовка
      And  I verify created requirement for "Midhub Global" domain with "Глобальный желтый" type on Choose global requirements page
      When I enable checkbox on created requirement on Choose global requirements page
      And  I click Choose button for doc on Choose global requirements page
      Then I verify Global Requirement page
      # проверяем что поля Стоимость выпуска и Стоимость использования не доступны для ввода, т.к. документ относится к категории-удостоверение личности
      When I click Add button
      And  I verify Template constructor with "Паспорт гражданина РФ" data
      And  I verify added requirement
