# Created by penguin at 03.08.2020
Feature: Company have they own documents. We need to validate this documents too.
  As executive we need to see documents in domains, select documents and send them to validators.
  After validate we'll see documents, can open them, resend them etc.

  Background:
    Given Midhub auth page is displayed
    When I click welcome button
    And  I enter a pin and login
    And  I wait when loader disappeared

    @smoke
  Scenario: [Паспорт гражданина РФ] Send filled form to verification and send for sign to validator
    Then I should see admin main page
    When I click admin button
    Then I am on Admin page
    When I click Company Documents
    Then I verify Company Documents
    When I click Add document
    And  I choose domain "РОССИЙСКАЯ ФЕДЕРАЦИЯ" on Choose Document screen
    Then I verify "Паспорт гражданина РФ, Приказ о назначении ген. директора" in list on Add Doc screen
    When I click on "Паспорт гражданина РФ" on Add Doc screen
    Then I verify "Паспорт гражданина РФ" template form
    When I fill text field "Фамилия" with value "Петрова"
    And  I fill text field "Имя" with value "Ольга"
    And  I fill text field "Отчество" with value "Антоновна"
    And  I select "Ж" for field "Пол"
    And  I fill text field "Дата рождения" with value "21.01.1993"
    And  I fill text field "Место рождения" with value "Волгоград"
    And  I fill text field "Серия и номер паспорта" with value "4444 444444"
    And  I fill text field "Кем выдан" with value "ТП №1 г.Москва"
    And  I fill text field "Дата выдачи" with value "01.01.2000"
    And  I add 2 photos on template form
    And  I click Next button on template form
    Then I verify "Паспорт гражданина РФ" on Company Documents page 
    When I click on "Паспорт гражданина РФ" on Company Documents page
    Then I verify Document page "Паспорт гражданина РФ" for "Test User1"
    When I click "Send to validation" button
    Then I verify Verification Type Selection page
    When I choose green global verification
    Then I verify Document Preview page "Паспорт гражданина РФ" for "Test User1" with header
    And  I verify send to validator button on Document Preview page
    And  I verify green global verification on Document Preview Page
    When I click "Send to validator" button
    # BUG: uncomment when this bug will be fixed
    # Then I verify no "Паспорт гражданина РФ" on Company Documents page
    When I go to In process tab
    Then I verify In process page
    And  I verify "Паспорт гражданина РФ" with status "Waiting for signing" for "Green Global" verification on In process page
    When I click work button
    Then I should see admin main page
    When I click go to processing
    And  I get to the Application page
    And  I choose domain "РОССИЙСКАЯ ФЕДЕРАЦИЯ" in filters
    And  I click request button until pool is empty
    And  I wait until request button is active
    Then I should see user empty document
    When I click admin button
    Then I am on Admin page
    When I click Company Documents
    Then I verify Company Documents
    When I go to In process tab
    # TODO: please recheck if status is correct
    Then I verify "Паспорт гражданина РФ" with status "Assigned to notary" for "Green Global" verification on In process page
    When I click on "Паспорт гражданина РФ" on In process page
    Then I verify Document Preview page "Паспорт гражданина РФ" for "Test User1"
    And  I verify green global verification on Document Preview Page
    And  I verify encryption buttons on Document Preview page
    # TODO: bug, doesn't work further
    When I click "Encrypt to validator" button
    Then I verify no encryption buttons on Document Preview page
    When I click work button
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
    When I click admin button
    Then I am on Admin page
    When I click Company Documents
    Then I verify Company Documents
    When I go to In process tab
    Then I verify "Паспорт гражданина РФ" with status "Waiting for signing" for "Green Global" verification on In process page
    When I click on "Паспорт гражданина РФ" on In process page
    Then I verify Document Preview page "Паспорт гражданина РФ" for "Test User1"
    And  I verify green global verification on Document Preview Page
    # TODO
    # And  I verify sign and report buttons on Document Preview page
    # When I click "Sign" button
    # Then I verify Company Documents with "Паспорт гражданина РФ" and verification




