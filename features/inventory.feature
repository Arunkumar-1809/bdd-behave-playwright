Feature: Product Inventory and Cart
  As a logged-in user
  I want to browse products and add them to my cart
  So that I can purchase items

  Background:
    Given I am logged in as "standard_user"

  Scenario: Add a single product to the cart
    When I add "Sauce Labs Backpack" to the cart
    Then the cart badge should show "1"

  Scenario: Add multiple products to the cart
    When I add "Sauce Labs Backpack" to the cart
    And I add "Sauce Labs Bike Light" to the cart
    Then the cart badge should show "2"

  Scenario: Remove a product from the cart
    Given I have added "Sauce Labs Backpack" to the cart
    When I remove "Sauce Labs Backpack" from the cart
    Then the cart badge should not be visible

  Scenario: Sort products by price low to high
    When I sort products by "Price (low to high)"
    Then the first product listed should be "Sauce Labs Onesie"
