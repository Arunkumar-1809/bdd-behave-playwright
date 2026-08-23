Feature: Login
  As a registered user of Sauce Demo
  I want to log in with my credentials
  So that I can access the product inventory

  Background:
    Given I am on the Sauce Demo login page

  Scenario: Successful login with valid credentials
    When I log in with username "standard_user" and password "secret_sauce"
    Then I should be redirected to the inventory page
    And I should see the page title "Products"

  Scenario: Login fails with invalid password
    When I log in with username "standard_user" and password "wrong_password"
    Then I should see an error message containing "Username and password do not match"

  Scenario: Login fails with locked out user
    When I log in with username "locked_out_user" and password "secret_sauce"
    Then I should see an error message containing "Sorry, this user has been locked out"

  Scenario Outline: Login fails with missing credentials
    When I log in with username "<username>" and password "<password>"
    Then I should see an error message containing "<error_message>"

    Examples:
      | username       | password      | error_message                    |
      |                | secret_sauce  | Username is required             |
      | standard_user  |               | Password is required             |
