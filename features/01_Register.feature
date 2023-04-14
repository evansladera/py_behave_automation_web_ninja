@registration_functionality
Feature: Registration functionality

#  Background: Get page
#    Given User navigates to Register Account page
  @registration_empty_fields
  Scenario: User creates an account without filling any details
    Given User navigates to Register Account page
    When User dont enter any details into fields
    And User clicks on Continue button
    Then User should get proper warning messages for every mandatory field

  @registration_mandatory_fields
  Scenario: User creates an account only with mandatory fields
    Given User navigates to Register Account page
    When User enters the details into below fields
      | firstName | lastName | email           | telephone  | password |
      | Evans     | Ladera   | evans@gmail.com | 1234567890 | 123456   |
    And User selects Privacy Policy
    And User clicks on Continue button
    Then User account should get created successfully

  @registration_all_fields
  Scenario: User creates an account with all fields
    Given User navigates to Register Account page
    When User enters the details into below fields
      | firstName | lastName  | email            | telephone  | password |
      | Johary    | Hernandez | johary@gmail.com | 1234567890 | 123456   |
    And User selects Yes for Newsletter
    And User selects Privacy Policy
    And User clicks on Continue button
    Then User account should get created successfully

  @registration_duplicate_account
  Scenario: User creates a duplicate account
    Given User navigates to Register Account page
    When User enters the details into below fields
      | firstName | lastName  | email           | telephone  | password |
      | Johary    | Hernandez | evans@gmail.com | 1234567890 | 123456           |
    And User selects Yes for Newsletter
    And User selects Privacy Policy
    And User clicks on Continue button
    Then User should get a proper warning about duplicate email

