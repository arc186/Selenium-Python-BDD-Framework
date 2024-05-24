Feature: Login Functionality
  @login  @dd
  Scenario Outline: Login with valid credentials
    Given  open login page
    When enter valid email_address as "<email>" and valid password as "<password>"
    And click on login button
    Then should logging successfully
    Examples:
      | email           | password |
      |lmnop@gmail.com  |lmnop123  |
      |lmnop3@gmail.com |lmnop456  |
      |lmnop2@gmail.com |lmnop789  |

  @login
  Scenario: Login with invalid credentials
    Given open login page
    When enter invalid email address and invalid password "lmnop12"
    And click on login button
    Then display proper warning message
  @login
  Scenario: Login with valid email address and invalid password
    Given  open login page
    When enter valid email address "lmnop@gmail.com" and invalid password "lmnop12"
    And click on login button
    Then display proper warning message
  @login
  Scenario: Login with invalid email address and valid password
    Given open login page
    When enter invalid email address and valid password "lmnop123"
    And click on login button
    Then display proper warning message
  @login
  Scenario: Login with not entering any credentials
    Given open login page
    When not entering any credential details
    And click on login button
    Then display proper warning message
  @login
  Scenario: Login with entering valid email address only
    Given open login page
    When enter valid email address "lmnop@gmail.com" only
    And click on login button
    Then display proper warning message
  @login
  Scenario: Login with entering valid password only
    Given open login page
    When enter valid password "lmnop123" only
    And click on login button
    Then display proper warning message



