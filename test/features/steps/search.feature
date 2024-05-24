Feature: Search Functionality
  @search
  Scenario: Search For Valid Product
    Given Navigate to home page
    When enter valid product "HP" in search Box field
    And  click on search button
    Then valid product should be display on screen
  @search
  Scenario: Search For Invalid Product
    Given Navigate to home page
    When enter invalid product "DELL" in search Box field
    And  click on search button
    Then proper error message should be display on screen
  @search
  Scenario: Search without entering any Product
    Given Navigate to home page
    When dont enter anything on search box filed
    And  click on search button
    Then proper error message should be display on screen


